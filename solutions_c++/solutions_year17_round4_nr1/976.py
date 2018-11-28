#include<bits/stdc++.h>
using namespace std;

#define scl(x) scanf("%lld",&x)
#define sc(x)  scanf("%d",&x)
#define ll long long
#define lop(i,n) for(int i=0;i<n;++i)
typedef pair<int, int> ii;
typedef pair<ll, ll> pll;

int memo[101][101][101][4][5];

int solve(int c1,int c2,int c3,int left,int p){
	if(!c1&&!c2&&!c3)return 0;
	int &ret=memo[c1][c2][c3][left][p];
	if(~ret)return ret;
	ret=0;

	if(c1){
		ret=solve(c1-1,c2,c3,(left-1+p)%p,p);
	}
	if(c2){
		ret=max(ret, solve(c1,c2-1,c3,(left-2+p)%p,p));
	}
	if(c3){
		ret=max(ret, solve(c1,c2,c3-1,(left-3+p)%p,p));
	}
	if(!left)ret++;
	return ret;
}
int main(){
#ifndef ONLINE_JUDGE
	freopen("i.txt","r",stdin);
	freopen("o.txt","w",stdout);
#endif
	memset(memo,-1,sizeof memo);
	int t;
	sc(t);
	lop(C,t){
		int n,p;
		int c[4]={0,0,0,0};
		sc(n);
		sc(p);
		lop(i,n){
			int v;
			sc(v);
			++c[v%p];
		}
		printf("Case #%d: %d\n",C+1,c[0]+solve(c[1],c[2],c[3],0,p));
	}
}
