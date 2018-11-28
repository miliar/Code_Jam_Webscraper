#include<bits/stdc++.h>

using namespace std;

#define ll long long int
#define pb push_back
#define f first
#define s second
#define mod 1e9+7
#define mp make_pair
#define PI 3.14159265
#define eps 0.000001

const int N = 1234567;

char t[30][30];
int n, m;

void solve() {
	for(int i = 0; i < n; i++) {
		for(int j = 0; j < m; j++) {
			if(t[i][j] != '?') {
				for(int k = j - 1; k >= 0 && t[i][k] == '?'; k--) {
						t[i][k] = t[i][j];
					}
					for(int k = j + 1; k < m && t[i][k] == '?'; k++) {
						t[i][k] = t[i][j];
					}
			}
		}
	}
}

#define test
int main() {
	ios::sync_with_stdio(false); cin.tie(0);
#ifdef test
	freopen("a.in","rt",stdin);
	freopen("a.out","wt",stdout);
#endif
	int tt;
	cin >> tt;
	for(int ii = 1; ii <= tt; ii++) {
		cout << "Case #" << ii << ": " << endl;
		cin >> n >> m;
		char a[n][m];
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				cin >> a[i][j];
				t[i][j] = a[i][j];
			}
		}
		solve();
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				if(t[i][j] != '?') {
					for(int k = i - 1; k >= 0 && t[k][j] == '?'; k--) {
						t[k][j] = t[i][j];
					}
					for(int k = i + 1; k < n && t[k][j] == '?'; k++) {
						t[k][j] = t[i][j];
					}
				}
			}
		}
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				cout << t[i][j];
			}
			cout << endl;
		}
	}
	return 0;
}