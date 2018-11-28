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

vector <string> adj;
int main(){
	//ios::sync_with_stdio(false);
	//cin.tie(NULL);
	int t;
	cin>>t;
	int n;
	int ca=0;
	int r,o,y,g,b,v;
	while(t--){
		ca++;
		cin>>n>>r>>o>>y>>g>>b>>v;
		adj.resize(0);
		cout<<"Case #"<<ca<<": ";
		if(r>=y && r>= b){
			if(r>n/2){
				cout<<"IMPOSSIBLE"<<endl;
				continue;
			}
			rep(i,r){
				adj.pb("R");
			}
			rep(i,y){
				adj[i]="YR";
			}
			repp(i,y,r){
				adj[i]="BR";
			}
			int dif=y+b-r;
			rep(i,dif){
				adj[i]="YBR";
			}
		}else if(y>=r && y>=b){
			if(y>n/2){
				cout<<"IMPOSSIBLE"<<endl;
				continue;
			}
			rep(i,y){
				adj.pb("Y");
			}
			rep(i,r){
				adj[i]="RY";
			}
			repp(i,r,y){
				adj[i]="BY";
			}
			int dif=r+b-y;
			rep(i,dif){
				adj[i]="BRY";
			}
		}else{
			if(b>n/2){
				cout<<"IMPOSSIBLE"<<endl;
				continue;
			}
			rep(i,b){
				adj.pb("B");
			}
			rep(i,y){
				adj[i]="YB";
			}
			repp(i,y,b){
				adj[i]="RB";
			}
			int dif=y+r-b;
			rep(i,dif){
				adj[i]="YRB";
			}
		}
		rep(i,adj.size()){
			cout<<adj[i];
		}cout<<endl;
	}
	return 0;
}

