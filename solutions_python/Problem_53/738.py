for tc in range(1, int(input()) + 1):
	n, k = map(int, raw_input().split())
	z = 2**n
	print("Case #%d: %s" % (tc, "ON" if k % z == z - 1 else "OFF"))