
# File handles
input_file = open('D-small-attempt0.in', 'r')
output_file = open('D-small-attempt0.out', 'w')

def CompareListsForHigherValuesOfSecondList(list1, list2):
    list1_sorted = sorted(list1)
    list2_sorted = sorted(list2)
    points = 0

    for x in range(len(list1_sorted)):
        for y in range(len(list2_sorted)):
            if list2_sorted[y] > list1_sorted[x]: 
                points = points + 1
                list2_sorted[y] = 0
                list1_sorted[x] = 0
                break

    return points

def GetNaomiPoints(listNaomi, listKen, pieces):
    ken_points_normal_war = CompareListsForHigherValuesOfSecondList(listNaomi, listKen)
    naomi_points_normal_war = pieces - ken_points_normal_war
    #print("Naomi would win:" + str(naomi_points_normal_war))
    return naomi_points_normal_war

def GetPoints(listNaomi, listKen, pieces):
    naomi_points_normal_war = CompareListsForHigherValuesOfSecondList(listKen, listNaomi)
    return naomi_points_normal_war
  
def GetNaomisBestInDeceitfulWar(listNaomi, listKen, pieces):
    list_naomi_possible_points = []

    for i in range(pieces):
        list_naomi_possible_points.append(GetPoints(listNaomi, listKen, pieces))
        min_naomi = min(listNaomi)
        listNaomi.remove(min_naomi)
        max_ken = max(listKen)
        listKen.remove(max_ken)
        pieces = pieces - 1

    return max(list_naomi_possible_points)

def SolveOneGame(caseNumber):
    pieces = int(input_file.readline())

    # Get naomi values
    naomi_line = input_file.readline()
    naomi_values = [float(i) for i in naomi_line.split()]
   
    # Get Ken values
    ken_line = input_file.readline()
    ken_values = [float(i) for i in ken_line.split()]

    second = GetNaomiPoints(naomi_values, ken_values, pieces)
    first = GetNaomisBestInDeceitfulWar(naomi_values, ken_values, pieces)
    output_file.write("Case #" + str(caseNumber) + ": " + str(first) + " " + str(second) + "\n")

# The main logic
number_of_games = int(input_file.readline())
for g in range(0, number_of_games):
    SolveOneGame(g + 1)

# Close the files
input_file.close()
output_file.close()