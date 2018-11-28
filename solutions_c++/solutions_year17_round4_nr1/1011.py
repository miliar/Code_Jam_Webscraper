#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> pp;
typedef pair<ll,ll> pll;
void read(int& x){ scanf("%d",&x); }
void read(ll& x){ scanf("%lld",&x); }
template<typename T,typename... Args>
void read(T& a,Args&... b){ read(a); read(b...); }
#define all(x) (x).begin(),(x).end()
#define pb push_back
#define x first
#define y second

int n;
int g[110];
int p;

void work(){
	read(n, p);
	for(int i=1; i<=n; ++i) read(g[i]);
	if(p == 2){
		int od=0, ev=0;
		for(int i=1; i<=n; ++i){
			((g[i]&1)?od:ev)++;
		}
		printf("%d\n", ev + (od+1)/2);
	} else if(p == 3){
		int c[3]={0,0,0};
		for(int i=1; i<=n; ++i) c[g[i]%3]++;
		int mx=c[1], mn=c[2];
		if(mx<mn) swap(mx, mn);
		int ans = c[0] + mn + (mx-mn+2)/3;
		printf("%d\n", ans);
	} else {
		int c[4]={0,0,0,0};
		for(int i=1; i<=n; ++i) c[g[i]%4]++;
		int ans = c[0];
		for(int x=0; x<=100; ++x){
			for(int y=0; y<=100; ++y){
				for(int z=0; z<=100; ++z){
					int la = c[1]-x-2*y;
					int lb = c[2]-y-z;
					int lc = c[3]-x-2*z;
					if(la>=0 && lb>=0 && lc>=0){
						ans = max(ans, c[0] + x+y+z + la/4 + lb/2 + lc/4 + !!(la%4+lb%2+lc%4));
					} else break;
				}
			}
		}
		printf("%d\n", ans);
	}
}

#define CASE "large"

int main()
{
	freopen(CASE ".in", "r", stdin);
	freopen(CASE ".out", "w", stdout);
	int tc; read(tc);
	for(int i=1; i<=tc; ++i){
		printf("Case #%d: ", i);
		work();
	}
    return 0;
}
