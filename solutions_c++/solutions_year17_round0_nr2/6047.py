#include<bits/stdc++.h>

#define MOD 1000000007
#define MAX 100005
#define ll long long
#define slld(t) scanf("%lld",&t)
#define sd(t) scanf("%d",&t)
#define ss(x) scanf("%s",x)
#define pd(t) printf("%d\n",t)
#define plld(t) printf("%lld\n",t)
#define pii pair<int,int>
#define pll pair<ll,ll>
#define tr(container,it) for(typeof(container.begin()) it=container.begin();it!=container.end();it++)
#define mp(a,b) make_pair(a,b)
#define FF first
#define SS second
#define pb(x) push_back(x)
#define vi vector<int>
#define vpii vector<pii >
#define vll vector<ll>
#define clr(x) memset(x,0,sizeof(x))

using namespace std;

void solve(){
	ll n;slld(n);
	ll dig[20];
	int cur=0;
	ll tn=n;
	while(tn){
		dig[cur++]=tn%10;
		tn/=10;
	}
	ll final[20];
	for(int i=cur-1;i>=0;i--){
		ll already=0;
		ll goingto=0;
		for(int j=i-1;j>=0;j--){
			already=already*10+dig[j];
			goingto=goingto*10+dig[i];
		}
		if(goingto<=already){
			final[i]=dig[i];
		}else{
			final[i]=dig[i]-1;
			for(int j=i-1;j>=0;j--) final[j]=9;
			break;
		}
	}
	ll ans=0;
	for(int i=cur-1;i>=0;i--) ans=ans*10+final[i];
	plld(ans);
}

#define adkro

int main(){

#ifdef adkroxx
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
#endif
	
	int t;sd(t);	
	for(int tt=1;tt<=t;tt++){
		printf("Case #%d: ",tt);
		solve();
	}
}
