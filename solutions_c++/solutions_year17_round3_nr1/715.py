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
const ld EPS=1e-12;
vector<pair<ld,ld> > p;

multiset<ld> se;

int main(){
	//ios::sync_with_stdio(false);
	//cin.tie(NULL);
	int t;
	int ca=0;
	cin>>t;
	while(t--){
		se.clear();
		ca++;
		int n;
		int k;
		cin>>n>>k;
		p.resize(0);
		ld x,y;
		rep(i,n){
			cin>>x>>y;
			p.pb(mp(x,y));
		}
		sort(p.begin(),p.end());
		multiset<ld> :: iterator it;
		ld ans=0;
		rep(i,n){
			//cout<<i<<" fd "<<endl;
			ld tmp=0;
			if((int)(se.size())>=k-1){
				int cnt=1;
				for(it=se.begin();cnt<k&&it!=se.end();it++,cnt++){
					tmp-=(*it);
					//cout<<cnt<<"dfvfd"<<endl;
				}
				tmp+=(p[i].X)*(p[i].X);
				tmp+=((ld)(2.0)*(p[i].X)*(p[i].Y));
				ans=max(ans,tmp);
			}
			se.insert(-(ld)(2.0)*(p[i].X)*(p[i].Y));
		}
		ans=ans*(ld)(acos(-1));
		cout<<"Case #"<<ca<<": "<<setprecision(18)<<ans<<endl;
	}
	return 0;
}

