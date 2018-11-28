#include <bits/stdc++.h>

using namespace std;

long long e[200], s[200];
long long d[200][200];
double t[200][200];

void main2() {
	int n, q;
	cin >> n >> q;
	for (int i = 0; i < n; i++)
		cin >> e[i] >> s[i];
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> d[i][j];
			if (d[i][j] == -1)
				d[i][j] = 1LL<<60;
		}
		d[i][i] = 0;
	}
	for (int k = 0; k < n; k++)
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			t[i][j] = (d[i][j] > e[i]) ? (1e18) : ((double)d[i][j]/s[i]);
	for (int k = 0; k < n; k++)
		for (int i = 0; i < n; i++)
			for (int j = 0; j < n; j++)
				t[i][j] = min(t[i][j], t[i][k] + t[k][j]);
	for (int i = 0; i < q; i++) {
		int u, v;
		cin >> u >> v;
		cout << fixed << setprecision(9) << t[u-1][v-1] << ' ';
	}
	cout << endl;
}

int main() {
	int t; cin >> t;
	for (int o = 1; o <= t; o++) {
		cout << "Case #" << o << ": ";
		main2();
	}
	return 0;
}
