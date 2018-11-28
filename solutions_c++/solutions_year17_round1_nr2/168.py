#include <bits/stdc++.h>

using namespace std;
#define For(i,l,r) for (int i = l; i <= r; ++i) 
#define Cor(i,l,r) for (int i = l; i >= r; --i)

pair<int,int> last; 
bool legal(int x, int y) {
	int l = (double)x / (1.1 * y) - 1e-9 + 1;
	int r = (double)x / (0.9 * y) + 1e-9;
	last = make_pair(l, r);
	return l <= r;
}

int n, m;
int require[55], A[55][55], p[55], pick[55];
int main() {
	int T; cin >> T;
	For(TK,1,T) {
		printf("Case #%d: ", TK);
		cin >> n >> m;
		For(i,1,n) scanf("%d", &require[i]);
		For(i,1,n) {
			For(j,1,m) scanf("%d", &A[i][j]);
			sort(A[i] + 1, A[i] + m + 1);
		}
		memset(p, 0, sizeof p);
		int ans = 0;
		while (true) {
			bool hasNext = true;
			For(i,1,n) {
				while (p[i] < m && !legal(A[i][p[i] + 1], require[i])) ++p[i]; 
				if (p[i] == m) {
					hasNext = false ;
					break ;
				}
				pick[i] = A[i][p[i] + 1];
			}
			if (!hasNext) break ;
			int Max = 0, Min = 1e9;
			For(i,1,n) {
				legal(pick[i], require[i]);
				Max = max(Max, last.first);
				Min = min(Min, last.second);
			}
			if (Max <= Min) {
				++ans; 
				For(i,1,n) ++p[i];
			} else {
				For(i,1,n) {
					legal(pick[i], require[i]);
					if (last.second == Min) {
						++p[i];
						break ;
					}
				}
			}
		}
		cout << ans << endl;
	}
	return 0;
}