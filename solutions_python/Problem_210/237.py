t = int(input())  
for i in range(1, t + 1):
  AC, AJ = [int(x) for x in input().split(' ')]
  activities = []
  for j in range(AC):
    start, stop = [int(x) for x in input().split(' ')]
    activities.append({'start': start, 'stop': stop, 'who': 'C'})
  for j in range(AJ):
    start, stop = [int(x) for x in input().split(' ')]
    activities.append({'start': start, 'stop': stop, 'who': 'J'})
  activities.sort(key=lambda x: x['start'])
  if AC < 2 and AJ < 2:
    result = 2
  else:
    if activities[1]['stop'] - activities[0]['start'] > 720 and activities[1]['start'] - activities[0]['stop'] < 720:
      result = 4
    else:
      result = 2
  print("Case #{}: {}".format(i, result))
