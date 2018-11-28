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

char arr[1005];

void solve(){
	ss(arr);
	int k;sd(k);
	
	int l=strlen(arr);
	
	int i,ans=0;
	for(i=0;i+k-1<l;i++){
		if(arr[i]=='-'){
			ans++;
			for(int j=i;j<=i+k-1;j++) arr[j]=(arr[j]=='+')?'-':'+';
		}
	}
	
	for(;i<l;i++){
		if(arr[i]=='-'){
			printf("IMPOSSIBLE\n");
			return;
		}
	}
	
	pd(ans);
}

#define adkro

int main(){

#ifdef adkroxx
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
#endif
	
	int t;sd(t);	
	for(int tt=1;tt<=t;tt++){
		printf("Case #%d: ",tt);
		solve();
	}
}
