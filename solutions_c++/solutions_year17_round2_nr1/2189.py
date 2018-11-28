#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000007
#define pii pair<int, int>
#define pll pair<long long, long long>
#define V  vector
#define pb  push_back
#define mp  make_pair
#define pq priority_queue
#define FIN(x) freopen(x,"r",stdin)
#define FOUT(x) freopen(x,"w",stdout)
#define ALL(x) x.begin(),x.end()
#define M(a,x) memset(a,x,sizeof(a))
#define S(x) scanf("%d",&x)
#define Sl(x) scanf("%lld",&x)
#define scs(x) scanf("%s",x);
#define SZ(x) (int)x.size()
#define print(x) printf("%d",x);
#define nl printf("\n")
#define fr first
#define se second
#define printl(x) printf("%lld",x)
#define F(i,a,n) for(int i=a;i<n;i++)
#define INF 4000000000000000000LL
#define LL long long

int n;
double d;
double K[10000];
double s[10000];
int cs = 0;
int main() {
	int t;
	S(t);
	while(t--){
		cin >> d >> n;
		double mx = -1e9;
		for(int i = 0 ; i < n ; i++){
			cin >> K[i] >> s[i];
			mx = max(mx,(d-K[i])/s[i]);
		}
		double ans = d/mx;
	  printf("Case #%d: %.17lf\n",++cs,ans);
	}
}