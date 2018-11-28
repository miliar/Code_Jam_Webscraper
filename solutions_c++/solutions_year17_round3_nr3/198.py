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

#define INF 1987654321
#define PI 3.1415926535897932384626
int tc;int N,K;

vector<double> p; double U;
bool chk(double x){
	double u = 0;
	for(auto e : p ){
		//printf("%.2lf %.2lf\n",e,x);
		if( e <= x ){
			u += (x-e);
		}
	}
	return u <= U;
}
void solve(){
	p.clear();
	geti(N,K);
	scanf("%lf",&U);
	repp(i,N){
		double x;
		scanf("%lf",&x); p.push_back(x);
	}
	double ans = 1;
	double high = 1.1, low = 0.0;
	int cnt = 100; double res = 0;
	while(cnt--){
		double mid = (high+low)/2;
		if( chk(mid) ){
			low = mid; res = mid;
		}
		else{
			high = mid;
		}
	}
	for(auto e : p ){
		if( e > res ) ans *= e;
		else ans *= res;
	}
	//cout << res << endl;
	printf("%.10f\n",ans);
}
int main() {
	freopen("output.txt","w",stdout);
	scanf("%d",&tc);
	for(int t=1;t<=tc;t++){
		printf("Case #%d: ",t);
		solve();
	}
}	