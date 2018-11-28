#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>

using namespace std;
int N, M, C;
pair<int, int> ticket[1010];
bool seated[1010], used[1010]; 
int cnt[1010];
int main() {
	int T;
	cin >> T;
	for(int cas = 1; cas <= T; ++cas) {
		cin >> N >> C >> M;
		for(int i = 1; i <= N; ++i) {
			cnt[i] = 0;
		}
		for(int i = 1; i <= M; ++i) {
			int p,b;
			cin >> p >> b;
			ticket[i].first = p;
			ticket[i].second = b;
			used[i] = false;
			cnt[p]++;
		}
		sort(ticket + 1, ticket + M + 1);
		int rest = M;
		int ans = 0;
		for(int i = 1; i <= M; ++i) {
			//printf("%d :%d\n",i, rest);
			if(rest == 0) {
				break;
			}
			ans++;
			for(int j = 1; j <= C; ++j) {
				seated[j] = false;
			}
			int last = 1;
			for(int j = 1; j <= N; ++j) {
				for(int k = last; k <= M; ++k) {
					if(!used[k] && !seated[ticket[k].second] && ticket[k].first >= j) {
						rest--;
						//printf("%d %d %d\n",i,j,ticket[k].first);
						last = k + 1;
						used[k] = true;
						seated[ticket[k].second] = true;
						break;
					}
				}
			} 
		}
		int cost = 0;
		for(int i = 1; i <= N; ++i) {
			if(cnt[i] > ans) {
				cost += cnt[i] - ans;
			}
		}
		printf("Case #%d: %d %d\n",cas,ans,cost);

	}

	return 0;
}