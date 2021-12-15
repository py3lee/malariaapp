# Dash app on 3 malaria datasets

This repository contains the python scripts used to create the Dash app to visualize the number of malaria deaths over time using aggregated malaria data.  

Link to Dash app: https://malariadatasets.herokuapp.com

# Dataset

Data Source: https://github.com/rfordatascience/tidytuesday/tree/master/data/2018/2018-11-13

3 Datasets:

- malaria_inc.csv - Malaria incidence by country for all ages across the world across time
- malaria_deaths.csv - Malaria deaths by country for all ages across the world and time.
- malaria_deaths_age.csv - Malaria deaths by age across the world and time.

## Dataset prepreocessing to visualization

The app uses a preprocessed dataset. Details on the exact preprocessing steps can be found in this [data pipeline script](https://github.com/py3lee/projects/blob/main/malaria/src/main.py). The justfications for the preprocessing steps can be found in this [jupyter notebook](https://github.com/py3lee/projects/blob/main/malaria/analysis/Python_1_EDA_malaria.ipynb). 

See the [related repository](https://github.com/py3lee/projects/tree/main/malaria) for further information.