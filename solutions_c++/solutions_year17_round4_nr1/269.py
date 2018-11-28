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
int tc;int N,P;
int p[5];
void solve(){
	geti(N,P);
	vector<int> v;
	memset(p,0,sizeof p);
	repp(i,N){
		int x; geti(x);
		p[x%P]++;
	}
	if( P == 2 ){
		printf("%d\n",p[0]+p[1]/2+p[1]%2);
		return;
	}	
	if( P == 3 ){
		int ans = p[0];
		int mn = MIN2(p[1],p[2]);
		ans += mn; p[1] -= mn; p[2] -= mn;
		ans += p[1]/3; ans += p[2]/3; p[1]%=3; p[2]%=3;
		if( p[1] > 0 || p[2] > 0 ) ans++;
		printf("%d\n",ans);
		return;
	}
	int ans = p[0];
	ans += p[2]/2; p[2] %= 2;
	int mn = MIN2(p[1],p[3]);
	ans += mn; p[1]-=mn; p[3] -= mn;
	mn = MIN2(p[1]/2,p[2]);
	ans += mn; p[1] -= mn*2; p[2] -= mn;
	ans += p[1]/4; ans += p[3]/4; p[1] %= 4; p[3] %= 4;
	if( p[2] > 0 || p[1] > 0 || p[3] > 0 ) ans++;
	printf("%d\n",ans);
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
