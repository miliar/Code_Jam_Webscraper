#include <bits/stdc++.h>

using namespace std;
#define For(i,l,r) for (int i = l; i <= r; ++i) 
#define Cor(i,l,r) for (int i = l; i >= r; --i)

char A[55][55];
bool mark[55];
bool occupy[55];
int main() {
	int T; cin >> T;
	For(TK,1,T) {
		printf("Case #%d:\n", TK);
		int n, m;
		scanf("%d%d", &n, &m);
		For(i,1,n) scanf("%s", A[i] + 1);
		memset(mark, 0, sizeof mark);
		For(i,1,n) For(j,1,m) if (A[i][j] != '?') {
			mark[j] = true;
		}
		memset(occupy, 0, sizeof occupy);
		For(i,1,n) For(j,1,m) if (A[i][j] != '?') {
			Cor(x,i,1) Cor(y,j,1) {
				if (mark[y] && y < j) break ;
				if (A[x][y] == '?') A[x][y] = A[i][j];
				occupy[y] = true;
			}
		}
		For(i,1,n) For(j,1,m) {
			if (A[i][j] == '?') {
				if (occupy[j]) {
					A[i][j] = A[i - 1][j];
				} else {
					A[i][j] = A[i][j - 1];
				}
			}
		}
		For(i,1,n) puts(A[i] + 1);
	}
	return 0;
}