#include <cstdio>
#include <vector>
#include <cassert>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
#include <map>

using namespace std;

int D,N,Ki,Si;
void run() {
  scanf("%d%d", &D, &N);
  double maxT=0.0;
  for (int i=0;i<N;++i) {
    scanf("%d%d", &Ki, &Si);
    double Ti=(double(D)-double(Ki))/double(Si);
    if (Ti>maxT) maxT=Ti;
  }
  printf("%.10f\n", double(D)/maxT);
}

int main() {
  int T;
  scanf("%d",&T);
  for (int t=1;t<=T;++t) {
    printf("Case #%d: ",t);
    run();
    fflush(stdout);
  }
  return 0;
}
