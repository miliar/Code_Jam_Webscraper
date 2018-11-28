#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <cstring>
#include <map>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <bitset>
#define f first
#define s second
#define ll long long
#define ull unsigned long long
#define mp make_pair
#define pb push_back
#define vi vector <int>
#define ld long double
#define pii pair<int, int>
using namespace std;    
const int N = 110, mod = int(1e9)  + 7;
int T;

int n, e[N], s[N],q;
ll a[N][N];
long double d[N][N];

void solve(){
	scanf("%d%d",&n,&q);
	for(int i = 1; i <= n; i++){
		scanf("%d%d",&e[i], &s[i]);
	}
	for(int i = 1; i <= n; i++){
		for(int j = 1; j <= n; j++){
			scanf("%lld",&a[i][j]);
		}
	}
	for(int k = 1; k <= n; k++){
		for(int i = 1; i <= n; i++){
			for(int j = 1; j <= n; j++){
				if(a[i][k] != -1 && a[k][j] != -1){
					if(a[i][j] == -1) a[i][j] = a[i][k] + a[k][j];
					a[i][j] = min(a[i][j], a[i][k] + a[k][j]);
				}
			}
		}
	}
	for(int i = 1; i <= n; i++){
		for(int j = 1; j <= n; j++){
			if(a[i][j] <= e[i] && a[i][j] != -1){
				d[i][j] = (a[i][j] + 0.0) / s[i];
			}
			else{
				d[i][j] = 1e15;
			}
		}
	}
	for(int k = 1; k <= n; k++){
	    for(int i = 1; i <= n; i++){
			for(int j = 1; j <= n; j++){
				d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
			}
		}
	}
	while(q--){
		int u,v;
		scanf("%d%d",&u,&v);
		printf("%.12lf ", (double)d[u][v]);
	}
	printf("\n");

}

int main () {
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++){
		printf("Case #%d: ",tt);
		solve();
	}

return 0;
}