class decision_node(object):
    def __init__(self, weight, feature='', left=None, right=None, parent=None):
        self.weight = weight
        self.feature = feature
        self.left = left
        self.right = right
        self.parent = parent

def main(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    out_lines = []
    
    N = int(lines.pop(0))
    
    for case in xrange(N):
        L = int(lines.pop(0))
        node = None
        tree_line = ''
        for i in xrange(L):
            line = str(lines.pop(0)).strip()
            tree_line = ' '.join([tree_line, line])
        tree_line = tree_line[1:].replace('( ', '(').replace(' )', ')')
        
        
        def parse_tree(node_text):
            new_node_text = node_text[1:-1].strip()
            attribs = new_node_text.split(' ', 2)
            
            weight = float(attribs.pop(0))
            if len(attribs) > 0:
                feature = str(attribs.pop(0))
                new_tree_text = str(attribs.pop(0)).strip()
                
                left_index = 0
                right_index = -1
                parens_to_match = 0
                for i, char in enumerate(new_tree_text):
                    if char == '(':
                        parens_to_match += 1
                    elif char == ')':
                        parens_to_match -= 1
                    
                    if parens_to_match == 0:
                        left_index = i+1
                        right_index = i+2
                        break
                
                left = parse_tree(new_tree_text[:left_index])
                right = parse_tree(new_tree_text[right_index:])
                node = decision_node(weight, feature=feature, left=left, right=right)
            else:
                node = decision_node(weight)
            
            return node
        
        root_node = parse_tree(tree_line)
        
        line = 'Case #%i: \n' %((case + 1))
        sub_lines = ''
        A = int(lines.pop(0))
        for i in xrange(A):
            animal_attribs = lines.pop(0).split(' ')
            animal = animal_attribs.pop(0)
            n = animal_attribs.pop(0)
            features = []
            while len(animal_attribs) > 0:
                features.append(animal_attribs.pop(0).replace('\n', ''))
            
            p = 1.0
            node = root_node
            while True:
                p *= node.weight
                if node.left is None and node.right is None:
                    break
                else:
                    if node.feature in features:
                        node = node.left
                    else:
                        node = node.right
            
            sub_lines += '%0.7f\n' %(p)
        
        line += sub_lines
        print line
        out_lines.append(line)
    
    f = open('A.out', 'w')
    f.writelines(out_lines)
    f.close()
    

if __name__ == '__main__':
    main('A-large.in')