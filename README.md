# learning-python

## Set up

Assuming you have Python installed on your system, otherwise first install Python 3.8+ for best results.

### Create a Python virtual environment

On *nix systems:

```shell
python3 -m venv .env
```

On Windows systems:

```shell
py -m venv .env
```

### Switch into Python virtual environment

On *nix systems:

```shell
source .env/bin/activate
```

On Windows systems:

```shell
.env\Scripts\activate.bat
```

### Install/Upgrade modules necessary for managing and installing other modules

```shell
python -m pip install --upgrade pip wheel setuptools
```

### Install dependencies

```shell
python -m pip install -r requirements.txt
```

---

## Working with existing project 

### Ensure you have activated Python virtual environment

Your shell should indicate the active Python virtual environment within parentheses.  For example, notice the `(.env)` below:

```shell
C:\code\smu\learning-python(dev)
(.env) λ
```

### If not already activated, switch into Python virtual environment

On *nix systems:

```shell
source .env/bin/activate
```

On Windows systems:

```shell
.env\Scripts\activate.bat
```

### Start Jupyter Lab

```shell
jupyter-lab
```

Open browser to URL indicated by `jupyter-lab` to start using notebooks for development.

---

## Shutting down

### Stop Jupyter Lab

Within your terminal, press `Ctrl-C` to stop `jupyter-lab`

### Deactivate Python virtual environment

```shell
deactivate
```