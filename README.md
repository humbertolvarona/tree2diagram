# tree2diagram

Converts directory tree text files into Mermaid or D2 graph diagrams

## Overview

`tree2diagram` is a Python utility that parses a text-based tree structure (using characters like ├── and └──) and generates a diagram in either [Mermaid](https://mermaid-js.github.io/) or [D2](https://d2lang.com/) syntax. It is designed to automate the conversion of simple text trees into graph diagrams for documentation, visualization, or presentation purposes.

---

## Features

* Parses tree-like text files and creates a nested Python dictionary.
* Generates graph diagrams in two supported formats:

  * Mermaid (graph TD)
  * D2 (text-based diagram language)
* Fully automated: input the filename and choose the output mode.
* Clean, modular code with clearly separated responsibilities.

---

## Input Format and How to Generate the Input File

The input text file should represent a tree using indentation and characters like:

```
root
├── child1
│   ├── grandchild1
│   └── grandchild2
└── child2
    └── grandchild3
```

No blank lines should be present, and indentation must be consistent.

### Generating the Input File Using the `tree` Command

You can automatically generate the required input file (e.g., `data.txt`) with the following bash command:

```sh
tree -d > data.txt
```

This command outputs the directory tree of the current directory (and subdirectories) to `data.txt` in the correct format.

#### Installing the `tree` Utility

* **Debian/Ubuntu:**

  ```sh
  sudo apt install tree
  ```
* **Fedora:**

  ```sh
  sudo dnf install tree
  ```
* **Arch Linux/Manjaro:**

  ```sh
  sudo pacman -S tree
  ```
* **openSUSE:**

  ```sh
  sudo zypper install tree
  ```
* **Alpine Linux:**

  ```sh
  sudo apk add tree
  ```

Refer to your distribution’s documentation if you use another Linux variant.

---

## Usage

### Quick Start

1. Place your tree text in a file (e.g., `data.txt`). You can generate this with `tree -d > data.txt` as explained above.
2. Run the script:

   ```python
   run_tree2diagram("data.txt", mode="d2", prefix="root")
   run_tree2diagram("data.txt", mode="mermaid", prefix="root")
   ```
3. By default, it will parse `data.txt` and output `data.d2` (D2 format) or `data.mmd` (Mermaid format).

---

## Function Reference

* **`parse_tree_txt(file_path)`**
  Reads a tree-formatted text file and returns a nested dictionary representing the tree.

* **`to_mermaid(tree, prefix=".", level=0)`**
  Converts a tree dictionary into a Mermaid flowchart (graph TD) format string.

* **`to_d2(tree, prefix=".", level=0)`**
  Converts a tree dictionary into D2 format string.

* **`generate_diagram(tree, mode="d2", prefix="root")`**
  Chooses the appropriate export format based on `mode` (`d2` or `mermaid`).

* **`get_output_filename(input_txt, mode)`**
  Returns the output filename with the correct extension (`.d2` or `.mmd`).

* **`save_output(diagram, output_path)`**
  Saves the generated diagram to a file.

* **`run_tree2diagram(input_txt, mode="d2", prefix="root")`**
  Orchestrates the process: parsing, diagram generation, and saving.

---

## Example

Given an input file `data.txt`:

```
root
├── A
│   ├── A1
│   └── A2
└── B
    └── B1
```

If run with D2 mode, it produces `data.d2`:

```
root: "root"
root_A: "A"
root -> root_A
root_A_A1: "A1"
root_A -> root_A_A1
root_A_A2: "A2"
root_A -> root_A_A2
root_B: "B"
root -> root_B
root_B_B1: "B1"
root_B -> root_B_B1
```

---

## Customization

* To change the input file, use the `input_txt` argument of `run_tree2diagram()`.
* To generate Mermaid format, set `mode="mermaid"` in `run_tree2diagram()`.
* The prefix can be changed to any root node label as needed.

---

## Requirements

* Python 3.6+
* No external dependencies.

---

## License (MIT)

Copyright (c) 2024 HL Varona ([humberto.varona@gmail.com](mailto:humberto.varona@gmail.com))

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
