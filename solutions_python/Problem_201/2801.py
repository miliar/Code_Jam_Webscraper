tc = int(input())

for c in range(tc):
    N, K = map(int, input().split())
    empties = [(0, N-1)]

    for k in range(K):

        empties.sort(key=lambda x: x[1]-x[0]+1, reverse=True)
        
        left_edge_idx = empties[0][0]
        right_edge_idx = empties[0][1]
        empty_rooms = right_edge_idx - left_edge_idx + 1
        center_idx = left_edge_idx + empty_rooms // 2

        if empty_rooms % 2 == 0:
            center_idx -= 1

        empty_left = center_idx - left_edge_idx
        empty_right = right_edge_idx - center_idx

        empties.remove(empties[0])
        
        if left_edge_idx <= center_idx - 1:
            empties.append((left_edge_idx,
                            center_idx - 1))
            
        if center_idx + 1 <= right_edge_idx:
            empties.append((center_idx + 1,
                            right_edge_idx))
        
        empty = (empty_left, empty_right)
        maxi = max(empty)
        mini = min(empty)
    print("Case #{0}: {1} {2}".format(c+1, maxi, mini))

