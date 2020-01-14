"""NUI Galway CT5132/CT5148 Programming and Tools for AI (James McDermott)

Skeleton/solution for Assignment 1: Numerical Integration

By writing my name below and submitting this file, I/we declare that
all additions to the provided skeleton file are my/our own work, and that
I/we have not seen any work on this assignment by another student/group.

Student name(s):
Student ID(s):

"""

import numpy as np
import sympy
import itertools
import math

def numint_py(f, a, b, n):
    """Numerical integration. For a function f, calculate the definite
    integral of f from a to b by approximating with n "slices" and the
    "lb" scheme. This function must use pure Python, no Numpy.

    >>> abs(numint_py(math.sin, 0, 2*math.pi, 100) - 0) < 10**-8
    True
    >>> round(numint_py(lambda x: 1, 0, 1, 100), 5)
    1.0
    >>> round(numint_py(math.exp, 1, 2, 100), 5)
    4.64746

    """
    A = 0
    w = (b - a) / n # width of one slice
    # STUDENTS ADD CODE FROM HERE TO END OF FUNCTION
    for i in range(n):
        xi = a + w * i
        A += w * f(xi)
    return A

def numint(f, a, b, n, scheme='mp'):
    """Numerical integration. For a function f, calculate the definite
    integral of f from a to b by approximating with n "slices" and the
    given scheme. This function should use Numpy, and eg np.linspace()
    will be useful.
    
    >>> abs(numint(np.sin, 0, 2*math.pi, 100) - 0) < 10**-8
    True
    >>> round(numint(lambda x: np.ones_like(x), 0, 1, 100), 5)
    1.0
    >>> round(numint(np.exp, 1, 2, 100, 'lb'), 5)
    4.64746
    >>> round(numint(np.exp, 1, 2, 100, 'mp'), 5)
    4.67075
    >>> round(numint(np.exp, 1, 2, 100, 'ub'), 5)
    4.69417

    """
    # STUDENTS ADD CODE FROM HERE TO END OF FUNCTION
    x = np.linspace(a, b, n, endpoint=False)
    w = (b - a) / n # width of one slice
    if scheme == 'lb':
        pass # we already have the lb values
    elif scheme == 'mp':
        x += w / 2
    elif scheme == 'ub':
        x += w
    fx = f(x) # all f(x) values
    A = w * np.sum(fx)
    return A

def true_integral(fstr, a, b):
    """Using Sympy, calculate the definite integral of f from a to b and
    return as a float. Here fstr is an expression in x, as a str. It
    should use eg "np.sin" for the sin function.

    This function is quite tricky, so you are not expected to
    understand it or change it! However, you should understand how to
    use it. See the doctest example.

    >>> true_integral("np.sin(x)", 0, 2 * np.pi)
    0.0
    >>> true_integral("x**2", 0, 1)
    0.3333333333333333
    """
    x = sympy.symbols("x")
    # make fsym, a Sympy expression in x, now using eg "sympy.sin"
    fsym = eval(fstr.replace("np", "sympy")) 
    A = sympy.integrate(fsym, (x, a, b)) # definite integral
    A = float(A.evalf()) # convert to float
    return A

def numint_err(fstr, a, b, n, scheme):
    """For a given function fstr and bounds a, b, evaluate the error
    achieved by numerical integration on n points with the given
    scheme. Return the true value, absolute error, and relative error
    as a tuple.

    Notice that the relative error will be infinity when the true
    value is zero. None of the examples in our assignment will have a
    true value of zero.

    >>> print("%.4f %.4f %.4f" % numint_err("x**2", 0, 1, 10, 'lb'))
    0.3333 0.0483 0.1450
    """
    f = eval("lambda x: " + fstr) # f is a Python function
    A = true_integral(fstr, a, b)
    # STUDENTS ADD CODE FROM HERE TO END OF FUNCTION
    A_est = numint(f, a, b, n, scheme)
    abs_err = abs(A - A_est)
    rel_err = abs((A - A_est) / A)
    return A, abs_err, rel_err

def make_table(f_ab_s, ns, schemes):
    """For each function f with associated bounds (a, b), and each value
    of n and each scheme, calculate the absolute and relative error of
    numerical integration and print out one line of a table. This
    function doesn't need to return anything, just print. Each
    function and bounds will be a tuple (f, a, b), so the argument
    f_ab_s is a list of tuples.

    Hint: use print() with the format string
    "%s,%.2f,%.2f,%d,%s,%.4g,%.4g,%.4g". Hint 2: consider itertools.

    >>> make_table([("x**2", 0, 1), ("np.sin(x)", 0, 1)], [10, 100], ['lb', 'mp'])
    x**2,0.00,1.00,10,lb,0.3333,0.04833,0.145
    x**2,0.00,1.00,10,mp,0.3333,0.0008333,0.0025
    x**2,0.00,1.00,100,lb,0.3333,0.004983,0.01495
    x**2,0.00,1.00,100,mp,0.3333,8.333e-06,2.5e-05
    np.sin(x),0.00,1.00,10,lb,0.4597,0.04246,0.09236
    np.sin(x),0.00,1.00,10,mp,0.4597,0.0001916,0.0004168
    np.sin(x),0.00,1.00,100,lb,0.4597,0.004211,0.009161
    np.sin(x),0.00,1.00,100,mp,0.4597,1.915e-06,4.167e-06
    
    """
   
    # STUDENTS ADD CODE FROM HERE TO END OF FUNCTION
    for (f, a, b), n, scheme in itertools.product(f_ab_s, ns, schemes):
        true_int, abs_err, rel_err = numint_err(f, a, b, n, scheme)
        print("%s,%.2f,%.2f,%d,%s,%.4g,%.4g,%.4g" %
              (f, a, b, n, scheme, true_int, abs_err, rel_err))

def main():
    """Call make_table() as specified in the pdf."""
    # STUDENTS ADD CODE FROM HERE TO END OF FUNCTION
    f_ab_s = [
        ("np.cos(x)", 0, 0.5*math.pi),
        ("np.sin(2*x)", 0, 1),
        ("np.exp(x)", 0, 1)
        ]
    ns = [10, 100, 1000]
    schemes = ["lb", "mp"]
    make_table(f_ab_s, ns, schemes)

"""

We observe that the 'mp' scheme is much better than 'lb'. The relative
error is smaller by 2 or more orders of magnitude, depending on the
integral and the value of n.

Increasing the value of n improves performance. For 'lb', increasing n
by a factor of 10 gives a factor of 10 decrease in relative error. For
'mp', it gives a factor of 100.

The relative error with the 'mp' scheme with n=10 is comparable to the
'lb' scheme with n=1000.

"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()

