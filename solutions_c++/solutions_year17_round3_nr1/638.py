#include <bits/stdc++.h>
using namespace std;

typedef int ll;

#define int long long
#define ff first
#define ss second
#define pb push_back
#define mp make_pair
#define sz(x) ((int)x.size())
#define all(x) x.begin(),x.end()

typedef pair<int,int>pii;
typedef pair<int,pair<int,int> > piii;

const int mod=1e9+7;

int POWER[65];
long double pi=3.14159265358979323846264338327950288419716939937510582097;
int power(int a, int b) {int ret=1;while(b) {if(b&1) ret*=a;a*=a;if(ret>=mod) ret%=mod;if(a>=mod) a%=mod;b>>=1;}return ret;}
int inv(int x) {return power(x,mod-2);}

void precompute() {
	POWER[0]=1;
	for(int i=1;i<63;i++) POWER[i]=POWER[i-1]<<1LL;
}

vector<pii>v;

bool cmp1(pii a , pii b) {
	if(a.ff>b.ff)
		return 1;
	if(a.ff==b.ff) {
		if(a.ss>b.ss)
			return 1;
	}

	return 0;
}

bool cmp2(pii a , pii b) {
	int x=a.ff*a.ss,y=b.ff*b.ss;
	if(x>y)
		return 1;
	return 0;
}

int DP[1005][1005],n,k;
int go(int curr , int lef) {
	if(lef==0) {
		return 0;
	}
	if(curr==n) {
		return -2;
	}

	if(DP[curr][lef]!=-1)
		return DP[curr][lef];

	int ret=go(curr+1,lef-1);
	if(ret!=-2)	{
		ret=ret+(2*v[curr].ff*v[curr].ss);
		if(lef==k) {
			ret+=(v[curr].ff*v[curr].ff);
		}
	}
	ret=max(ret,go(curr+1,lef));
	DP[curr][lef]=ret;
	return ret;
}

ll main() {
	freopen("Task.in","r",stdin);freopen("Task1.out","w",stdout);
	int t,cc=0;
	cin>>t;
	while (t--) {
		v.clear();
		memset(DP,-1,sizeof(DP));
		cin>>n>>k;

		for (int i=0 ; i<n ; i++) {
			int r,h;
			cin>>r>>h;

			v.pb(mp(r,h));
		}
		sort(v.begin(),v.end(),cmp1);
		int ret=go(0,k);

		long double ans=(long double)ret*pi;
		cc++;
		cout<<"Case #"<<cc<<": "<<setprecision(10)<<fixed<<ans<<endl;
	}	
}