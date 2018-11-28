#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

const double INF = 100000000000.0;

typedef double db;

const int N = 10005;

db p[N];
db s[N];
int n;
double d;
bool chk(double tt) {//시간 고정
	double bd = INF;
	for (int i = 0; i < n; ++i) {
		db tmp = p[i] + s[i]*tt;
		bd = min(bd,tmp);
	}
	if (bd < d) {
		return false;
	}
	else {
		return true;
	}
}

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	scanf("%d",&t);

	for(int i=1;i<=t;++i) {
		scanf("%lf%d",&d,&n);
		
		for (int i = 0; i < n; ++i) {
			scanf("%lf",p+i);
			scanf("%lf",s+i);
		}

		double l = 0.0000;
		double r = INF;

		for(int i=0;i<500;++i){
			double m = (l+r)/2;
		
			if (chk(m)) {
				r = m;
			}
			else {
				l = m;
			}
		}

		db ans = d/l;
		printf("Case #%d: %.8lf\n",i,ans);
	}
	return 0;
}