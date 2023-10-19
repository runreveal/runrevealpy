# RunReveal
Great with a jupyter notebook

# Installing
```
pip3 install runreveal
```
# Using
```
from runreveal import RunReveal
rr = RunReveal("show me my cloudflare audit logs from the past month where srcIP is not empty string", True).create_dataframe()
rr.head(5)
```
# Requirements
Your workspace ID and a RunReveal API token must be set on the environment.

```
export RUNREVEAL_WORKSPACE="sdfsdfsdfsdf"
export RUNREVEAL_AUTH_TOKEN="sdfsdfsdfsdfsdf"
```

# Dependencies
This package relies on `requests` and `pandas`.
