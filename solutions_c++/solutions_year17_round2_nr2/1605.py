#include <cstdio>

using namespace std;

int main() {
	int t;
	scanf("%d",&t);
	for (int cs = 1; cs <= t; ++cs)
	{
		int n,r,o,y,g,b,v;
		bool possible = true;
		scanf("%d%d%d%d%d%d%d", &n, &r, &o, &y, &g, &b, &v);
		if ((r > n/2) || (o > n/2) || (y > n/2) || (g > n/2) || (b > n/2) || (v > n/2)) {
			possible = false;
		}
		printf("Case #%d: ",cs);

		char char1, char2, char3;
		int amount1, amount2, amount3;
		if ((r >= b) && (r >= y)) {
			char1 = 'R';
			amount1 = r;
			char2 = 'B';
			amount2 = b;
			char3 = 'Y';
			amount3 = y;
		} else if ((b >= r) && (b >= y)) {
			char1 = 'B';
			amount1 = b;
			char2 = 'R';
			amount2 = r;
			char3 = 'Y';
			amount3 = y;
		} else if ((y >= b) && (y >= r)) {
			char1 = 'Y';
			amount1 = y;
			char2 = 'B';
			amount2 = b;
			char3 = 'R';
			amount3 = r;
		}

		if (possible) {
			int rem = amount2 + amount3 - amount1;
			for (int i = 0; i < rem; ++i)
			{
				printf("%c%c%c", char1,char2,char3);
			}
			for (int i = rem; i < amount2; ++i)
			{
				printf("%c%c", char1,char2);
			}
			for (int i = amount2; i < amount1; ++i)
			{
				printf("%c%c", char1,char3);
			}
			printf("\n");
		} else {
			printf("IMPOSSIBLE\n");
		}
		
	}
	return 0;
}