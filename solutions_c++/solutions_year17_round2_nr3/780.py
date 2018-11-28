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

long dist[101][101];
int max_dist[101],speed[101];
int N;

long double min_time[101][101];

int main() {
  int T,cs;
  int Q;
  int i,j,k;
  
  scanf("%d",&T);

  rab(cs,1,T) {
    scanf("%d %d",&N,&Q);
    Fi(N) scanf("%d %d",&max_dist[i],&speed[i]);
    Fi(N) Fj(N) {
      scanf("%ld",&dist[i][j]);
      min_time[i][j] = -1.;
    }

    Fk(N) Fi(N) Fj(N) {
      if (dist[i][k] == -1 || dist[k][j] == -1) continue;
      long r = dist[i][k] + dist[k][j];
      if (dist[i][j] == -1 || r < dist[i][j]) {
        dist[i][j] = r;
      }
    }

    Fi(N) Fj(N) {
      long  d = dist[i][j];
      if (d < 0 || d > max_dist[i]) {
        min_time[i][j] = -1;
      } else {
        min_time[i][j] = (long double)dist[i][j] / (long double)speed[i];
      }
    }

    Fk(N) Fi(N) Fj(N) {
      //printf("%d %d %d: %lf %lf %lf\n",k,i,j,min_time[i][k],min_time[k][j],min_time[i][j]);
      if (min_time[i][k] < -0.5 || min_time[k][j] < -0.5) continue;
      double r = min_time[i][k] + min_time[k][j];
      if (min_time[i][j] < -0.5 || r < min_time[i][j]) min_time[i][j] = r;
    }

    printf("Case #%d:", cs);

    while (Q--) {
      scanf("%d %d",&i,&j);
      i--,j--;
      assert(i != j);
      printf(" %.11Lf",min_time[i][j]);
    }
    printf("\n");
  }

  return 0;
}
