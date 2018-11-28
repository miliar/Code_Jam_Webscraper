#include <string>
#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;

#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)

typedef long long LL;
const int INF = 1000000000;
const LL INFLL = (LL)INF*(LL)INF;
inline int getint() { int x; scanf("%d",&x); return x; }
inline void OPEN(string name) {
	string in = name+".in"; freopen(in.c_str(),"r",stdin);
	string out = name+".out"; freopen(out.c_str(),"w",stdout);
}

// Powered By TimoAI 2.2


int pos[1024];
double speed[1024];
int N;
double D;

double calc(double alfa, double beta) {
	REP(x,256) {
		double gama = (alfa + beta) / 2.0;
		double tt = D / gama;
		double zz = (D - 1) / gama;
		bool ok = true;
		REP(i,N) {
			double t2 = (D - pos[i]) * 1.0 / speed[i];
			double t3 = (D - 1 - pos[i]) * 1.0 / speed[i];
			if(tt <= t2 || zz <= t3) {
				ok = false;
				break;
			}
		}
		if(ok) alfa = gama;
		else beta = gama;
	}
	return alfa;
}

int main() {
	OPEN("A");
	double ans = INF;
	REP(nc,getint()) {
		D = getint();
		N=getint();
		REP(i,N) {
			pos[i] = getint();
			speed[i] = getint();
			double v = (D - pos[i]) * 1.0 / speed[i];
			double a = D / v;
			ans = min(ans, a);
		}

		printf("Case #%d: %.6f\n",nc+1,calc(0,INFLL));
	}
	return 0;
}
