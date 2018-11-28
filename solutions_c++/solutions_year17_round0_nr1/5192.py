#include <bits\stdc++.h>
using namespace std;
typedef vector<int> vi;

vi neighbors(int s, int t, int k) {
	int i = (1 << k) - 1;
	vi res;
	while (i <= t) res.push_back(s ^ i), i <<= 1;
	return res;
}

int bfs(int s, int t, int k) {
	if (s == t) return 0;
	vi d(1000000, -1); d[s] = 0;
	queue<int> q; q.push(s);
	while (!q.empty()) {
		int u = q.front(); q.pop();
		//cout << bitset<16>(u) << endl;
		vi nb = neighbors(u, t, k);
		for (int i = 0; i < nb.size(); ++i) {
			int v = nb[i];
			if (d[v] != -1) continue;
			d[v] = d[u] + 1;
			if (v == t) return d[v];
			q.push(v);
		}
	}
	return -1;
}

int greedy(string s, int k) {
	int res = 0;
	for (int i = 0; i < s.size(); ++i) {
		if (s[i] == '+') continue;
		if (s[i] == '-' && i + k <= s.size()) {
			for (int j = i; j < i + k; ++j) s[j] = (s[j] == '+' ? '-' : '+');
			res++;
		}
		else return -1;
	}
	return res;
}

int main()
{
	int t; cin >> t;
	for (int ti = 1; ti <= t; ti++) {
		string s; int k, a = 0; cin >> s >> k;
		//for (int i = 0; i < s.size(); ++i) a *= 2, a += (s[i] == '+' ? 1 : 0);
		//int res = bfs(a, (1 << s.size()) - 1, k);
		int res = greedy(s, k);
		if (res >= 0) cout << "Case #" << ti << ": " << res << endl;
		else cout << "Case #" << ti << ": IMPOSSIBLE\n";
	}
}

//int main()
//{
//	for (int k = 2; k <= 10; ++k)
//		for (int i = k; i <= 10; ++i) {
//			cout << i << " " << k << endl;
//			for (int t = 0; t < (1 << i); ++t) {
//				string s(i, '-');
//				for (int j = 0; j < i; ++j) if (t & (1 << j)) s[j] = '+';
//				int res = bfs(t, (1 << i) - 1, k); int res2 = greedy(s, k);
//				//if (res >= 0) cout << "Case #(" << s << ", " << k << "): " << res << " " << res2 << endl;
//				//else cout << "Case #(" << s << ", " << k << "): IMPOSSIBLE " << " " << res2 << "\n";
//				if (res != res2) cout << "!!!!!!!!!!! " << res << " " << res2 << "\n";
//			}
//		}
//}