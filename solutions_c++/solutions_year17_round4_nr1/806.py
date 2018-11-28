#include <bits/stdc++.h>
using namespace std;

#define FOR(i,l,r) for(int i = (int) (l);i < (int) (r);i++)
template<typename T> bool chmax(T& a,const T& b){ return a < b ? (a = b,true) : false; }
template<typename T> bool chmin(T& a,const T& b){ return b < a ? (a = b,true) : false; }
typedef long long ll;

int TC,N,P;
int cnt [10];
int memo [200] [200] [200];

int rec(int a,int b,int c)
{
	if(memo [a] [b] [c] != -1) return memo [a] [b] [c];
	int res = 0;
	if(a || b || c) chmax(res,rec(0,0,0) + 1);
	FOR(i,0,5) FOR(j,0,5) FOR(k,0,5) if(i + j + k > 0 && i <= a && j <= b && k <= c){
		if((i + j * 2 + k * 3) % P == 0){
			chmax(res,rec(a - i,b - j,c - k) + 1);
		}
	}
	return memo [a] [b] [c] = res;
}

int main()
{
	scanf("%d",&TC);
	FOR(tc,1,TC + 1){
		scanf("%d%d",&N,&P);
		memset(cnt,0,sizeof(cnt));
		FOR(i,0,N){
			int x;
			scanf("%d",&x);
			cnt [x % P]++;
		}
		memset(memo,-1,sizeof(memo));
		memo [0] [0] [0] = cnt [0];
		int ans = rec(cnt [1],cnt [2],cnt [3]);
		printf("Case #%d: %d\n",tc,ans);
	}

	return 0;
}
