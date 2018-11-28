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
int a[100];

bool check(int x){
	rep(i,20){
		a[i]=0;
	}
	rep(i,20){
		if(x == 0)break;
		a[i]=x%10;
		x/=10;
	}
	repp(i,1,20){
		if(a[i]>a[i-1])return false;
	}
	return true;
}

int main(){
	//ios::sync_with_stdio(false);
	//cin.tie(NULL);
	int t;
	cin>>t;
	int ca=0;
	while(t--){
		ca++;
		cout<<"Case #"<<ca<<": ";
		int n;
		cin>>n;
		int ans=0;
		rep(i,n+1){
			if(check(i)){
				ans=max(ans,i);
			}
		}
		cout<<ans<<endl;
	}
	return 0;
}

