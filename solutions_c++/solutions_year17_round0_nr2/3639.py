#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pdd pair<double,double>
#define X first
#define Y second
#define REP(i,a) for(int i=0;i<a;++i)
#define REPP(i,a,b) for(int i=a;i<b;++i)
#define FILL(a,x) memset(a,x,sizeof(a))
#define foreach( gg,itit )  for( typeof(gg.begin()) itit=gg.begin();itit!=gg.end();itit++ )
#define mp make_pair
#define pb push_back
#define all(s) s.begin(),s.end()
#define sz(s) (int)s.size()
#define present(c,x) ((c).find(x) != (c).end())
const double EPS = 1e-8;
const int mod = 1e9+7;
const int N = 1e3+10;
const ll INF = 1e18;

ll power(ll x,ll y){
	ll t=1;
	while(y>0){
		if(y%2) y-=1,t=t*x%mod;
		else y/=2,x=x*x%mod;
	}
return t;
}

char s[N],ans[N];
int n;

bool solve(int idx, bool check){
	if (idx==n){
		ans[n]='\0';
		return true;
	}
	int x=0;
	if (idx) x=ans[idx-1]-'0'; 
	if (!check){
		for(int i=9;i>=max(1,x);i--){
			ans[idx]=i+'0';
			bool tmp=solve(idx+1,0);
			if (tmp) return true;
		}
	}
	else{
		for(int i=s[idx]-'0';i>=max(1,x);i--){
			ans[idx]=i+'0';
			bool tmp;
			if (i!=s[idx]-'0') tmp=solve(idx+1,0);
			else tmp=solve(idx+1,1);
			if (tmp) return true;
		}
	}
	return false;
}

int main(){
	int t;
	scanf("%d",&t);
	REP(kase,t){
		scanf("%s",s);
		n=strlen(s);
		bool x=solve(0,1);
		if (!x){
			REP(i,n-1) ans[i]='9';
			ans[n-1]='\0';
		}
		printf("Case #%d: %s\n",kase+1,ans);
	}
	return 0;
}