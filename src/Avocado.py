import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg


"""
create csv reading method
"""
df = pandas.read_csv( "avocado.csv" )
print( df )

