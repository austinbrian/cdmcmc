#!/bin/bash/env python
'''
d

Author: @austinbrian
'''
# Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pymc3 as pm




##########
# STEP 1
# Load in election and approval data
##########

# Need to find results by congressional district
# Need to add approval data


##########
# STEP 2 #
##########

# Calculate distributions of means for historical approval/result relationships


##########
# STEP 3 #
##########

### Need to update with data from priors

def model_pymc(std_prior_lower=100.0,std_prior_upper=1000.0):
    with pm.Model() as model:

        group_sa_mean = pm.Normal('SA_mean',prior_1.mean(),sd=prior_1.std())
        group_me_mean = pm.Normal('ME_mean',prior_2.mean(),sd=prior_2.std())

#     std_prior_lower = 100.0
#     std_prior_upper = 1000.0 # changed to more accurately reflect the standard deviations here

    with model:

        group_sa_std = pm.Uniform('SA_std',lower=std_prior_lower,upper=std_prior_upper)
        group_me_std = pm.Uniform('ME_std',lower=std_prior_lower,upper=std_prior_upper)

        group_sa = pm.Normal('SA_acts', mu=group_sa_mean, sd=group_sa_std, observed=sa_80s)
        group_me = pm.Normal('ME_acts', mu=group_me_mean, sd=group_me_std, observed=me_00s)

        diff_of_means = pm.Deterministic('difference of means', group_sa_mean - group_me_mean)
        diff_of_stds = pm.Deterministic('difference of stds', group_sa_std - group_me_std)
        effect_size = pm.Deterministic('effect size', diff_of_means / np.sqrt((group_sa_std**2 + group_me_std**2) / 2))

    with model:
        trace = pm.sample(25000, njobs=4)

    pm.plot_posterior(trace[3000:],
                 varnames = ['SA_mean','ME_mean','SA_std','ME_std'],
                 color = '#F4953B')

    pm.plot_posterior(trace[3000:],
                  varnames=['difference of means', 'difference of stds', 'effect size'],
                  ref_val=0,
                  color='#87ceeb')
    plt.show()
