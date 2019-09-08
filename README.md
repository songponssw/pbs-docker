# PBSPro Docker Container

### Single Node
- Matrix data from [Matrix Multiplication Hadoop](https://github.com/shask9/Matrix-Multiplication-Hadoop)
- [Running PBSPro in docker](https://pbspro.atlassian.net/wiki/spaces/PBSPro/pages/79298561/Using+Docker+to+Instantiate+PBS)
```
## start docker
docker run --rm -it --name pbs -h pbs -e PBS_START_MOM=1 pbspro/pbspro bash

## setup worker node(localhost)
qmgr -c "create node pbs"
qmgr -c "set node pbs queue=workq"
```