#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define MS(a) memset(a,0,sizeof(a))
#define MP make_pair
#define PB push_back
const int INF = 0x3f3f3f3f;
const ll INFLL = 0x3f3f3f3f3f3f3f3fLL;
inline ll read(){
    ll x=0,f=1;char ch=getchar();
    while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=getchar();}
    while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}
    return x*f;
}
//////////////////////////////////////////////////////////////////////////
const int maxn = 1e5+10;

double pi = acos(-1);

struct node{
	double r,h;
	bool operator<(const node& rhs) const{
		return r > rhs.r;
	}
}a[1005];
double dp[1005][1005];
int id[1005];

int main(){
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);
	int T = read();
	for(int cas=1; cas<=T; cas++){
		int n,k; cin>>n>>k;

		for(int i=1; i<=n; i++){
			cin >> a[i].r >> a[i].h;
		}
		sort(a+1,a+n+1);

		id[1] = 1;
		for(int i=1; i<=n; i++){
			if(pi*a[i].r*a[i].r+2*pi*a[i].r*a[i].h > pi*a[id[i-1]].r*a[id[i-1]].r+2*pi*a[id[i-1]].r*a[id[i-1]].h){
				id[i] = i;
			}else{
				id[i] = id[i-1];
			}
		}

		memset(dp,0,sizeof(dp));
		for(int i=1; i<=n; i++){
			dp[i][1] = pi*a[id[i]].r*a[id[i]].r+2*pi*a[id[i]].r*a[id[i]].h;
		}
		for(int i=2; i<=n; i++){
			for(int j=2; j<=k; j++){
				dp[i][j] = max(dp[i-1][j],dp[i-1][j-1]+2*pi*a[i].r*a[i].h);
			}
		}

		printf("Case #%d: %.6lf\n",cas,dp[n][k]);
	}

    return 0;
}