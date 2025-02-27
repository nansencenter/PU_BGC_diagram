# PU_BGC_diagram
Set of python scripts for plotting diagrams for PU_BGC paper

### Metrices

Period: 5 years (e.g., 2018-2022 for ARC MFC)

### Modified Taylor diagram

Sample diagram creatd by diagram_taylor.py. Input data are set of standarddeviation, Pearson correlation,

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

![Alt text](modified_taylor.png)
