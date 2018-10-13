cases = int(input())
for case in range(1,cases+1):
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
#     maximum = 0
#     minimum = 0
#     if n>k:
#         rooms = [n]
#         for c in range(k):
#             m = max(rooms)
#             if m == 1:
#                 left = 0
#                 right = 0
#                 break
#             idx = rooms.index(m)
#             left = int((m-1)/2) if m%2==1 else int((m-1)/2)
#             right = int((m-1)/2) if m%2==1 else int((m-1)/2)+1
#             rooms = rooms[:idx] + [left,right] + rooms[idx+1:]
#               
#         maximum = max(left,right)
#         minimum = min(left,right)
  
    level = len('{0:b}'.format(k))
    previous_level =  '1' * (level-1)
    if previous_level == '':
        gap = k
    else:
        gap = k - int(previous_level,2)
    current_level = 2**level
    maximum = int(n/current_level-(gap-1)/current_level)
    minimum = int(n/current_level-(gap-1)/current_level-1/2)
    
    print('Case #{}: {} {}'.format(case, maximum, minimum))
