#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <cmath>
#include <cctype>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <bitset>
#include <list>
#include <cstdarg>

#ifndef DBG
#define	DBG	0
#endif

//#define	DBG(f,x)	if(_____debug & f) { x; }
using namespace std;

#define	rep(i,n)	for((i) = 0; (i) < (n); (i)++)
#define	rab(i,a,b)	for((i) = (a); (i) <= (b); (i)++)
#define all(v)		(v).begin(),(v).end()
#define	Fi(n)		rep(i,n)
#define	Fj(n)		rep(j,n)
#define	Fk(n)		rep(k,n)
#define	sz(v)		(v).size()

#define INF 1e+50
#define EPS 1e-15

double position[10000];
double speed[10000];
int N;

bool flag;

double intersect_at(double d, double s, double m) {
  if (m > s) {
    return m * (d / (m - s));
  } else {
    return INF;
  }
}

bool possible(double m, double D) {
  int i;

  Fi(N) {
    double d1 = intersect_at(position[i], speed[i], m);
    //if (flag) printf("%lf intersects at %.11lf\n",m,d1);
    //if (fabs(d1 - D) < EPS) continue;
    if (d1 < D) {
      return false;
    }
  }
  return true;
}

double bisection(double D) {
  int i;
  long double lo,up,mid;
  lo = INF;
  Fi(N) if (speed[i] < lo) lo = speed[i];
  up = INF;

  int iter = 0;

  while (fabs(lo - up) > EPS) {
    mid = (lo + up) / 2;

    //if (flag) printf("%d: %.9lf, %.9lf %.9lf -- %.9lf \n", ++iter,mid,lo,up, fabs(lo-up));
    if (possible(mid, D)) {
      lo = mid;
    } else {
      up = mid;
    }
    //if (iter > 20) exit(0);
  }

  return mid;
}

int main() {
  int T, cs;
  int i;
  double D;

  scanf("%d", &T);

  rab(cs,1,T) {
    scanf("%lf%d",&D,&N);

    Fi(N) {
      scanf("%lf %lf",&position[i], &speed[i]);
      position[i] /= D;
      speed[i] /= D;
    }

    if (cs == 18) flag = true;

    printf("Case #%d: %.7lf\n", cs, bisection(1) * D);
  }

  return 0;
}
