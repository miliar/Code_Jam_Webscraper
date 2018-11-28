#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define sz(x) ((int)x.size())
#define clr(a,b) memset(a,b,sizeof(a))
typedef long long ll;
const int maxn=1e3+7;
const int INF=1e9+7;
int n,m,T;
string s;
int len;
int num[20];

bool F;
bool dfs(int i,int pre){
	if(i==len)return true;
	int v=num[i];
	if(F)v=9;
	if(v<pre)return false;
	bool fg=dfs(i+1,v);
	if(fg){
		num[i]=v;
		return true;
	}
	if(v>pre){
		F=true;
		fg=dfs(i+1,v-1);
		if(fg){
			num[i]=v-1;
			return true;
		}
		F=false;
	}
	return false;
}
void solve(){
	len=s.length();
	F=false;
	for(int i=0;i<len;i++)num[i]=s[i]-'0';
	dfs(0,-1);
	ll p=1;
	ll ans=0;
	for(int i=len-1;i>=0;i--){
		if(num[i]==-1)num[i]=9;
		ans+=num[i]*p;
		p*=10;
	}
	cout<<ans<<endl;
}
int main(){
#ifdef AC
freopen("data.in","r",stdin);
freopen("data.out","w",stdout);
#endif
	cin>>T;
	for(int tc=1;tc<=T;tc++){
		printf("Case #%d: ",tc);
		cin>>s;
		solve();
	}
	return 0;
}

