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

typedef pair<double,int> pd;

int N,M,T,K,tc;
int Q; vector<pair<double,double>> horse;
double dist[300][300];
vector<pair<int,double>> E[300]; double time[300][300];
double ans[300];
void solve(){
	rep(i,300) E[i].clear();
	horse.clear();
	rep(i,300) rep(j,300) dist[i][j] = 0;
	geti(N,Q); 
	horse.push_back({0,0});
	repp(i,N){
		double x,y; scanf("%lf%lf",&x,&y);
		horse.push_back({x,y});
	}
	repp(i,N){
		repp(j,N){
			scanf("%lf",&dist[i][j]);
			if( dist[i][j] < 0 ) dist[i][j] = 1e20;
		}
	}
	
	repp(k,N){
		repp(i,N){
			repp(j,N){
				if( dist[i][j] > dist[i][k] + dist[k][j] ) dist[i][j] = dist[i][k] + dist[k][j];
			}
		}
	}
	
	repp(i,N){
		repp(j,N)if( i != j ){ // i -> j
			double mxdist = horse[i].Fi; double speed = horse[i].Se;
			time[i][j] = 1e20;
			if( dist[i][j] <= mxdist ){
				E[i].push_back({j,dist[i][j]/speed});
			//	printf("Add %d to %d - %lf\n",i,j,dist[i][j]/speed);
				time[i][j] = dist[i][j]/speed;
			}
		}
	}



	repp(q,Q){
		int S,D; geti(S,D);
		rep(i,300)  ans[i] = 1e20;
		priority_queue<pd, vector<pd>, greater<pd>> pq;
		ans[S] = 0; pq.push({ans[S],S});

		while(!pq.empty()){
			int cur = pq.top().Se; double curdist = pq.top().Fi;
			pq.pop();
			if( ans[cur] < curdist ) continue;
			for(auto e : E[cur]){
				if( ans[e.Fi] > curdist + e.Se ){
					ans[e.Fi] = curdist + e.Se;
					pq.push({ans[e.Fi], e.Fi});
				}
			}
		}
		//repp(i,N) printf("%.10lf ",ans[i]);
		printf("%.10f ",ans[D]);
	}

	printf("\n");
}

int main() {
	freopen("output.txt","w",stdout);
	scanf("%d\n",&tc);
	for(int tt=1;tt<=tc;tt++){
		printf("Case #%d: ",tt);
		solve();
	}
}