import sys
import os

def tokenizer(stream):
    for line in stream:
        for token in line.split():
            yield token

filename = 'A-large.in'

def winning_percentage(line):
    line = line.replace('.','')
    return line.count('1')/len(line)

def get_enemies(line):
    enemies = []
    for i in range(len(line)):
        if line[i] != '.':
            enemies.append(i)
    return enemies

def average(values):
    return float(sum(values))/float(len(values))

def getOWP(winning_percentages, enemies, playerNo, results):
    e = enemies[playerNo]
    return average([(winning_percentages[enemy]*float(len(enemies[enemy]))-float(results[enemy][playerNo]))/float((len(enemies[enemy])-1)) for enemy in e])

#def getOOWP(winning_percentages, enemies, playerNo, results):
#    return average([getOWP(opp) for opp in opponentsOpponents])

def opponentsOpponents(winning_percentages, enemies, playerNo):
    oppopp = []
    for enemy in enemies:
        oppopp.extend(enemies[enemy])
    return oppopp

def getResults(line):
    results = {}
    for i in range(len(line)):
        if line[i] == '1':
            results[i] = 1
        elif line[i] == '0':
            results[i] = 0
    return results

def getRPI(winning_percentages, enemies, playerNo, results):
    #oo = opponentsOpponents(winning_percentages, enemies, playerNo)
    #print(oo)
    #oo = set(oo)
    #print(oo)
    #oo.remove(playerNo)
    return 0.25*winning_percentages[playerNo] + \
           0.5*getOWP(winning_percentages, enemies, playerNo, results) + \
           0.25*average([getOWP(winning_percentages, enemies, o, results) for o in enemies[playerNo]])
          
def main():
    with open(filename, 'r') as file:
        tokenized_file = tokenizer(file)
        T = int(next(tokenized_file))
        for case in range(T):
            winning_percentages = {}
            enemies = {}
            results = {}
            N = int(next(tokenized_file))
            for row in range(N):
                line = next(tokenized_file)
                enemies[row] = get_enemies(line)
                results[row] = getResults(line)
                winning_percentages[row] = winning_percentage(line)
            #for playerNo in range(N):
                #print("%d's owp: %f"%(playerNo, getOWP(winning_percentages, enemies, playerNo, results)))
                #print("%d's oowp: %f"%(playerNo, get))
            print("Case #%d: "%(case+1))
            for player in range(N):
                print(getRPI(winning_percentages, enemies, player, results))

main()