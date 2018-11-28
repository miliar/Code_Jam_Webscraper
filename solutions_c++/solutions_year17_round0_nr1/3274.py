# include <bits/stdc++.h>
using namespace std;

int main()
{		
	int T; cin >> T;
	for(int tt=1; tt<=T; ++tt) {
		string s; int f;
		cin >> s >> f;
		
		int d = 0;
		for(int i=0; i<s.size(); ++i) {
			d |= (s[i] == '-') << i;
		}
		
		const int INF = 1e9;
		vector<int> tab(1 << 11, INF);
		tab[d] = 0;
		
		int mask = (1 << f) - 1;
		
		queue<int> que; que.push(d);
		while(!que.empty()) {
			int cur = que.front(); que.pop();
			for(int i=0; i+f<=s.size(); ++i) {
				int nxt = cur ^ (mask << i);
				if (tab[cur] + 1 < tab[nxt]) {
					tab[nxt] = tab[cur] + 1;
					que.push(nxt);
				}
			}
		}
		
		if (tab[0] == INF) printf("Case #%d: IMPOSSIBLE\n", tt);
		else printf("Case #%d: %d\n", tt, tab[0]);
	}
	return 0;
}