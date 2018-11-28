#include <cstdio>
#include <algorithm>
#include <cassert>

using namespace std;

const int Way[6][4] = {
	{0, 0, 4, 1},
	{0, 1, 2, 1},
	{0, 2, 0, 1},
	{1, 0, 1, 1},
	{2, 1, 0, 1},
	{4, 0, 0, 1}
};

int Gao[105][105][105];

int cases;
int N, P;
int T[5];

int main() {
	scanf("%d", &cases);
	for(int xx = 1; xx <= cases; ++xx) {
		scanf("%d%d", &N, &P);
		memset(T, 0, sizeof(T));
		for(int i = 0; i < N; ++i) {
			int x;
			scanf("%d", &x);
			T[x % P]++;
		}
		int ans = 0;
		ans += T[0];
		if(P == 2) {
			ans += T[1] / 2 + (T[1] % 2);
		} else if(P == 3) {
			int tmp = min(T[1], T[2]);
			ans += tmp;
			T[1] -= tmp;
			T[2] -= tmp;
			if(T[1] != 0) {
				ans += T[1] / 3 + (T[1] % 3 != 0);
			} else {
				ans += T[2] / 3 + (T[2] % 3 != 0);
			}
		} else if(P == 4) {
			memset(Gao, 255, sizeof(Gao));
			Gao[0][0][0] = 0;
			for(int i = 0; i <= T[1]; ++i)
				for(int j = 0; j <= T[2]; ++j)
					for(int k = 0; k <= T[3]; ++k) {
						for(int l = 0; l < 6; ++l) {
							int di = i - Way[l][0];
							int dj = j - Way[l][1];
							int dk = k - Way[l][2];
							if(di >= 0 && dj >= 0 && dk >= 0 && Gao[di][dj][dk] != -1)
								Gao[i][j][k] = max(Gao[i][j][k], Gao[di][dj][dk] + Way[l][3]);
						}
					}
			ans = -1;
			for(int i = T[1] - 3; i <= T[1]; ++i)
				for(int j = T[2] - 1; j <= T[2]; ++j)
					for(int k = T[3] - 3; k <= T[3]; ++k)
						if(i >= 0 && j >= 0 && k >= 0 && Gao[i][j][k] != -1) {
							int v = (i == T[1] && j == T[2] && k == T[3]) ? 0 : 1;
							ans = max(ans, Gao[i][j][k] + v);
						}
			ans += T[0];
		} else {
			assert(false);
		}
		printf("Case #%d: %d\n", xx, ans);
	}
}

