#include <bits/stdc++.h>
 
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define FORD(i, a, b) for(int i = (a); i >= (b); --i)
#define VAR(v, i) __typeof(i) v=(i)
#define FORE(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define all(v) (v).begin(),(v).end()
 
#define PII pair<int,int>
#define mp make_pair
#define st first
#define nd second
#define pb push_back
#define lint long long int
#define VI vector<int>
 
#define debug(x) {cerr <<#x <<" = " <<x <<endl; }
#define debug2(x,y) {cerr <<#x <<" = " <<x << ", "<<#y<<" = "<< y <<endl; } 
#define debug3(x,y,z) {cerr <<#x <<" = " <<x << ", "<<#y<<" = "<< y << ", " << #z << " = " << z <<endl; } 
#define debugv(x) {{cerr <<#x <<" = "; FORE(itt, (x)) cerr <<*itt <<", "; cerr <<endl; }}
#define debugt(t,n) {{cerr <<#t <<" = "; FOR(it,0,(n)) cerr <<t[it] <<", "; cerr <<endl; }}
 
#define make( x) int (x); scanf("%d",&(x));
#define make2( x, y) int (x), (y); scanf("%d%d",&(x),&(y));
#define make3(x, y, z) int (x), (y), (z); scanf("%d%d%d",&(x),&(y),&(z));
#define make4(x, y, z, t) int (x), (y), (z), (t); scanf("%d%d%d%d",&(x),&(y),&(z),&(t));
#define makev(v,n) VI (v); FOR(i,0,(n)) { make(a); (v).pb(a);} 
#define IOS ios_base::sync_with_stdio(0)
#define HEAP priority_queue
 
#define read( x) scanf("%d",&(x));
#define read2( x, y) scanf("%d%d",&(x),&(y));
#define read3(x, y, z) scanf("%d%d%d",&(x),&(y),&(z));
#define read4(x, y, z, t) scanf("%d%d%d%d",&(x),&(y),&(z),&(t));
#define readv(v,n) FOR(i,0,(n)) { make(a); (v).pb(a);}
#define jeb fflush(stdout)
 
 
using namespace std;
 
#define max_n 100015

int n;
int e[105];
int s[105];
lint d[105][105];
double dp[105][105][105];

void solve() {
	read(n);
	make(q);
	FOR(i,0,n) {
		make2(a, b); e[i] = a; s[i] = b;
	}
	FOR(i,0,n) FOR(j,0,n) {
		make(a); d[i][j] = a;
	}
	FOR(i,0,n) d[i][i] = 0;
	FOR(i,0,n) {
		FOR(j,0,n) {
			FOR(k,0,n) {
				if (d[j][i] == -1 || d[i][k] == -1) continue;
				if (d[j][k] == -1) d[j][k] = d[j][i] + d[i][k];
				if (d[j][i] + d[i][k] < d[j][k]) d[j][k] = d[j][i]+d[i][k];
			}
		}
	}
	FOR(i,0,n) FOR(j,0,n) FOR(k,0,n+1) dp[i][j][k] = -1;
	FOR(i,0,n) FOR(j,0,n) {
		if (d[i][j] <= e[i]) dp[i][j][0] = d[i][j]*1./s[i];
		else dp[i][j][0] = -1;
	}
	FOR(k,1,n+1) {
		FOR(i,0,n) FOR(j,0,n) dp[i][j][k] = dp[i][j][k-1];
		FOR(i,0,n) {
			FOR(j,0,n) {
				FOR(u,0,n) {
					if (d[i][u] > e[i] || d[i][u] == -1 || dp[u][j][k-1]==-1) continue;
					double pos = dp[u][j][k-1] + d[i][u]*1./s[i];
					if (dp[i][j][k] == -1) dp[i][j][k] = pos;
					else dp[i][j][k] = min(dp[i][j][k], pos);
				}
			}
		}
	}
	FOR(i,0,q) {
		make2(a,b);
		a--; b--;
		printf("%.10lf ", dp[a][b][n]);
	}
	printf("\n");
	

}


int main() {
	make(z);
	FOR(test,1,z+1) {
		printf("Case #%d: ", test);
		solve();
	}
}	
