logging.basicConfig (
    level = logging.INFO,
    format= "[%(asctime)s: %(levelname)s]: %(message)s"

)

while True:
    project_name = input("Enter Project Name: ")
    if project_name != '':
        break

logging.info(f"Creating Project by name: {project_name}")

# List of Files
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini"
]



for file in list_of_files:
    filepath = Path(file)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"Creating a directory at:  {filedir} for files: {filename}")
    if (not os.path.exits(filepath)) or (os.path.getsize(filepath)==0):
        with open (filepath, "w") as f:
            pass
            logging.info(f"Creating a new file: {filename} at path: {filepath}")
    else:
        logging.info(f"file is already present at: {filepath}")