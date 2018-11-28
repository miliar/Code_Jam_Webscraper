#include <bits/stdc++.h>
#include <unistd.h>

#define debug(x) cout << #x << " = " << x << endl
#define fori(i, ini, lim) for(int i = int(ini); i < int(lim); i++)
#define ford(i, ini, lim) for(int i = int(ini); i >= int(lim); i--)

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

const int MAX = 1e2 + 6;
ll need[MAX], helper[MAX], lft[MAX], rgt[MAX];
ll package[MAX][MAX];
bool alive[MAX][MAX];
int n, p;

int main() {
	int t;
	scanf("%d", &t);
	int kase = 1;
	while(t--) {
		memset(alive, true, sizeof alive);
		scanf("%d %d", &n, &p);
		fori(i, 1, n + 1) {
			scanf("%lld", need + i);
		}
		fori(i, 1, n + 1) {
			fori(j, 1, p + 1) {
				scanf("%lld", &package[i][j]);
			}
			sort(package[i] + 1, package[i] + p + 1);
		}

		int ans = 0;
		ll servings = 1;
		while(1) {
			fori(i, 1, n + 1) {
				helper[i] = need[i] * servings;
				lft[i] = ceil(0.9 * helper[i]);
				rgt[i] = ceil(1.1 * helper[i]);
			}	
			int can_take = 1 << 30;
			bool all_greater = true;
			fori(i, 1, n + 1) {
				int total = 0;
				fori(j, 1, p + 1) {
					if(alive[i][j]) {
						if(lft[i] <= package[i][j] && package[i][j] <= rgt[i]) {
							total++;
						}
						if(lft[i] <= package[i][j]) {
							all_greater = false;
						}
					}
				}
				can_take = min(can_take, total);
			}
			fori(i, 1, n + 1) {
				int taken = 0;
				fori(j, 1, p + 1) {
					if(taken == can_take) {
						break;
					}
					if(alive[i][j]) {
						alive[i][j] = false;
						taken++;
					}
				}
			}
			ans += can_take;
			servings++;
			if(all_greater) {
				break;
			}
		}
		printf("Case #%d: %d\n", kase++, ans);
	}

	return 0;
}

