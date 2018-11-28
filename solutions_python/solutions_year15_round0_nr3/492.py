class QuaternionValue():
    def __init__(self, val, sign):
        self.val = val
        self.sign = sign

class DijkstraQuaternion():
    def __init__(self):
        self.q_map = {}
        self.add("1", "1", "1", True)
        self.add("1", "i", "i", True)
        self.add("1", "j", "j", True)
        self.add("1", "k", "k", True)

        self.add("i", "1", "i", True)
        self.add("i", "i", "1", False)
        self.add("i", "j", "k", True)
        self.add("i", "k", "j", False)
        
        self.add("j", "1", "j", True)
        self.add("j", "i", "k", False)
        self.add("j", "j", "1", False)
        self.add("j", "k", "i", True)

        self.add("k", "1", "k", True)
        self.add("k", "i", "j", True)
        self.add("k", "j", "i", False)
        self.add("k", "k", "1", False)

    def add(self, x,y, val, sign):
        if not x in self.q_map:
            self.q_map[x] = {}
        self.q_map[x][y] = QuaternionValue(val, sign)

    def get(self, x,y):
        return self.q_map[x][y]


quaternion_map = DijkstraQuaternion()
memorised_k = {}

#Start with sign=True and goal=['i','j','k']
def dijkstra(pattern, sign, goal):
    global memorised_k
    global quaternion_map
    if pattern in memorised_k:
        if not memorised_k[pattern] == False:
            return memorised_k[pattern].sign
        else:
            return False
        
    current = QuaternionValue("1", True)
    for x in range(0,len(pattern)):
        next_id = pattern[x]
        current = quaternion_map.get(current.val, next_id)
        sign = sign == current.sign
        if not goal[0] == 'k' and current.val == goal[0]:
            #print pattern[:x+1]
            return dijkstra(pattern[x+1:], sign, goal[1:])
        
    if goal[0] == 'k':
        if current.val == "k":
            memorised_k[pattern] = QuaternionValue(current.val, sign)
            return sign
        else:
            memorised_k[pattern]=False
    return False

def test_pattern(pattern):
    map_c = {}
    for char in pattern:
        map_c[char] = True
        if len(map_c)>1:
            return True
    return False

file_name = "C-small-attempt0"
file_handle = open(file_name + ".in")
output_file = open(file_name + ".out", 'w')

test_cases = int(file_handle.readline())

for i in range(0,test_cases):
    print i
    line_split = file_handle.readline().strip().split()
    l = int(line_split[0])
    x = int(line_split[1])
    base_pattern = file_handle.readline().strip()

    result = "NO"
    if test_pattern(base_pattern):
        pattern = base_pattern * x
        if dijkstra(pattern,True,['i','j','k']):
            result = "YES"
        
    output_file.write("Case #{0}: {1}\n".format(str(i+1), result))
    

file_handle.close()
output_file.close()
