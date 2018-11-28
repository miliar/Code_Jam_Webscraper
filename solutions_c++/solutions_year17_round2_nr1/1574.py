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
const ll INF = 1e18;

#define ld long double
//#define double long double
const ld EPS=1e-7;

vector <pair<ld,ld> > adj;
int main(){
	//ios::sync_with_stdio(false);
	//cin.tie(NULL);
	int t;
	cin>>t;
	int ca=0;
	int n;
	ld d;
	while(t--){
		adj.resize(0);
		ca++;
		cin>>d>>n;
		ld p,q;
		rep(i,n){
			//cin>>s[i]>>v[i];
			cin>>p>>q;
			adj.pb(mp(p,q));
		}
		sort(adj.begin(),adj.end());
		int l=0;
		repp(i,1,n){
			if(adj[i].Y > adj[l].Y)continue;
			ld ti=((ld)(1.0))*(adj[i].X-adj[l].X)/(adj[l].Y-adj[i].Y);
			ld di=adj[i].X+adj[l].Y*ti;
			if(di>=d+EPS){
				continue;
			}else{
				l=i;
			}
		}
		ld tim=(d-adj[l].X)/adj[l].Y;
		ld velo=d/tim;
		cout<<"Case #"<<ca<<": ";
		cout<<setprecision(16)<<velo<<endl;
	}
	return 0;
}

