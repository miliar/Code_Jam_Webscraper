#include <bits/stdc++.h>

using namespace std;

#define fr(a,b,c) for(int (a) = (b); (a) < (c); ++(a))
#define rp(a,b) fr(a,0,b)
#define fre(a,b) for(int a = adj[b]; ~a; a = ant[a])
#define cl(a,b) memset((a), (b), sizeof(a))
#define sc(a) scanf("%d", &a)
#define sc2(a,b) scanf("%d%d", &a, &b)
#define sc3(a,b,c) scanf("%d%d%d", &a, &b, &c)
#define scs(s) scanf("%s", s)
#define pri(x) printf("%d\n", x)

#define iter(a) __typeof((a).begin())
#define fore(a,b) for(iter(b) a = (b).begin(); a != (b).end(); ++a)

#define st first
#define nd second
#define mp make_pair
#define pb push_back

#define db(x) cerr << #x << " == " << x << endl
#define dbs(x) cerr << x << endl
#define _ << ", " <<

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector< vi > vii;

const int oo = 0x3f3f3f3f;

#define N 29

int m, n;
char grid[N][N];

int main() {
	int t, cn = 1; sc(t);
	while (t--) {
		sc2(m, n);
		rp(i, m) scs(grid[i]);
		
		rp(i, m) {
			int st = -1;
			rp(j, n) if (grid[i][j] != '?') {
				st = grid[i][j];
				break;
			}
			
			if (st != -1) {
				rp(j, n) if (grid[i][j] == '?')
					grid[i][j] = st;
				else st = grid[i][j];
			}
		}
		
		rp(i, m) {
			int st = -1;
			rp(j, n) if (grid[i][j] != '?') {
				st = grid[i][j];
				break;
			}
			
			if (st == -1 && i > 0) {
				rp(j, n) grid[i][j] = grid[i-1][j];
			}
		}
		rp(ii, m) {
			int i = m-ii-1;
			int st = -1;
			rp(j, n) if (grid[i][j] != '?') {
				st = grid[i][j];
				break;
			}
			
			if (st == -1 && ii > 0) {
				rp(j, n) grid[i][j] = grid[i+1][j];
			}
		}
		
		printf("Case #%d:\n", cn++);
		rp(i, m) puts(grid[i]);
	}
	return 0;
}




































