#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double Double;
int F[4][105][105][105];
const int INF = 1000000000;
void solve(int cn) {
	int N, P;
	scanf("%d%d", &N, &P);
	int cnt[4] = {0};
	for (int i = 0; i < N; ++i) {
		int a;
		scanf("%d", &a);
		++cnt[a % P];
	}
	vector<int> u(4);
	for (u[1] = 0; u[1] <= cnt[1]; ++u[1])
		for (u[2] = 0; u[2] <= cnt[2]; ++u[2])
			for (u[3] = 0; u[3] <= cnt[3]; ++u[3])
				for (int e = 0; e < P; ++e) {
					int &ret = F[e][u[1]][u[2]][u[3]];
					if (!u[1] && !u[2] && !u[3] && !e) {
						ret = 0;
						continue;
					}
					ret = -INF;
					for (int l = 1; l < P; ++l) {
						if (!u[l]) continue;
						auto v = u;
						--v[l];
						int e2 = (e - l + P) % P;
						ret = max(ret, F[e2][v[1]][v[2]][v[3]] + (e2 == 0));
					}
				}
	int ans = 0;
	for (int e = 0; e < P; ++e)
		ans = max(ans, F[e][cnt[1]][cnt[2]][cnt[3]]);
	printf("Case #%d: %d\n", cn, ans + cnt[0]);
}
int main() {
	int TC;
	scanf("%d", &TC);
	for (int cn = 1; cn <= TC; ++cn) {
		solve(cn);
	}
}

