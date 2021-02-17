# Plotting focal mechanism solutions for depth vs (latitudes/longitudes)
```
-Utpal Kumar
17 Feb 2021
```
## Requirements:
- Python 3.8.5 or above

## Installation

### Make python environment
```
python -m venv venv
```

### Activate environment (Mac/Linux)
```
source venv/bin/activate
```
### Activate environment (Windows)
```
venv\Scripts\activate
```

### Install required packages
```
pip install pandas pygmt
```

## Data file format:
![data format](docs/data_format.png "Data Format")

## Run program
```
python plot_depth.py
```

![Depth vs Longitudes](docs/depth-long-plot.png "Depth vs Longitudes")

![Depth vs Latiudes](docs/depth-lat-plot.png "Depth vs Latiudes")