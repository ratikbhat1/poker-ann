## A Sample file to show how to load and use the ann 

from pybrain.tools.shortcuts import buildNetwork
import pickle

annfile = open('path-to-ann-dump/pokerann','r') #after you run the ann file a pickle dump of the ann by the name of pokerann will be created which is being loaded here

ann = pickle.load(annfile)

print(ann.activate([1,1,1,13,2,4,2,3,1,12]))
