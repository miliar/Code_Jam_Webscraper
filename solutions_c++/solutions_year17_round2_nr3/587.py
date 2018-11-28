#include <bits/stdc++.h>
using namespace std;

const int SIZE = 205;

#define fi first
#define se second


int n, Q;
long long e[SIZE], s[SIZE];
long long d[SIZE][SIZE];
double ans[SIZE][SIZE];

void solve() {
	cin>>n>>Q;
	for (int i = 0; i < n; i++) {
		cin>>e[i]>>s[i];
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			ans[i][j] = (long long) 1e17;
			cin>>d[i][j];
			if (d[i][j] == -1) {
				d[i][j] = (long long) 1e17;
			}
		}
	}

	for (int k=0; k<n; ++k)
	for (int i=0; i<n; ++i)
	for (int j=0; j<n; ++j) {
		d[i][j] = min (d[i][j], d[i][k] + d[k][j]);
	}

	
	for (int i=0; i<n; ++i)
	for (int j=0; j<n; ++j) {
		if (d[i][j] <= e[i]) {
			ans[i][j]=min(ans[i][j], 1.0 * d[i][j] / s[i]);
		}
	}

	for (int k=0; k<n; ++k)
	for (int i=0; i<n; ++i)
	for (int j=0; j<n; ++j) {
		ans[i][j] = min (ans[i][j], ans[i][k] + ans[k][j]);
	}

	for (int i =0; i < Q; i++) {
		int a,b;
		cin>>a>>b;
		a--;
		b--;
		printf(" %.7lf", ans[a][b]);
	}
	cout<<endl;
}

void renull() {
	memset(e, 0, sizeof(e));
	memset(s, 0, sizeof(s));
	memset(d, 0, sizeof(d));
	memset(ans, 0, sizeof(ans));
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin>>t;
	for (long long t_id = 1; t_id <= t; t_id++) {
		renull();
		printf("Case #%lld:", t_id);
		solve();
	}

	return 0;
}
