#include <bits/stdc++.h>

using namespace std;

const int inf = (int)1e9;

string s;  
queue < int > q;
int T, k, d[1050];

int main() {
	freopen(".in", "r", stdin);
	freopen(".out", "w", stdout);

	cin >> T;

	for (int i = 1; i <= T; i++) {
		cin >> s >> k;
		int n = (int)s.size();
		for (int i = 0; i < (1 << n); i++)
			d[i] = inf;
		int st = 0;
		for (int i = 0; i < n; i++) {
			if (s[i] == '+')
				st |= (1 << i);
		}
		d[st] = 0;
		q.push(st);
		while (!q.empty()) {
			int mask = q.front();
			q.pop();
			for (int i = 0; i < n - k + 1; i++) {
				int tomask = mask;
				for (int j = i; j <= i + k - 1; j++)
					tomask ^= (1 << j);
				if (d[mask] + 1 < d[tomask]) {
					d[tomask] = d[mask] + 1;
					q.push(tomask);
				}
			}
		}
		cout << "Case #" << i << ": ";
		if (d[(1 << n) - 1] == inf)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << d[(1 << n) - 1] << endl;
	}

	return 0;
}
