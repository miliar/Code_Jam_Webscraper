'''
Created on Apr 13, 2013

@author: nils
'''

import numpy as np

def solve(lawn):
    
    for dim in lawn.shape:
        if dim <= 1:
            return True
        
    minimum = lawn.min()
    
    min_row_index = []
    min_column_index = []
    
    for index, row in enumerate(lawn):
        if _are_all_equal(row, minimum):
            min_row_index.append(index)
            
    for index, column in enumerate(lawn.transpose()):
        if _are_all_equal(column, minimum):
            min_column_index.append(index)
            
    for row_index in range(lawn.shape[0]):
        for column_index in range(lawn.shape[1]):
            if minimum == lawn[row_index][column_index]:
                if row_index not in min_row_index and column_index not in min_column_index:
                    return False
                
    
        
    for row_index in min_row_index:
        new_lawn = np.delete(lawn, row_index, 0)
        if solve(new_lawn):
            return True

    for column_index in min_column_index:
        new_lawn = np.delete(lawn, column_index, 1)
        if solve(new_lawn):
            return True
                
            
    return False
        
def _are_all_equal(line, value):
    for elem in line:
        if elem != value:
            return False
    
    return True 
    