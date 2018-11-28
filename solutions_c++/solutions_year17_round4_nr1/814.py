#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int T, N, P, G[102];
int pm[102];

int main () {

  cin >> T;

  for(int tc=1;tc<=T;tc++) {
    for(int i=0;i<102;i++) {
      G[i] = 0;
      pm[i] = 0;
    }
    cin >> N >> P;
    for(int i=0;i<N;i++) {
      cin >> G[i];
      pm[G[i] % P] ++;
    }
    int ret = 0;
    ret += pm[0];
    if(P == 2) {
      ret += pm[1] / 2;
      pm[1] = pm[1] % 2;
    } else if(P == 3) {
      int c1 = min(pm[1], pm[2]);
      ret += c1;
      pm[1] -= c1;
      pm[2] -= c1;
      ret += pm[1]/3;
      ret += pm[2]/3;
      pm[1] = pm[1] % 3;
      pm[2] = pm[2] % 3;
    } else {
      int c1 = min(pm[1],pm[3]);
      ret += c1;
      pm[1] -= c1;
      pm[3] -= c1;

      c1 = min(pm[2] * 2, pm[1]) / 2;
      ret += c1;
      pm[1] -= c1 * 2;
      pm[2] -= c1;

      c1 = min(pm[2] * 2, pm[3]) /2;
      ret += c1;
      pm[3] -= c1 * 2;
      pm[2] -= c1;

      c1 = pm[2] / 2;
      ret += c1;
      pm[2] = pm[2] % 2;

      ret += pm[1] / 4;
      ret += pm[3] / 4;
      pm[1] = pm[1] % 4;
      pm[3] = pm[3] % 4;
    }
    bool lf = false;
    for(int i=1;i<P;i++) {
      if(pm[i] > 0 ) lf = true;
    }
    if(lf) ret ++;


    printf("Case #%d: ",tc);
    printf("%d", ret);
    printf("\n");
  }

  return 0;
}