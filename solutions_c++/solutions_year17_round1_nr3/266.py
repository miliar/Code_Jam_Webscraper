#include<bits/stdc++.h>
using namespace std;

#define scl(x) scanf("%lld",&x)
#define sc(x)  scanf("%d",&x)
#define ll long long
#define lop(i,n) for(int i=0;i<n;++i)
typedef pair<int, int> ii;
typedef pair<ll, ll> pll;

int B,D,t,mxHd;
int memo[102][102][102][102];
int solve(int Hd,int Ad,int Hk,int Ak){
	if(Hk<=0)return 0;
	if(Hd<=0)return 1e9;
	int &ret=memo[Hd][Ad][Hk][Ak];
	if(~ret)return ret;
	ret=solve(Hd-Ak,Ad,Hk-Ad,Ak)+1;
	if(Ad<Hk&&B){
		int nd=min(100,Ad+B);
		ret=min(ret, solve(Hd-Ak,nd,Hk,Ak)+1);
	}
	if(Ak&&D){
		int nk=(max(0,Ak-D));
		ret=min(ret, solve(Hd-nk,Ad,Hk,nk)+1);
	}
	if(mxHd-Ak>Hd)ret=min(ret,solve(mxHd-Ak,Ad,Hk,Ak)+1);
	return ret;

}
int Hd,Ad,Hk,Ak;
int main(){
#ifndef ONLINE_JUDGE
	freopen("i.txt","r",stdin);
	freopen("o.txt","w",stdout);
#endif
	sc(t);
	lop(C,t){
		printf("Case #%d: ",C+1);
		memset(memo,-1,sizeof memo);
		cin>>Hd>>Ad>>Hk>>Ak>>B>>D;
		mxHd=Hd;
		int res=solve(Hd,Ad,Hk,Ak);
		if(res>100000000)puts("IMPOSSIBLE");
		else printf("%d\n",res);
	}
}
