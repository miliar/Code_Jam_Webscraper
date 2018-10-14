from sys import stdin,stdout

def main():
    t = int(stdin.readline())
    for i in range(t):
        seconds = 0
        position = {"O" : 1, "B": 1}
        other_player = {"O" : "B", "B" : "O"}
        line = stdin.readline().strip()
        lineproc = line.split()
        n = int(lineproc[0])
        tasks = []
        for x in range(1,2*n, 2):
            vector = []
            vector.append(lineproc[x])
            vector.append(int(lineproc[x+1]))
            tasks.append(vector)
        ## move position
        current = 0
        while(current < len(tasks)):
            ##check first task
            current_player = tasks[current][0]
            to_go = tasks[current][1]
            ## check this player
            if to_go > position[current_player]:
                position[current_player] += 1
            elif to_go < position[current_player]:
                position[current_player] -= 1
            else:
                current += 1
            ##move other player into position
            other = current
            other_pos = -1
            while other < len(tasks):
                if tasks[other][0] == other_player[current_player]:
                    other_pos = other
                    break
                else:
                    other += 1
            if other_pos != -1:
                if tasks[other_pos][1] > position[other_player[current_player]]:
                    position[other_player[current_player]] += 1
                elif tasks[other_pos][1] < position[other_player[current_player]]:
                    position[other_player[current_player]] -= 1
                else:
                    pass
            seconds +=1
        print ("Case #", i+1, ":", " ", seconds, sep= "")

main()
