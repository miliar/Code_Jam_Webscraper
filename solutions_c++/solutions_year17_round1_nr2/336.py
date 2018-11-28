#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
const int nmax = 50 + 18;

int T, N, P;
int R[nmax], Q[nmax][nmax], q[nmax][nmax], qi[nmax], l[nmax][nmax], r[nmax][nmax];
int ans, global_k;

bool cmp(int i, int j)
{
	return Q[global_k][i] > Q[global_k][j];
}

void calcrange(int &l, int &r, int Q, int R)
{
	r = 10 * Q / 9 / R;
	l = 10 * Q / 11 / R;
	if (l * R * 11 != 10 * Q)
		++l;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for (int cases = 1; cases <= T; ++cases) {
		scanf("%d%d", &N, &P);
		for (int i = 1; i <= N; ++i) {
			scanf("%d", R + i);
		}
		for (int i = 1; i <= N; ++i) {
			for (int j = 1; j <= P; ++j) {
				scanf("%d", Q[i] + j);
				calcrange(l[i][j], r[i][j], Q[i][j], R[i]);
				q[i][j] = j;
				//printf("%d %d\n", l[i][j], r[i][j]);
			}
			global_k = i;
			sort(q[i] + 1, q[i] + P + 1, cmp);
			//for (int j = 1; j <= P; ++j)
			//	printf("%d ", q[i][j]);
			//printf("\n");
			qi[i] = 1;
		}
		ans = 0;
		bool valid = 1;
		while (valid) {
			for (int i = 1; i <= N; ++i)
				if (qi[i] > P) {
					valid=  0;
					break;
				}
			if (!valid) break;
			
			int L = 0, R = 10000000;
			for (int i = 1; i <= N; ++i) {
				int now = q[i][qi[i]];
				if (L < l[i][now])
					L = l[i][now];
				if (R > r[i][now])
					R = r[i][now];
			}
			if (R <= 0) break;
			if (L <= R) {
				ans += 1;
				for (int i = 1; i <= N; ++i)
					++qi[i];
			}
			else {
				for (int i = 1; i <= N; ++i) {
					while (qi[i] <= P && l[i][q[i][qi[i]]] > R)
						++qi[i];
				}
			}
		}
		printf("Case #%d: %d\n", cases, ans);
	}
	return 0;
}
