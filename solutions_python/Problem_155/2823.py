# Read input
lines = [line.strip() for line in open('A-large.in')]  

# Pull number of test cases
test_cases = int(lines[0])

# Remove first line (number of test cases) from list
del lines[0]

for i in range(0, test_cases):
  v = lines[i].split()

  max_shyness = int(v[0])
  audience = v[1]

  # Loop through audience and figure out minimum number of friends at each level needed to 
  # insure that everyone stands
  friends_needed = 0
  audience_members_standing = 0

  # NOTE: The given end point is never part of the generated list.
  # https://docs.python.org/2/library/functions.html#range
  for j in range(0, max_shyness + 1):
    additional_friends_needed = 0

    audience_current_shyness = int(audience[j])
  
    if (audience_members_standing < j):
      additional_friends_needed = (j - audience_members_standing)

    audience_members_standing = audience_members_standing + additional_friends_needed + audience_current_shyness
    friends_needed = friends_needed + additional_friends_needed

  print ("Case #" + str(i + 1) + ": " + str(friends_needed))
