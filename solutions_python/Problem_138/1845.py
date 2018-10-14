
with open('file') as f:
   count = 0
   num_test_cases = int(f.readline())
   while num_test_cases > 0:
      num_blocks_of_wood = int(f.readline())
   
      naomis_blocks = [float(x) for x in f.readline().split()]
      kens_blocks = [float(x) for x in f.readline().split()]

      naomis_blocks.sort()
      kens_blocks.sort()

      cheated_winning = 0 

      legit_winning = 0
    
      length = len(naomis_blocks)-1
      i = length
      j = length
      cheated_winning_pos = i
#      print naomis_blocks, kens_blocks, i, cheated_winning_pos
      while i >= 0:
#         print naomis_blocks[i], kens_blocks[j], naomis_blocks[cheated_winning_pos], kens_blocks[i]
         if naomis_blocks[i] > kens_blocks[j]:
            legit_winning+=1
         else:
            j-=1
         if naomis_blocks[cheated_winning_pos] > kens_blocks[i]:
            cheated_winning+=1
            cheated_winning_pos-=1
         i-=1
      count += 1
      print("Case #" + str(count) + ": " + str(cheated_winning) + " " + str(legit_winning))   
      num_test_cases -= 1 
