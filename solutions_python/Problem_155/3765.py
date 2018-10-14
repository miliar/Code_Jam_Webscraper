for case in range(int(input())):
	max_shyness, audience = input().split()
	invites = total = 0
	for shyness, members in enumerate(audience):
		if total >= int(max_shyness):
			break
		elif total < shyness and int(members) > 0:
			invites += (shyness - total)
			total += invites
		total += int(members)
	print('Case #%d: %d' % ((case + 1), invites))
