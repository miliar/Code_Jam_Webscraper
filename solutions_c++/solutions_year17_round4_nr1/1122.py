#include <bits/stdc++.h>
#define fr(a,b,c) for(int a=b,_=c;a<_;a++)
#define rp(a,b) for(int a=0,_=b;a<_;a++)
#define X first
#define Y second
#define pb push_back
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<ll,ll> pll;
vector<int> v;
int solve(int p){
	vector<int> res;
	fr(i,0,p)res.pb(0);
	for(auto k:v)res[k%p]++;
	if(p==2){
		return res[0]+(res[1]+1)/2;
	}if(p==3){
		int ret=res[0];
		if(res[1]>res[2]){
			res[1]-=res[2];
			ret+=res[2];
			ret+=(res[1]+2)/3;
		}else{
			res[2]-=res[1];
			ret+=res[1];
			ret+=(res[2]+2)/3;
		}
		return ret;
	}if(p==4){
		int ret=res[0];
		ret+=res[2]/2;
		res[2]&=1;
		ret+=min(res[1],res[3]);
		int x=min(res[1],res[3]);
		res[1]-=x;
		res[3]-=x;
		ret+=res[1]/4;
		res[1]%=4;
		ret+=res[3]/4;
		res[3]%=4;
		if(res[1]+res[2]*2==4){ret++;res[1]-=2;res[2]--;}
		if(res[3]+res[2]*2==8){ret++;res[1]-=2;res[2]--;}
		if(res[1]+res[2]+res[3])ret++;
		return ret;
	}
}
	
int main(){
	int t;scanf("%d",&t);
	fr(T,0,t){
		int p,n;scanf("%d%d",&n,&p);
		v.clear();
		fr(i,0,n){
			int a;
			scanf("%d",&a);
			v.pb(a);
		}
		int ans=solve(p);
		printf("Case #%d: %d\n",T+1,ans);
	}
}
