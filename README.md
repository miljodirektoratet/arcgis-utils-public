# mdir-arcpy-utils-public

Python utility package for ArcGIS Pro 3.5 and AGOL/ESRI-related tasks at the Norwegian Environment Agency (miljødirektoratet).

**Table of Contents**

- [Guidelines](#guidelines)
- [Package Installation](#package-installation)
- [Module Installation](#module-installation)
- [Development](#development)

## Guidelines

- **ArcGIS Python**: python utilities intended for ArcGIS Pro 3.5 runtime or ArcGIS Online.
- **Module layout**: keep reusable modules inside `src/mdir_arcpy_utils_public` so they can be used both as package imports and as direct module files (for example from AGOL workflows).
- **Public code**: public-safe helper code only, sensitive code actual admin-tasks or infrastructure code is stored internally.
- **Security practices**:
  - Never commit passwords, tokens, or other sensitive data. Use key vaults for secret management.
  - Secret scanning, CodeQL, and Dependabot are enabled.

### Repository Structure

| File or Directory           | Purpose                                          |
| --------------------------- | ------------------------------------------------ |
| src/mdir_arcpy_utils_public | Python package source                            |
| notebooks                   | Usage examples and workflow demos                |
| environment.yml             | Conda environment definition                     |
| pyproject.toml              | Python packaging metadata and Pixi configuration |

## Package Installation

```powershell
# main branch (fast iteration)
pip install "git+https://github.com/miljodirektoratet/arcpy-utils-public.git@main"

# tag (release workflow)
pip install "git+https://github.com/miljodirektoratet/arcpy-utils-public.git@v0.0.1"

# commit (strict reproducibility)
pip install "git+https://github.com/miljodirektoratet/arcpy-utils-public.git@cff3f70b85822c82204c0e66876c240fbebeb563"
```

## Module Installation

In AGOL we recommend loading a single module file instead of installing the full package to reduce credits usage. The [demo_agol.ipynb](./notebooks/demo_agol.ipynb) notebook shows how to do this using the `load_github_module` function. You can pin to a version tag or a commit hash, or use `main` for quick development.

## Development

Choose one local environment manager.

### Option A: Conda

```powershell
conda env create -f environment.yml
conda activate mdir-arcpy-utils-public

# Local development package
pip install -e .
```

### Option B: Pixi

```powershell
pixi install
pixi shell
pixi run install-editable
```
