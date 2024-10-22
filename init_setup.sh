echo [$(date)] : "START"
echo [$(date)] : "Creating conda env with python 3.12.6"
conda create -- prefix.env/ python = 3.12.6 -y
echo [$(date)] : "active env"
source activate ./env
echo [$(date)] : "installing dev requirements"
pip install -r requirements_dev.txt
echo [$(date)] : "END"

