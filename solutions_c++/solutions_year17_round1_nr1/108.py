#include<bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define x first
#define y second
#define sz(a) ((int)(a).size())
#define rep(i, a, b) for(int (i) = (a); (i) < (b); (i)++)
#define dec(i, a, b) for (int (i) = (a); (i) >= (b); (i)--)
#define clr(a,v) memset(a, v, sizeof(a))
#define all(a) (a).begin(),(a).end()
#define MAXN 303030
#define LOGN 20
#define EPS 1e-5
#define fcin ios_base::sync_with_stdio(false)
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

char grid[26][26], ruim[26];

int main(){
	//freopen("bipartite.in","r",stdin);
	//freopen("bipartite.out","w",stdout);
	int t;
	scanf("%d", &t);
	rep(caso,1,t+1){
		int n, m;
		scanf("%d%d", &n, &m);
		rep(i,0,n) scanf("%s", grid[i]);
		clr(ruim,0);
		rep(i,0,n){
			int ini = -1;
			rep(j,0,m) if(grid[i][j] != '?'){ ini = j; break; }
			if(ini==-1) ruim[i]=1;
			else{
				rep(j,0,m){
					if(grid[i][j] == '?') grid[i][j] = grid[i][ini];
					else ini = j;
				}
			}
		}
		while(1){
			int pa=-1, pb=-1;
			rep(i,0,n) if(ruim[i]){
				if(i && !ruim[i-1]){ pb=i-1, pa=i; break; }
				if(i+1 < n && !ruim[i+1]){ pb=i+1, pa=i; break; }
			}
			if(pa == -1) break;
			ruim[pa]=0;
			rep(j,0,m) grid[pa][j] = grid[pb][j];
		}
		printf("Case #%d:\n", caso);
		rep(i,0,n) printf("%s\n", grid[i]);
	}
}

