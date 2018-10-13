'''
Created on May 7, 2011

@author: rob
'''

def main():
    input = open('/Users/rob/Downloads/B-large.in')
    T = int(input.readline())
    for i in range(T):
        combine = []
        opposed = []
        tokens = input.readline().split()
        C = int(tokens[0])
        for c in range(C):
            combine.append(tokens[1+c])
        
        D = int(tokens[1+C])
        for d in range(D):
            opposed.append(tokens[2+C+d])
            
        invoked = tokens[C+D+3]
        result = []
        for a in invoked:
            # Check for combination
            result.append(a)
            if len(result)>1:
                b = result[len(result)-2]
                
                madeRecipe = False
                for recipe in combine:
                    ingredients = recipe[:2]
                    if ingredients == a+b or ingredients == b+a:
                        del result[-2:]
                        result.append(recipe[2:])
                        madeRecipe = True
                        break
                
                if not madeRecipe:
                    for element in result[:-1]:
                        for opposition in opposed:
                            if opposition == a+element or opposition == element+a:
                                result = []
                                break
        
        output = 'Case #' + str(i+1) + ': ['
        for i in range(len(result)):
            output += result[i]
            if (i != len(result)-1):
                output += ', '
        
        output += ']'
        
        print(output)

if __name__ == '__main__':
    main();