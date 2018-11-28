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

int a[105];
int b[4];

int main(){
	//ios::sync_with_stdio(false);
	//cin.tie(NULL);
	int t;
	cin>>t;
	int ca=0;
	while(t--){
		ca++;
		int n,p;
		rep(i,4){
			b[i]=0;
		}
		cin>>n>>p;
		rep(i,n){
			cin>>a[i];
		}
		rep(i,n){
			b[a[i]%p]++;
		}
		int ans=0;
		if(p==2){
			ans+=b[0];
			ans+=(b[1]/2);
			b[1]%=2;
			if(b[1] == 1){
				ans++;
			}
		}else if(p==3){
			ans+=b[0];
			int x=max(b[1],b[2]);
			int y=min(b[1],b[2]);
			ans+=y;
			x-=y;
			ans+=(x/3);
			if(x%3 > 0){
				ans++;
			}
		}else{
			ans+=b[0];
			int x=max(b[1],b[3]);
			int y=min(b[1],b[3]);
			int z=b[2];
			ans+=y;
			x-=y;
			ans+=z/2;
			z%=2;
			ans+=x/4;
			x%=4;
			if(z==0){
				if(x>0){
					ans++;
				}
			}else{
				if(x==3){
					ans+=2;
				}else{
					ans++;
				}
			}
		}
		cout<<"Case #"<<ca<<": "<<ans<<endl;
	}
	return 0;
}

