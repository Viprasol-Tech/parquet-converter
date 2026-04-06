"""
parquet-converter - Convert data to and from Parquet format

Part of Viprasol Utilities: https://viprasol.com
"""

__version__ = "0.1.0"
__author__ = "Viprasol"
__email__ = "hello@viprasol.com"

from .core import ParquetConverter, convert, process, main

__all__ = ["ParquetConverter", "convert", "process", "main"]
