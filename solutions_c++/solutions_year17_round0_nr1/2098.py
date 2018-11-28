#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define sz(x) ((int)x.size())
#define clr(a,b) memset(a,b,sizeof(a))
typedef long long ll;
const int maxn=1e3+7;
const int INF=1e9+7;
int n,m,t;
int a[maxn];
string s;
int k;
bool vis[maxn];
void solve(){
	int len=s.length();
	for(int i=0;i<len;i++){
		if(s[i]=='-')a[i]=0;
		else a[i]=1;
	}
	bool flag=true;
	int ans=0,qwe=0;
	for(int i=0;i<=len-k;i++){
		if(i>=k)qwe^=vis[i-k];
		if(a[i]^qwe)vis[i]=0;
		else vis[i]=1,ans++;
		qwe^=vis[i];
	}
	for(int i=len-k+1;i<len;i++){
		if(i>=k)qwe^=vis[i-k];
		if(a[i]^qwe)continue;
		else flag=false;
	}
	if(!flag)puts("IMPOSSIBLE");
	else printf("%d\n",ans);
}
int main(){
#ifdef AC
freopen("data.in","r",stdin);
freopen("data.out","w",stdout);
#endif
	cin>>n;
	
	for(int i=1;i<=n;i++){
		printf("Case #%d: ",i);
		cin>>s>>k;
		solve();
	}
	return 0;
}

