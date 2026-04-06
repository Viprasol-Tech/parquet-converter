# Parquet Converter

Convert data to and from Parquet format

## Features

- Zero external dependencies (stdlib only)
- Easy-to-use CLI interface
- Professional Python implementation
- MIT licensed

## Installation

```bash
pip install -e .
```

Or clone and install:

```bash
git clone https://github.com/Viprasol-Tech/parquet-converter
cd parquet-converter
pip install -e .
```

## Usage

### Python

```python
from parquet_converter import ParquetConverter

result = ParquetConverter.process("data")
print(result)
```

### CLI

```bash
python -m parquet_converter "your input here"
```

## Documentation

See the source code and docstrings for detailed API documentation.

## License

MIT License - see LICENSE file for details

## About

Part of Viprasol Utilities: https://viprasol.com

Created by Viprasol - Building AI-focused tools for developers.
