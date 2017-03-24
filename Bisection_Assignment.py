# -*- coding: utf-8 -*-
tol = 0.00009  #tolerance for checking root
def function(x):
    return(x * x - 5 * x - 7)
a = 7   #range start value
b = 4   #range end value
iterations = 0
while  (iterations < 1000):
    iterations += 1
    c = (a + b) / 2
    ans = function(c)
    if (abs(ans)) < 0.009:
        print("root is",c )
        break;
    elif ans > 0:
        a = c
    else:
        b = c
if iterations == 1000:
    print("No root between range")


    
    

