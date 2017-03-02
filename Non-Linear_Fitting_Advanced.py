# Objective
# Test the effect of the following variables on the performance
# of non-linear least-square curve fitting:
# 1. Initial Guess
# 2. Noise
# 2. Algorithm used

# Assumption: we are studing a function of the form  Y = a *exp(-x/b)

# modules 
import numpy as np
import matplotlib.pyplot as plt
from   scipy import optimize 

# Exponential decay function
exp_decay = lambda pars, xdata: pars[0] * np.exp(-xdata/pars[1])

# Simulae Data
xdata = np.linspace(0,.1,20);      p_used = [2,.1]
ydata = exp_decay(p_used,xdata)

# Plot data
plt.plot(xdata,ydata)

# Residual function
res_func = lambda pars, exp_data: exp_decay(pars,xdata) - exp_data

# CASE 1. Initial Guess
x0 = [1, 1]

# estimate parameters in exp_decay 
OptimizeResult  = optimize.least_squares(res_func,  x0, args   = (ydata ))



def residuals(parameters,x_data,y_observed,func):
    '''
    Compute residuals of y_predicted - y_observed
    where:
    y_predicted = func(parameters,x_data)
    '''
    return func(parameters,x_data) - y_observed

# 3. Perform curve fitting
#    Initial guess for the parameters to be estimated
#    The parameters follow the same order than exp_decay
x0 = [1, 1]

#    Lower and uppers bounds
lb = [0,0]
ub = [2,2]

# estimate parameters in exp_decay 
OptimizeResult  = optimize.least_squares(residuals,  x0, bounds = (0,2),
                                          args   = ( xdata, y_data_with_noise,exp_decay) )
parameters_estimated = OptimizeResult.x

# Estimate data based on the solution found
y_data_predicted = exp_decay(parameters_estimated,xdata)

# Plot all together
plt.figure(2)
plt.plot(xdata,y_data_with_noise,'ob',
         xdata,y_data           ,'--k',
         xdata,y_data_predicted ,'xr')
plt.legend(('Data With noise','Real Data','Predicted Data'))

# How good are the parameters I estimated?
print( 'Predicted: ' + str( parameters_estimated))
print( 'Expected : ' + str( parameters_used))

