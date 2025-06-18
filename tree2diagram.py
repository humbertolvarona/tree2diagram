import os

def parse_tree_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = [line.rstrip('\n') for line in f if line.strip() != '']
    tree = {}
    stack = [(tree, -1)]
    for line in lines:
        stripped = line.lstrip(' │')
        indent = len(line) - len(stripped)
        name = stripped.replace('├── ', '').replace('└── ', '').strip()
        if not name:
            continue
        while stack and stack[-1][1] >= indent:
            stack.pop()
        parent_dict = stack[-1][0]
        parent_dict[name] = {}
        stack.append((parent_dict[name], indent))
    return tree

def to_mermaid(tree, prefix="."):
    lines = []
    def recurse(node, parent):
        for key, value in node.items():
            child = f"{parent}_{key}".replace('.', '').replace('-', '')
            lines.append(f"{parent} --> {child}")
            lines.append(f"{child}[{key}]")
            recurse(value, child)
    root = prefix.replace('.', 'root')
    lines.append(f"{root}[{prefix}]")
    recurse(tree, root)
    return "graph TD\n    " + "\n    ".join(lines)

def to_d2(tree, prefix="."):
    lines = []
    def recurse(node, parent):
        for key, value in node.items():
            child = f"{parent}_{key}".replace('.', '').replace('-', '')
            lines.append(f'{parent} -> {child}')
            lines.append(f'{child}: "{key}"')
            recurse(value, child)
    root = prefix.replace('.', 'root')
    lines.append(f'{root}: "{prefix}"')
    recurse(tree, root)
    return "\n".join(lines)

def generate_diagram(tree, mode="d2", prefix="root"):
    if mode == "mermaid":
        return to_mermaid(tree, prefix=prefix)
    elif mode == "d2":
        return to_d2(tree, prefix=prefix)
    else:
        raise ValueError("Unsupported mode.")

def get_output_filename(input_txt, mode):
    output_ext = {
        "mermaid": ".mmd",
        "d2": ".d2"
    }
    return os.path.splitext(input_txt)[0] + output_ext[mode]

def save_output(diagram, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(diagram)
    print(f"File generated: {output_path}")

def run_tree2diagram(input_txt, mode="d2", prefix="root"):
    tree = parse_tree_txt(input_txt)
    diagram = generate_diagram(tree, mode=mode, prefix=prefix)
    output_file = get_output_filename(input_txt, mode)
    save_output(diagram, output_file)

