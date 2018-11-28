#include <bits/stdc++.h>
using namespace std;
typedef long long				ll;
typedef pair<int,int >			pii;
#define V						vector
#define SYNC					ios_base::sync_with_stdio(0);cin.tie(0);
#define rep(i,b)				for(int i=0;i<b;i++)
#define repn(i,n)				for(int i=1;i<=n;i++)
#define ALL(x)					(x).begin(),(x).end()
#define fi						first
#define se						second
#define pb						push_back
#define dzx						cerr<<"here";
const ll MOD=1e9+7,INF=9e18;
const int inf=2e8;
/* cent π */
int g;
int fre[10];
int main(){SYNC
	int T;
	cin>>T;
	int y=0;
	repn(tc,T){
		int ans=0;
		memset(fre,0,sizeof fre);
		cout<<"Case #"<<tc<<": ";
		int n,p;
		cin>>n>>p;
		rep(i,n){
			cin>>g;
			fre[g%p]++;
		}
		ans+=fre[0];
		if(p==2){
			ans+=(fre[1]+1)/2;
		}
		else if(p==3){
			if(fre[1]>fre[2])
				swap(fre[1],fre[2]);
			
			int t=min(fre[2],fre[1]+1);
			ans+=t;
			fre[2]-=t;
			ans+=fre[2]/3;
		}
		cout<<ans;
		cout<<"\n";
	}
	return 0;
}