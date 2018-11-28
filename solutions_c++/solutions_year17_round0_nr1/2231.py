#include <cstdio>
#include <cstring>

int getBlankPos(char *cake, int begin)
{
	int i;

	for (i = begin; cake[i]; ++i) {
		if (cake[i] == '-')
			return i;
	}
	return i;
}

int getFlipCount(char *cake, int flipRange)
{
	int begin, end;
	int cakelen;
	int flipCnt;

	cakelen = strlen(cake);

	begin = getBlankPos(cake, 0);
	end = begin + flipRange;

	flipCnt = 0;
	while (end <= cakelen) {
		for (int i = begin; i < end; ++i) {
			if (cake[i] == '+')
				cake[i] = '-';
			else
				cake[i] = '+';
		}
		flipCnt++;

		begin = getBlankPos(cake, begin+1);
		end = begin + flipRange;
	}
	if (begin < cakelen)
		return -1;

	return flipCnt;
}

int main()
{
	int tcase;
	char cake[1001];
	int flipRange;
	int flipCnt;

	scanf("%d", &tcase);

	for (int i = 1; i <= tcase; ++i) {
		scanf("%s%d", cake, &flipRange);

		flipCnt = getFlipCount(cake, flipRange);
		if (flipCnt < 0) {
			printf("Case #%d: IMPOSSIBLE\n", i);
		}
		else{
			printf("Case #%d: %d\n", i, flipCnt);
		}
	}

	return 0;
}
