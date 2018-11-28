#include <string>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

#define DEBUGxy(x,y) cerr << #x << " = " << x << ", " << #y << " = " << y << endl;
#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)
#define GI ({int _x; scanf("%d",&_x); _x;})

typedef long long LL;
const int INF = 1000000000;
const LL INFLL = (LL)INF*(LL)INF;
inline int getint() { int x; scanf("%d",&x); return x; }
inline void OPEN(string name) {
	string in = name+".in"; freopen(in.c_str(),"r",stdin);
	string out = name+".out"; freopen(out.c_str(),"w",stdout);
}

// Powered By TimoAI 2.2

int N;

LL dist[128][128];
double best[128][128];
int speed[128];
int maks[128];

int main() {
	OPEN("C");
	REP(nc,getint()) {
		N = GI;
		int Q = GI;
		REP(i,N) {
			maks[i] = GI;
			speed[i] = GI;
		}
		REP(i,N) REP(j,N) {
			dist[i][j] = GI;
			best[i][j] = INFLL;
			if(dist[i][j]==-1) dist[i][j] = INFLL;
			else {
				if(dist[i][j] <= maks[i]) {
					best[i][j] = dist[i][j] * 1.0 / speed[i];
				}
			}
		}

		REP(k,N) REP(i,N) REP(j,N)
			dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j]);

		REP(k,N) REP(i,N) REP(j,N) {
			// i ke k
			// k ke j


			LL dd = dist[i][k] + dist[k][j];
			if(dd <= maks[i]) {
				double t = dist[i][j] * 1.0 / speed[i];
				if(t < best[i][j]) {
					best[i][j] = t;
				}
			}

			if(dist[i][k] <= maks[i] && dist[k][j] <= maks[k]) {
				double t1 = dist[i][k] * 1.0 / speed[i];
				double t2 = dist[k][j] * 1.0 / speed[k];
				if(t1 + t2 < best[i][j]) best[i][j] = t1 + t2;
			}

			double cik = INFLL;
			double ckj = INFLL;

			if(dist[i][k] <= maks[i]) {
				cik = dist[i][k] * 1.0 / speed[i];
			}
			if(dist[k][j] <= maks[k]) {
				ckj = dist[k][j] * 1.0 / speed[k];
			}

			double ik = min(best[i][k], cik);
			double kj = min(best[k][j], ckj);

			best[i][j] = min(best[i][j], ik + kj);

		}


		printf("Case #%d:",nc+1);
		REP(q,Q) {
			int a = GI;
			int b = GI;
			a--; b--;
			//DEBUGxy(dist[a][b], best[a][b]);
			printf(" %lf",best[a][b]);
		}
		puts("");
	}
	return 0;
}
