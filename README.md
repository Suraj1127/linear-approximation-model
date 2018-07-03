# linear-approximation-model
Linear model approximating non-linear functions using first order derivative.

## Description:

Not all functions are linear.  There are many non-linear functions which can't be modeled by a single straight line.
However, locally, all the non-linear functions can be modeled by the linear functions.  So, a bunch of linear functions
can model the non-linear function.  The approximation is given by the derivative equation.

y = m(x - x_1) + y_1 

where, (x, y) is the neighborhood point to (x_1, y_1).

## Requirements:
Python libraries
  - Numpy
  - Matplotlib
  
## Instructions:
- Run python module 'linear_approximation_model.py' and then enter the functions in numpy format and the range as well as interval.  The original function graph and approximated model's graph would be shown in the screen.
  ```
  python3 linear_approximation_model.py
  ```
