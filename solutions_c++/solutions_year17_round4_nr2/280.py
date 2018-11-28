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

int dupa[1005][1005];
int sum[1005];
int mam[1005];

void solve() {
	make3(n, c, m);
	FOR(i,1,c+1) FOR(j,1,n+1) dupa[i][j] = 0;
	FOR(i,0,m) {
		make2(p, x);
		dupa[x][p]++;
	}
	int ans = 0;
	int suma = 0;
	FOR(i,0,c+1) sum[i] = 0;

	FOR(i,1,n+1) {
		FOR(j,1,c+1) {
			suma += dupa[j][i];
			sum[j] += dupa[j][i];
			ans = max(ans, sum[j]);
		}
		ans = max(ans, (suma+(i-1))/i);
	}
	FOR(i,1,n+1) mam[i] = ans;
	int prom = 0;
	FOR(i,1,n+1) {
		FOR(j, 1, c+1) {
			int ile = min(mam[i], dupa[j][i]);
			dupa[j][i] -= ile;
			mam[i] -= ile;
			prom += dupa[j][i];
		}
	}
	printf("%d %d\n",ans, prom);
}


int main() {
	make(z);
	FOR(test,1,z+1) {
		printf("Case #%d: ", test);
		solve();
	}
}	
