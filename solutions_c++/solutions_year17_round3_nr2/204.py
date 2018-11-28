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
int tc;
int N,K;
int A,B;
int type[10050];
int asum, bsum;
void solve(){
	memset(type,0,sizeof type);
	geti(A,B);
	asum = bsum = 0;
	vector<pair<Pi,int>> event;
	repp(i,A){
		int a,b; geti(a,b);
		for(int i=a;i<b;i++){
			type[i] = 1;
			asum ++;
		}
		event.push_back({{a,b},1});
	}
	repp(i,B){
		int a,b; geti(a,b);
		for(int i=a;i<b;i++){
			bsum++;
			type[i] = 2;
		}
		event.push_back({{a,b},2});
	}
	
	vector<int> alist, blist;
	int ans = 0;
	sort(all(event));
	for(int i=0;i<event.size()-1;i++){
		if( event[i].Se == event[i+1].Se ){
			if( event[i].Se == 1 ){
				alist.push_back(event[i+1].Fi.Fi - event[i].Fi.Se);
			}
			else{
				blist.push_back(event[i+1].Fi.Fi - event[i].Fi.Se);
			}
			ans+=2;
		}
		else ans++;
	}

	if( event[event.size()-1].Se == event[0].Se ){
		if( event[0].Se == 1 ){
			alist.push_back(event[0].Fi.Fi + 1440 - event[event.size()-1].Fi.Se);
		}
		else{
			blist.push_back(event[0].Fi.Fi + 1440 - event[event.size()-1].Fi.Se);
		}
		ans+=2;	
	}
	else ans++;
	sort(all(alist)); sort(all(blist));
	for(auto e : alist){
		if( asum + e > 720 ) break;
		asum += e; ans-=2;
	}
	for(auto e : blist){
		if( bsum + e > 720 ) break;
		bsum += e; ans-=2;
	}
	printf("%d\n",ans);
}
int main() {
	freopen("output.txt","w",stdout);
	scanf("%d",&tc);
	for(int t=1;t<=tc;t++){
		printf("Case #%d: ",t);
		solve();
	}
}	