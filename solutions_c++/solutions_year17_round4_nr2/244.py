#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <math.h>
#include <assert.h>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <iostream>
#include <functional>
#include <vector>
#include <stack>
#include <deque>

using namespace std;
typedef long long ll;
typedef pair<int, int> Pi;

#define Fi first
#define Se second
#define pb(x) push_back(x)
#define sz(x) (int)x.size()
#define rep(i, n) for(int i=0;i<n;i++)
#define repp(i, n) for(int i=1;i<=n;i++)
#define all(x) x.begin(), x.end()

#define ABS(x) (((x) > 0 ) ? (x) : (-(x)))
#define MAX2(x, y) (((x) > (y)) ? (x) : (y))
#define MIN2(x, y) (((x) < (y)) ? (x) : (y))

#define MAX3(x, y, z) ( (x) > (y)  ? ( (x) > (z) ? (x) : (z)  ) : ( (y) > (z) ? (y) : (z) )  )
#define MIN3(x, y, z) ( (x) < (y)  ? ( (x) < (z) ? (x) : (z)  ) : ( (y) < (z) ? (y) : (z) )  )
#define MID3(val1,val2,val3) MAX2(MIN2(MAX2(val1,val2),val3),MIN2(val1,val2))
#define geti1(X) scanf("%d",&X)
#define geti2(X,Y) scanf("%d%d",&X,&Y)
#define geti3(X,Y,Z) scanf("%d%d%d",&X,&Y,&Z)
#define geti4(X,Y,Z,W) scanf("%d%d%d%d",&X,&Y,&Z,&W)

#define GET_MACRO(_1,_2,_3,_4,NAME,...) NAME
#define geti(...) GET_MACRO(__VA_ARGS__, geti4, geti3, geti2, geti1) (__VA_ARGS__)
#define INF 987654321
#define IINF 4321987654321
int tc;int N,C,M,P;
vector<int> v[1050]; int cnt[1050];
void solve(){
	geti(N,C,M);
	rep(i,1050) v[i].clear();
	memset(cnt,0,sizeof cnt);
	int x = 0, y = 0;
	repp(i,M){
		int a,b; geti(a,b);
		v[a].pb(b); cnt[b]++;
	}
	repp(i,C) x = max(cnt[i],x);
	x = max((M+C-1)/C,x);
	int sum = 0;
	for(int i=1;i<=N;i++){
		sum += v[i].size();
		x = max( (sum+i-1)/i,x);
	}
	x = max((int)v[1].size(),x);
	printf("%d ",x);
	repp(i,N){
		y += max(0,(int)v[i].size()-x);
	}
	printf("%d",y);
	printf("\n");
}

int main(){
	//freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	geti(tc);
	repp(t,tc){
		printf("Case #%d: ",t);
		solve();
	}
}
