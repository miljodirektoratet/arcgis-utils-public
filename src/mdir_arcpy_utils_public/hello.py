"""Test entrypoint for mdir-arcpy-utils-public."""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version


def main() -> None:
    """
    Display welcome message and package version information.

    :return: None.
    """
    try:
        package_version = version("mdir-arcpy-utils-public")
    except PackageNotFoundError:
        package_version = "0.0.1"

    print("Hello from mdir-arcpy-utils-public!")
    print(f"Version: {package_version}")


if __name__ == "__main__":
    main()
