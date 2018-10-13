
t = int(input())
for i in range(1, t + 1):
  value = input();
  goal, other_horses = [int(s) for s in value.split(" ")];
  #print("gola:{}".format(goal))
  #data containers
  start_poses = [0 for h in range(other_horses)]
  speeds = [0 for h in range(other_horses)]
  #read input
  for h in range(0, other_horses):
    pos, speed = [int(s) for s in input().split(" ")];
    start_poses[h] = pos;
    speeds[h] = speed;

  #SOLVE
  timeToGoal = -1
  for h in range(0, other_horses):
    matka = goal - start_poses[h];
    aika = matka / speeds[h];
    #print("aika:{} matka:{}".format(aika,matka))
    if(timeToGoal == -1 or timeToGoal < aika):
      timeToGoal = aika;
  #print("time to goal {}".format(timeToGoal))
  #print(speeds)
  #PRINT RESULT
  vastausaika = goal / timeToGoal

  print("Case #{0:.0f}: {1:.6f}".format(i, vastausaika));









