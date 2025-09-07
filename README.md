[![PyPI version](https://badge.fury.io/py/setup_py_gen.svg)](https://badge.fury.io/py/setup_py_gen)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/setup_py_gen)](https://pepy.tech/project/setup_py_gen)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/chigwell/setup_py_gen)

# setup_py_gen

`setup_py_gen` is a Python package designed to generate a valid `setup.py` script suitable for PyPI packaging using an LLM. It leverages AI to craft precise and ready-to-use package setup scripts based on user input and metadata.

## Installation

Install the package via pip:

```bash
pip install setup_py_gen
```

## Usage

Here's a simple example demonstrating how to generate a `setup.py` script using a language model instance:

```python
from llmatch_messages import llmatch
from langchain_llm7 import ChatLLM7
from langchain_core.language_models import BaseChatModel
from setup_py_gen import generate_setup_py_from_llm

# Initialize your LLM instance (placeholder example)
llm = ChatLLM7()

# Custom description for your package
custom_text = "A sample Python package for demonstration purposes."

# Generate setup.py content
setup_code = generate_setup_py_from_llm(
    llm=llm,
    custom_text=custom_text,
    package_name="sample_package",
    author="Your Name",
    author_email="your.email@example.com",
    repo_url="https://github.com/yourusername/sample_package"
)

print(setup_code)
```

This will output a complete `setup.py` script tailored to your description and metadata.

## Author

 Eugene Evstafev <hi@eugene.plus>  
 Repository: [https://github.com/chigwell/setup_py_gen](https://github.com/chigwell/setup_py_gen)
