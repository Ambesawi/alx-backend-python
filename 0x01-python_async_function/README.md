# Asynchronous Python (asyncio) Project

## Learning Objectives

This project focuses on asynchronous programming in Python using the asyncio library. By the end of this project, you will be able to:

1. Understand and use the `async` and `await` syntax in Python for asynchronous operations.
2. Execute an async program with asyncio.
3. Run concurrent coroutines to improve program efficiency.
4. Create asyncio tasks to manage asynchronous operations effectively.
5. Utilize the Python `random` module within asynchronous code.

## Requirements

### General

- **Python Version**: Python 3.7
- **Operating System**: Ubuntu 18.04 LTS

### Code Style and Documentation

- All code files follow the `pycodestyle` (version 2.5.x) coding style guide.
- Code files have a newline at the end.
- The first line of code files starts with `#!/usr/bin/env python3`.
- Functions and coroutines are appropriately type-annotated.
- Modules have documentation using `python3 -c 'print(__import__("my_module").__doc__)'`.
- Functions have documentation using `python3 -c 'print(__import__("my_module").my_function.__doc__)'`. The documentation consists of clear and meaningful sentences describing the purpose of the function.

### Project Structure
project-root/
│
├── your_code_file.py
├── another_code_file.py
│
└── README.md

### Usage

Include instructions on how to run and use your code here.

### Example

Provide an example or code snippet demonstrating the usage of your async code and asyncio tasks.

```python
import asyncio

async def main():
    # Your async code here
    pass

if __name__ == "__main__":
    asyncio.run(main())

