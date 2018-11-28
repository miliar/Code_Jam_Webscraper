#include <stdio.h>
#include <algorithm>

using namespace std;

int T;
int N, P;
int G[200];
int p[5];

int solve()
{
	for (int i = 0; i <= P; i++) {
		p[i] = 0;
	}

	for (int i = 0; i < N; i++) {
		p[G[i]%P]++;
	}

	if (P == 2) {
		return p[0] + (p[1]+1) / 2;
	} else if (P == 3) {
		int mini = min(p[1], p[2]);
		p[1] -= mini;
		p[2] -= mini;
		int res = mini + p[0] + (p[1] / 3) + (p[2] / 3);
		p[1] %= 3;
		p[2] %= 3;
		if (p[1] + p[2] > 0) res++;
		return res;
	} else {
		int res = p[0];
		res += p[2] / 2;
		p[2] %= 2;
		
		int mini = min(p[1], p[3]);
		res += mini;
		p[1] -= mini;
		p[3] -= mini;

		if (p[1] >= 2 && p[2] == 1) {
			res++;
			p[1] -= 2;
			p[2]--;
		}

		if (p[3] >= 2 && p[2] == 1) {
			res++;
			p[3] -= 2;
			p[2]--;
		}

		res += p[1]/4;
		p[1] %= 4;
		res += p[3]/4;
		p[3] %= 4;

		if (p[1]+p[2]+p[3] > 0) res++;
		return res;
	}
}

int main()
{
	scanf(" %d", &T);

	for (int cas = 1; cas <= T; cas++) {
		scanf(" %d %d", &N, &P);
		for (int i = 0; i < N; i++) {
			scanf(" %d", &G[i]);
		}

		int res = solve();

		printf("Case #%d: %d\n", cas, res);
	}

	return 0;
}