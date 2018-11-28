#include <bits/stdc++.h> // PLEASE

using namespace std;
typedef long long ll;
typedef pair <int, int> pp;
typedef pair <pp, pp> p;
#define MAXN 30
#define MAXM 1005
#define MAXP 25
#define INF 2000000000
#define HAX 10000000 
#define A first
#define B second
#define MP make_pair
#define PB push_back
#define FOR(i, a, b) for(int i =(a); i <=(b); ++i)
#define re(i, n) FOR(i, 1, n)
#define rep(i, n) for(int i = 0; i<(n); ++i)
#define fore(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
int R, C;
char ar[MAXN][MAXN];

bool chk(char c)
{
	int minx = INF;
	int maxx = 0;
	int miny = INF;
	int maxy = 0;
	for(int i=1; i<=R; i++) {
		for(int j=1; j<=C; j++) {
			if(ar[i][j] == c) {
				minx = min(minx, i);
				maxx = max(maxx, i);
				miny = min(miny, j);
				maxy = max(maxy, j);
			}
		}
	}
	for(int i=minx; i<=maxx; i++) {
		for(int j=miny; j<=maxy; j++) {
			if(ar[i][j] == c) continue;
			if(ar[i][j] == '?') continue;
			return false;
		}
	}
	return true;
}

void go(int a, int b, char c)
{
	if(ar[a][b] != '?') return;
	ar[a][b] = c;
	if(!chk(c)) {
		ar[a][b] = '?';
		return;
	}
	if(b>1) go(a, b-1, c);
	if(b<C) go(a, b+1, c);
}
int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int T;
	cin >> T;
	for(int t=1; t<=T; t++) {
		string s;
		cin >> R >> C;
		for(int i=1; i<=R; i++) {
			cin >> s;
			for(int j=1; j<=C; j++) ar[i][j] = (char)s[j-1];
		}
		for(int i=1; i<=R; i++) {
			for(int j=1; j<=C; j++) {
				if(ar[i][j] == '?') continue;
				if(j>1) go(i, j-1, ar[i][j]);
				if(j<C) go(i, j+1, ar[i][j]);
			}
		}
		for(int i=1; i<=R; i++) {
			if(ar[i][1] == '?') {
				for(int j=i-1; j>=1; j--) {
					if(ar[j][1] != '?') {
						for(int k=1; k<=C; k++) ar[i][k] = ar[j][k];
						break;
					}
				}
			}
			if(ar[i][1] == '?') {
				for(int j=i+1; j<=R; j++) {
					if(ar[j][1] != '?') {
						for(int k=1; k<=C; k++) ar[i][k] = ar[j][k];
						break;
					}
				}
			}
		}
		printf("Case #%d:\n", t);
		for(int i=1; i<=R; i++) {
			for(int j=1; j<=C; j++) printf("%c", ar[i][j]);
			printf("\n");
		}
	}
   
}
