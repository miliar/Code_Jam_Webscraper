#include <bits/stdc++.h>
#define REP(i, a, b) for (int i = a; i <= b; ++i)
#define PER(i, a, b) for (int i = a; i >= b; --i)
#define RVC(i, S) for (int i = 0; i < S.size(); ++i)
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define debug(...) fprintf(stderr, __VA_ARGS__)
using namespace std;

typedef pair<int, int> pii;
typedef vector<int> VI;
typedef long long LL;

inline int read(){
	int x = 0, ch = getchar(), f = 1;
	while (!isdigit(ch)){if (ch == '-') f = -1; ch = getchar();}
	while (isdigit(ch)) x = x * 10 + ch - '0', ch = getchar();
	return x * f;
}

int n, m;
char cake[30][30];

void solve(){
	n = read(), m = read();
	REP(i, 1, n)
		scanf("%s", cake[i] + 1);
	REP(i, 1, n) REP(j, 1, m){
		if (isalpha(cake[i][j])){
			char c = cake[i][j];
			REP(k, 1, j - 1) cake[i][k] = c;
			
			REP(k, j + 1, m){
				if (isalpha(cake[i][k]))
					c = cake[i][k];
				cake[i][k] = c;
			}
			REP(k, 1, i - 1) REP(l, 1, m)
				cake[k][l] = cake[i][l];

			REP(k, i + 1, n){
				int fl = 0;
				REP(l, 1, m) if (isalpha(cake[k][l])){
					fl = cake[k][l]; break;
				}
				if (!fl){
					REP(l, 1, m)
						cake[k][l] = cake[k - 1][l];
				}
				else{
					REP(l, 1, m){
						if (isalpha(cake[k][l]))
							fl = cake[k][l];
						cake[k][l] = fl;
					}
				}
			}
			REP(k, 1, n){
				REP(l, 1, m){
					putchar(cake[k][l]);
				}
				putchar('\n');
			}
			return;
		}
	}
}

int main(){
	int T = read();
	REP(kas, 1, T){
		printf("Case #%d:\n", kas);
		solve();
	}
	return 0;
}