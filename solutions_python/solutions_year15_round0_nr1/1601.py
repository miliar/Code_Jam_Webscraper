from itertools import accumulate

import numpy as np

with open('A-large.in') as f:
    cases = int(f.readline())
    
    for i in range(cases):
        ringers = 0
        
        max_shyness, audience = f.readline().split()
        audience = [int(shyness) for shyness in audience]
        
        cumulative = np.array(list(accumulate(audience)))
        threshold = np.arange(int(max_shyness) + 1)

        diff = threshold - cumulative
        
        if np.max(diff) >= 0:
            ringers = np.max(diff) + 1
            
        print("Case #{0}: {1}".format(i + 1, ringers))