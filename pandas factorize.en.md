+++
title = "Factorize data values in Pandas"
date = 2022-03-14
draft = false
keywords = ["pandas factorize"]
description = "This tutorial explains how to factorize data using pandas."
tags = ["Pandas", "Factorize"]
author = "Preet Sanghavi"
inarticle = true

+++

In this tutorial we will learn to factorize in pandas. We will be using the `pandas.factorize()` function to perform the task. By recognizing different values, the `pandas.factorize()` method aids in obtaining the numeric representation of an array.

Firstly, we will import the pandas, numpy library along with other required libraries.

## Import Libraries

```python
import numpy as np
import pandas as pd
from pandas.api.types import CategoricalDtype
```

## Using `pandas.factorize()` function

Now we will pass a list containing the characters to the `factorize()` function which will return us the labels and the unique values. We will output the labels and unique values separately.

```python
labels, uniques = pd.factorize(['b', 'd', 'd', 'c', 'a', 'c', 'a', 'b'])
```

The above code will return us the list of numeric representation of characters and the unique values.

Let us see the output using the below code.

```python
print("Numeric Representation : \n", labels)
print("Unique Values : \n", uniques)
```

```python
Numeric Representation : 
 [0 1 1 2 3 2 3 0]
Unique Values :
 ['b' 'd' 'c' 'a']
```

We can also sort the alphabets using the below code.

```python
labels, uniques = pd.factorize(['b', 'd', 'd', 'c', 'a', 'c', 'a', 'b'], sort = True)
```

We will have the below output for the above amendment.

```python
Numeric Representation : 
 [1 3 3 2 0 2 0 1]
Unique Values :
 ['a' 'b' 'c' 'd']
```

We can also use categories to divide the data values into category and in this case the unique values will differ. For this purpose we will use `pd.Categorical()` function to divide our data values.

```python
a = pd.Categorical(['a', 'a', 'c'], categories =['a', 'b', 'c'])
  
label3, unique3 = pd.factorize(a)
```

Let us now see output of the above code.

```python
Numeric Representation :
 [0 0 1]
Unique Values :
 ['a', 'c']
Categories (3, object): ['a', 'b', 'c']
```

We can see in the above output that our unique values list contains only the unique values.

Therefore, using the following approaches we can factorize the data values using pandas.
