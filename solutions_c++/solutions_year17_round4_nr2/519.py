#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

const int MAXN = 1010;
const int INF = 0x3f3f3f3f;

int need[MAXN];
int people[MAXN][MAXN];

void clear() {
	memset(people, 0, sizeof people);
	memset(need, 0, sizeof need);
}

int main() {
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);

	ios_base::sync_with_stdio(false);

	int T; cin >> T;
	for (int kase = 1; kase <= T; kase++) {
		clear();
		int N, C, M;
		cin >> N >> C >> M;
		for (int i = 0; i < M; i++) {
			int P, B; cin >> P >> B;
			people[B][P]++;
		}
		for (int i = 1; i <= C; i++) {
			for (int j = 1; j <= N; j++) {
				people[i][j] = people[i][j - 1]  + people[i][j];
			}
		}
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= C; j++) {
				need[i] += people[j][i];
			}
		}
		int ans1 = 0, ans2 = 0;
		for (int i = 1; i <= N; i++) {
			ans1 = max((need[i] + i - 1) / i, ans1);
		}
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= C; j++) {
				ans1 = max(ans1, people[j][i]);
			}
		}
		for (int i = 1; i <= N; i++) {
			ans2 += max(0, need[i] - need[i - 1] - ans1);
		}
		cout << "Case #" << kase << ": " << ans1 << " " << ans2 << endl;
	}
  return 0;
}