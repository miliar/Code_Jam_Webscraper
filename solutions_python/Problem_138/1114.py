from copy import deepcopy

def play_war(n_blocks, k_blocks):
    
    for i in range(len(n_blocks)):        
        n_block = n_blocks[i]
        for j in range(len(k_blocks)):
            if k_blocks[j] > n_block:
                k_blocks.pop(j)
                break

    return len(k_blocks)
       
def deceitful_war(n_blocks, k_blocks):
    n_blocks = sorted(n_blocks)
    larger_blocks = 0

    for i in range(len(n_blocks)):
        n_block = n_blocks[i]
        for j in range(len(k_blocks)):
            if k_blocks[j] < n_block:
                k_blocks.pop(j)
                larger_blocks += 1
                break
        
    return larger_blocks



def main():
    _file = ""
    with open("D-large.in", "r") as inputfile:
        _file = inputfile.read()


    file_rows = _file.split("\n")
    batches = int(file_rows[0])
    file_rows = file_rows[1:]
    scores = []

    for batch in range(batches):
        batch_items = file_rows[batch*3:3+batch*3]
        n_blocks = batch_items[1].split()
        k_blocks = batch_items[2].split()

        n_blocks = [float(i) for i in n_blocks]
        k_blocks = [float(i) for i in k_blocks]
        k_blocks = sorted(k_blocks)
        
        n_score_war = play_war(deepcopy(n_blocks), deepcopy(k_blocks))
        n_score_decitful = deceitful_war(deepcopy(n_blocks), deepcopy(k_blocks))

        scores.append((n_score_decitful, n_score_war))

    with open("output.txt", "w+") as outputfile:
        for i in range(len(scores)):
            outputfile.write("Case #{0:}: {1:} {2:}\n".format(i+1, scores[i][0], scores[i][1]))
    
if __name__ == "__main__":
    main()



