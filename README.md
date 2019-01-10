# CraftBeerPI HTTP Sensor Plugin

This plugin is allows to push sensor data to CraftBeerPi4 via HTTP Endpont

## Installation 

```
  git clone https://github.com/Manuel83/cbpi-httpsensor
  cd cbpi-httpsensor
  pip install . 
```

Add `cbpi-httpsensor` to plugin_list.txt in the confing.yaml of CraftBeerPi

## Endpoint

The plugin exposes the follwoing HTTP GET Endpoint.

http://localhost:8080/httpsensor/{key}/{value}
