#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pdd pair<double,double>
#define X first
#define Y second
#define rep(i,a) for(int i=0;i<(int)a;i++)
#define repp(i,a,b) for(int i=(int)a;i<(int)b;i++)
#define fill(a,x) memset(a,x,sizeof(a))
#define foreach( gg, itit) for( typeof(gg.begin()) itit=gg.begin();itit!=gg.end();itit++ )
#define mp make_pair
#define pb push_back
#define all(s) s.begin(),s.end()
#define present(c,x) ((c).find(x) != (c).end())
const int mod  = 1e9+7;
const int N = 1e6+10;

#define ld long double
const ld INF = 1e18;
//#define double long double
const ld EPS=1e-12;

ld e[1005];
ld v[1005];
ld dp[1005];

ld dist[1005];
ld pre[1005];

int main(){
	//ios::sync_with_stdio(false);
	//cin.tie(NULL);
	int t;
	cin>>t;
	int ca=0;
	int n,q;
	while(t--){
		cin>>n>>q;
		ca++;
		cout<<"Case #"<<ca<<": ";
		rep(i,n){
			cin>>e[i]>>v[i];
		}
		rep(i,n){
			rep(j,n){
				ld x;
				cin>>x;
				if(x != -1){
					dist[i]=x;
				}
			}
		}
		pre[0]=0;
		repp(i,1,n){
			pre[i]=pre[i-1]+dist[i-1];
		}
		int u,v_;
		rep(i,q){
			cin>>u>>v_;
		}
		dp[0]=0;
		repp(i,1,n){
			dp[i]=INF;
			rep(j,i){
				ll di=(pre[i]-pre[j]);
				if(di>e[j])continue;
				ld tim=(di)/(v[j]);
				dp[i]=min(dp[i],dp[j]+tim);
			}
		}
		cout<<setprecision(18)<<dp[n-1]<<endl;
	}
	return 0;
}

