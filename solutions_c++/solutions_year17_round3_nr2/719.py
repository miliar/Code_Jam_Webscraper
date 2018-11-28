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
vector<pair<pii, int> > vec;
multiset<int> se[3];

int net[10];
int tmp;
int main(){
	//ios::sync_with_stdio(false);
	//cin.tie(NULL);
	int t;
	int ca=0;
	cin>>t;
	while(t--){
		ca++;
		net[0]=net[1]=0;
		se[0].clear();
		se[1].clear();
		se[2].clear();
		vec.resize(0);
		tmp=0;
		int n,m;
		cin>>n>>m;
		int p,q;
		rep(i,n){
			cin>>p>>q;
			vec.pb(mp(mp(p,q),1));
		}
		rep(i,m){
			cin>>p>>q;
			vec.pb(mp(mp(p,q),0));
		}
		sort(vec.begin(),vec.end());
		int cur=2;
		int ans=0;
		int flag=0;
		rep(i,vec.size()){
			if(cur==vec[i].Y){
				if(i!=0){
					net[cur]+=vec[i].X.X-vec[i-1].X.Y;
					se[cur].insert(-vec[i].X.X+vec[i-1].X.Y);
				}
			}else{
				if(i!=0){
					ans++;
					//se[2].insert(-ve[i].X.X+vec[i-1].X.Y);
					tmp+=vec[i].X.X-vec[i-1].X.Y;
				}
			}
			if(i==(int)(vec.size())-1){
				if(vec[0].Y == vec[i].Y){
					int xp=24*60-vec[i].X.Y;
					xp+=vec[0].X.X;
					se[vec[i].Y].insert(-xp);
					net[vec[i].Y]+=24*60-vec[i].X.Y;
					net[vec[i].Y]+=vec[0].X.X;
				}else{
					ans++;
					tmp+=24*60-vec[i].X.Y;
					tmp+=vec[0].X.X;
				}
			}
			cur=vec[i].Y;
			net[cur]+=vec[i].X.Y-vec[i].X.X;
		}
		if(net[cur]>720){
			cur^=1;
		}
		//cout<<ans<<endl;
		if(net[cur]+tmp<720){
			net[cur]+=tmp;
			int idx=cur^1;
			multiset<int>::iterator it;
			for(it=se[idx].begin();it!=se[idx].end();it++){
				net[cur]-=(*it);
				//cout<<net[cur]<<" "<<cur<<endl;
				ans+=2;
				if(net[cur]>=720)break;
			}
			if(net[cur]<720)ans+=2;
		}
		if(vec.size()==1){
			if(ans!=2){
				//return 0;
				//cout<<"WTF"<<endl;
			}
			ans=2;
		}
		if(n==1&&m==1){
			ans=2;
			//if(ans!=2){
				//cout<<"WTF"<<endl;
				//return 0;
			//}
		}
		//cout<<n<<" "<<m<<endl;
		cout<<"Case #"<<ca<<": "<<ans<<endl;
		//cout<<tmp<<endl;
	}
	return 0;
}

