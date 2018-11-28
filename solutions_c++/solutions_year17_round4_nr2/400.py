#include <iostream>
#include <iomanip>
#include <cmath>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <queue>
#include <map>

using namespace std;

bool on_train[1001][1001];
bool seat[1001][1001];

int ciel(int p, int q) {
	int ans = p/q;
	if (ans * q < p) ans ++;
	return ans;
}

int main() {
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; tt ++) {
		cout << "Case #" << tt << ": ";
		int n, c, m;
		cin >> n >> c >> m;
		vector<int> p_blist[1001];
		int p_cnt[1001], b_cnt[1001];
		memset(p_cnt, 0, sizeof(p_cnt));
		memset(b_cnt, 0, sizeof(b_cnt));
		for (int i = 0; i < m; i ++) {
			int p, b;
			cin >> p >> b;
			p_cnt[p] ++;
			b_cnt[b] ++;
			p_blist[p].push_back(b);
		}
		int p_cum = 0;
		int ans = 0;
		for (int i = 1; i <= n; i ++) {
			p_cum += p_cnt[i];
			ans = max(ans, ciel(p_cum, i));
		}
		for (int i = 1; i <= c; i ++) {
			ans = max(ans, b_cnt[i]);
		}
		
		int prom = 0;
		p_cum = 0;
		for (int i = 1; i <= n; i ++) {
			if (p_cnt[i] > ans) prom += p_cnt[i] - ans;
		}
	//	memset(on_train, 0, sizeof(on_train));
	//	memset(seat, 0, sizeof(seat));
	//	for (int i = 1; i <= n; i ++) {
	//		for (int e : p_blist[i]) {
	//			
	//		}
	//	}
		
		cout << ans <<' ' << prom << endl;
	}
	return 0;
}

