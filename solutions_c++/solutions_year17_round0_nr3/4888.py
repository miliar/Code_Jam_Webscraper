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
ll a[105][2];
ll ed[105][2];

ll lef, ri;


void solve(ll x,ll cx, ll cy,ll k){
	if(k<=cx){
		ri=(x/2LL);
		if(x%2LL == 1LL)lef=ri;
		else lef=ri-1;
		//lef = gl(x);
		//ri=gr(x);
		return;
	}else{
		k-=cx;
		if(k<=cy){
			//lef=gl(x-1);
			//ri=gr(x-1);
			ri=(x-1LL)/2LL;
			if(x%2LL == 0LL)lef=ri;
			else lef=ri-1;
			return;
		}else{
			k-=cy;
		}
	}
	ll tcx=0;
	ll tcy=0;
	ll ma=0;
	if(x%4==0){
		ma=x/2LL;
		tcx+=cx;
		tcy+=cx;
		tcy+=2LL*cy;
	}else if(x%4 == 1){
		ma=x/2LL;
		tcx+=2LL*cx;
		tcx+=cy;
		tcy+=cy;
	}else if(x%4 == 2){
		ma=x/2LL;
		tcx+=cx;
		tcy+=cx;
		tcy+=2LL*cy;
	}else{
		ma=x/2LL;
		tcx+=2LL*cx;
		tcx+=cy;
		tcy+=cy;
	}
	solve(ma,tcx,tcy,k);
}

int main(){
	//ios::sync_with_stdio(false);
	//cin.tie(NULL);
	int t;
	cin>>t;
	ll n,k;
	int ca=0;
	while(t--){
		cin>>n>>k;
		if(n==1){
			ca++;
			cout<<"Case #"<<ca<<": 0 0"<<endl;
			continue;
		}
		solve(n,1LL,0LL,k);
		ca++;
		cout<<"Case #"<<ca<<": "<<ri<<" "<<lef<<endl;
	}
	return 0;
}

