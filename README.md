# OBNetwork
OBNetwork is a library created for the generation of Bayesian Network structures. These are dictionary-based composites, which generate dependency sublayers.

## Installation
Run the following to install:
```console
$ pip install BNetwork == 0.4
```

## Usage

A library must be imported, then initialize our Bayesian network.
```python
import OBNetwork

BayesianNetwork = BNetwork()
```

An adjacency matrix must be generated from which we will generate our relations
```python
matrix = [
    #A B C D E
    [0,1,1,0,0],    #A                  [A]
    [0,0,0,1,1],    #B                 /   \
    [0,0,0,0,1],    #C              [B]     [C]
    [0,0,0,0,0],    #D             /   \
    [0,0,0,0,0]     #E          [D]     [E]
]
```

Within the library we can generate our matrix, from which we can see that it is returned as a dictionary. To create a new bayesian network use the method createBNetwork(matrix)
```python
BayesianNetwork.createBNetwork(matrix)
print(BayesianNetwork)
```

To insert a new probability into our BayesianNetwork, use the method inserProbability()
```python
BayesianNetwork.insertProbability('A',0.24)     #A
BayesianNetwork.insertProbability('B|A',0.15)   #B
BayesianNetwork.insertProbability('B|-A',0.19)
BayesianNetwork.insertProbability('C|A',0.24)   #C
BayesianNetwork.insertProbability('C|-A',0.31)
BayesianNetwork.insertProbability('D|B',0.12)   #D
BayesianNetwork.insertProbability('D|-B',0.25)
BayesianNetwork.insertProbability('E|BC',0.12)  #E
BayesianNetwork.insertProbability('E|B-C',0.08)
BayesianNetwork.insertProbability('E|-BC',0.31)
BayesianNetwork.insertProbability('E|-B-C',0.14)
```

To verify if a probability is required, use the method descriptionCheck()
```python
print(BayesianNetwork.descriptionCheck())
```

And if you want to see the bayesian network compact representation, just use showCompactRepresentation()
```python
print(BayesianNetwork.showCompactRepresentation())
```