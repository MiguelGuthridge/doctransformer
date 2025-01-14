"""
# Transdoc / Handlers / API

API definition for Transdoc handler modules.
"""
from typing import Protocol
from pathlib import Path
from transdoc.__transformer import TransdocTransformer


class TransdocHandler(Protocol):
    """
    A language handler plugin for transdoc.
    """

    def get_file_extensions(self) -> list[str]:
        """
        Returns the list of file extensions that this handler supports.

        This should be a list of strings, where each string is a file
        extension, excluding the leading dot.

        Returns:
            list[str]: supported file extensions (eg `['txt', 'md'])
        """
        ...

    def transform_file(
        self,
        transformer: TransdocTransformer,
        in_path: Path,
        out_path: Path,
    ) -> None:
        """
        Transforms the contents of the file at `in_path`, writing the
        transformed output into the file at `out_path`.

        Args:
            transformer (TransdocTransformer): use `transformer.apply` on any
            rule calls.
            in_path (Path): path to input file
            out_path (Path): path to output file
        """
        ...
