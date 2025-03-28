# PU_BGC_diagram
Set of experiment setings and python scripts for plotting diagrams for PU_BGC [paper](https://mseduculiegebe-my.sharepoint.com/:f:/g/personal/mgregoire_uliege_be/Egk1DWz5_7JNlL6nQJqDZpkBJveCWEb-LGwqO3cVyeO6AQ?e=O9Ly7D) 

## Updates

- [02/28/2025] ```cmems_instac_loader.py``` and ```config_user.yaml``` added

## List of scripts

- ```cmems_instac_loader.py``` to download [Global Ocean - Delayed Mode Biogeochemical product](https://doi.org/10.17882/86207) with [Copernicus Marine Toolbox](https://help.marine.copernicus.eu/en/collections/9080063-copernicus-marine-toolbox)
- ```diagram_taylor.py``` to plot modified Taylor diagram (Note: under development)

## Usages

### plot sample Taylor diagram

```python
python diagram_taylor.py
```

### check usage of ```cmems_instac_loader.py```

```python
python cmems_instac_loader.py
```

NOTE: Rewrite ```config_user.yaml``` to register your Copernicus Marine credentials before using ```cmems_instac_loader.py```

## Experiment Setups

### Metrices for PU_BGC BIO_MY diagnosis with model ensemble 

- Period: 5 years (e.g., 2017-2021 for ARC MFC)
- Model:
   - MFC BIO MY with data assimilation (CMEMS product)
   - MFC BIO MY without data assimilation (control experiment)
- Model subdomains:
   - ARC MFC Norwegian Sea
   - ARC MFC Greenland Sea
   - ARC MFC Subpolar Gyre
   - other MFCs subdomains (e.g., MED WEST and MED EAST)
- Independent Observations (Reference):
   - CMEMS INSTAC [Global Ocean - Delayed Mode Biogeochemical product](https://doi.org/10.17882/86207)
       - BGC Argo float data (PF): Chlorophyll-a, BBP/POC, Oxygen, Nitrate
       - Bottle sampled in situ data (BO): Chlorophyll-a, Nitreate, Silicate, Phosphate, Oxygen 
- Variables [unit]: 
   - 0-100m Nitrate [mmol/m3]
   - 100-400m Nitrate [mmol/m3]
   - 0-100m Phosphate [mmol/m3]
   - 100-400m Phosphate [mmol/m3]
   - 0-100m Silicate [mmol/m3]
   - 100-400m Silicate [mmol/m3]
   - 0-100m Nitrate [mmol/m3]
   - 100-400m Nitrate [mmol/m3]
   - 0-100m Chlorophyll-a [mg/m3]
   - 100-400m Chlorophyll-a [mg/m3]
   - 0-100m POC [mg/m3]
   - 100-400m POC [mg/m3]
   - 0-100m Oxygen [mmol/m3]
   - 100-400m Oxygen [mmol/m3]

### Modified Taylor diagram (see [Taylor 2005](https://pcmdi.llnl.gov/staff/taylor/CV/Taylor_diagram_primer.pdf)) 

Sample modified Taylor diagram creatd by diagram_taylor.py. Data used in the sample plot are bogus. Input data are set of standard deviation, Pearson correlation in sample() specified by

```python
    stdref = 48.491 # reference (observation) standard deviation
    stats = [
        [25.939, 0.385, "ARC NWS"], 
        [29.593, 0.509, "ARC SPG"],
        [33.125, 0.585, "MED EAST"], 
        [35.807, 0.609, "MED WEST"]
    ]
    # [standard deviation, Pearson correlation, label]
```

Since it does not accept different source of data yet, the code will be modified soon so that data can be imported by YAML file of the form:

```python
datasets:
  - name: "ARC NRW"
    reference_stddev: 48.491
    stddev: 25.939
    correlation: 0.385

  - name: "ARC SPG"
    reference_stddev: 50.123
    stddev: 29.593
    correlation: 0.509

  - name: "MED WST"
    reference_stddev: 45.678
    stddev: 33.125
    correlation: 0.585

  - name: "MED EST"
    reference_stddev: 48.491
    stddev: 29.593
    correlation: 0.509
```

![Alt text](modified_taylor.png)
