#include <bits/stdc++.h>
#define pb push_back
using namespace std;

string s;
int n, k;
int T;
map<vector<bool>, int> used;

int main() {
	cin >> T;
	for (int tc = 0; tc < T; tc++) {
		cin >> s >> k;
		used.clear();
		vector<bool> head;
		n = s.size();
		for (int i = 0; i < n; i++) {
			if (s[i] == '+') head.pb(1);
			else head.pb(0);
		}
		queue<vector<bool>> q;
		q.push(head);
		used[head] = 0;
		while (!q.empty()) {
			vector<bool> v = q.front(); q.pop();
			int dist = used[v];
			for (int i = 0; i < k; i++) v[i] = !v[i];
			for (int i = 0; i + k <= n; i++) {
				if (!used.count(v)) {
					used[v] = dist + 1;
					q.push(v);
				}
				v[i] = !v[i];
				if (i + k < n) v[i + k] = !v[i + k];
			}
		}
		vector<bool> happy(n, 1);
		int ans = -1;
		if (used.count(happy)) ans = used[happy]; 
		cout << "Case #" << tc + 1 << ": ";
		if (ans > -1) cout << ans << endl;
		else cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}