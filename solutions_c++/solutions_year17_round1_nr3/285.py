#include <bits/stdc++.h>
using namespace std;

#define FOR(i,l,r) for(int i = (int) (l);i < (int) (r);i++)
#define ALL(x) x.begin(),x.end()
template<typename T> bool chmax(T& a,const T& b){ return a < b ? (a = b,true) : false; }
template<typename T> bool chmin(T& a,const T& b){ return b < a ? (a = b,true) : false; }
typedef long long ll;

int T,Hd,Hk,Ad,Ak,B,D;
const int MAX = 100;
const int INF = 1e9;

int solve(int Hd,int Ad,int Hk,int Ak,int debuff,int buff)
{
	int res = 0,curr = Hd;
	FOR(i,0,debuff){
		if(curr <= max(0,Ak - D)){
			curr = Hd - Ak;
			res++;
		}
		Ak = max(0,Ak - D);
		res++;
		if(curr <= Ak) return INF;
		curr -= Ak;
	}
	FOR(i,0,buff){
		if(curr <= Ak){
			curr = Hd - Ak;
			res++;
		}
		Ad = min(100,Ad + B);
		res++;
		if(curr <= Ak) return INF;
		curr -= Ak;
	}
	while(true){
		if(Hk <= Ad) return res + 1;
		if(curr <= Ak){
			curr = Hd - Ak;
			res++;
		}
		Hk = max(0,Hk - Ad);
		res++;
		if(curr <= Ak) return INF;
		curr -= Ak;
	}
	return INF;
}

int main()
{
	scanf("%d",&T);
	FOR(testCase,1,T + 1){
		scanf("%d%d%d%d%d%d",&Hd,&Ad,&Hk,&Ak,&B,&D);
		int ans = INF;
		FOR(debuff,0,MAX + 1) FOR(buff,0,MAX + 1){
			chmin(ans,solve(Hd,Ad,Hk,Ak,debuff,buff));
		}
		if(ans == INF){
			printf("Case #%d: IMPOSSIBLE\n",testCase);
		}
		else{
			printf("Case #%d: %d\n",testCase,ans);
		}
	}

	return 0;
}
