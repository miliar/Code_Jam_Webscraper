#include <queue>
#include <vector>
#include <cstdio>
#include <cstdlib>
using namespace std;

int main() {
  int T; scanf("%d", &T);
  for(int tc = 1;tc <= T;++tc) {
    printf("Case #%d: ", tc);
    int n, k;
    double u;

    scanf("%d%d", &n, &k);
    scanf("%lf", &u);

    double sc;
    priority_queue<double, vector<double>, greater<double> > pq;
    for(int i = 0;i < n;++i) {
      scanf("%lf", &sc);
      pq.push(sc);
    }

    if(n==1) {
      printf("%.10lf\n", u + sc);
      continue;
    }

    while(u) {
      double t = pq.top(); pq.pop();
      int jml = 1;
      while(!pq.empty() && pq.top() == t) {
        pq.pop();
        ++jml;
      }

      if(pq.empty()) {
          // bagi2 ke semua bro
          double add = u/(1.0*jml);
          while(jml--) pq.push(t + add);
          u = 0;
          break;
      } else {
        double nx = pq.top();
        if( (nx-t)*1.0*jml <= u ) {
          u -= (nx-t)*1.0*jml;
          while(jml--) pq.push(nx);
        } else {
          double add = u/(1.0*jml);
          while(jml--) pq.push(t + add);
          u = 0;
          break;
        }
      }
    }

    double ans = 1.0;
    while(!pq.empty()) {
      double t = pq.top(); pq.pop();
      ans = ans * t;
    }

    printf("%.10lf\n", ans);
  }
}
