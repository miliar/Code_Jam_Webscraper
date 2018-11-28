#include <iostream>
#include <cstring>
#include <iomanip>
#include <stdio.h>
using namespace std;

const int zuida = 1000000005;
const int maxn = 105;
int E[maxn], D[maxn][maxn];
double S[maxn], ans[maxn][maxn];

int main() {
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int t;
	cin >> t;
	int count = 1;
	while(t--)
	{
		int n, q;
		cin >> n >> q;
		for (int i = 1; i <= n; ++i) {
			cin >> E[i] >> S[i];
		}
		for (int i = 1; i <= n; ++i) {
			for (int j = 1; j <= n; ++j) {
				cin >> D[i][j];
				if (D[i][j] == -1) D[i][j] = zuida; 
			}
		}
		for (int i = 1; i <= n; ++i) {
			for (int j = 1; j <= n; ++j) 
			if (j!=i) {
				for (int k = 1; k <= n; ++k) 
				if (i!=j && j!=k) {
					D[j][k] = min(D[j][i] + D[i][k], D[j][k]);
				}
			}
		}
		for (int i = 1; i <= n; ++i) {
			for (int j = 1; j <= n; ++j) {
				if (D[i][j] <= E[i]) ans[i][j] = D[i][j] / S[i];
				else ans[i][j] = 1e20;
			}
		}
		for (int i = 1; i <= n; ++i) {
			for (int j = 1; j <= n; ++j) 
			if (j!=i) {
				for (int k = 1; k <= n; ++k) 
				if (i!=j && j!=k) {
					ans[j][k] = min(ans[j][i] + ans[i][k], ans[j][k]);
				}
			}
		}
		cout << "Case #" << count++ <<": ";
		for (int i = 1; i <= q; ++i) {
			int a, b;
			cin >> a >> b;
			cout << fixed << setprecision(10) << ans[a][b];
			if (i == q) 
				cout << endl;
			else 
				cout << " ";
		}
	}
} 
