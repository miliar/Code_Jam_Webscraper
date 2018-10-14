with open('sample.in','rb') as f, open('solution.txt','wb') as o:
  number_of_test_cases = int(f.readline())
  for case in xrange(0,number_of_test_cases):
    number_of_blocks = int(f.readline())
    N_blocks = sorted([float(x) for x in f.readline().split(' ')],reverse=True)
    K_blocks = sorted([float(x) for x in f.readline().split(' ')],reverse=True)
    N_blocks_decit = list(N_blocks)
    K_blocks_decit = list(K_blocks)
    N_points_decit = 0
    N_points = 0
  
    ############################################################################
    ## Deceitful War
    ############################################################################
    for i in xrange(0,number_of_blocks):

      if N_blocks_decit[0] > K_blocks_decit[0]:
        N_blocks_decit.pop(0)
        K_blocks_decit.pop(0)
        N_points_decit+=1
      elif len(N_blocks_decit) > 1:
        N_blocks_decit.pop(-1) 
        K_blocks_decit.pop(0) 
    
    
    ############################################################################
    ## War
    ############################################################################
    for i in xrange(0,number_of_blocks):
      N_weight = N_blocks[-1]
      if K_blocks[-1] > N_weight:
        N_blocks.pop(len(N_blocks)-1)
        K_blocks.pop(len(K_blocks)-1)
      elif K_blocks[0] < N_weight:
        N_points+=1
        N_blocks.pop(len(N_blocks)-1)
        K_blocks.pop(len(K_blocks)-1)
      else:
        K_weight = min(x for x in K_blocks if x > N_weight)
        K_blocks.pop(K_blocks.index(K_weight))
        N_blocks.pop(len(N_blocks)-1)
    o.write('Case #%i: %i %i\n'%(case+1,N_points_decit,N_points))
