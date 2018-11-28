#include <bits/stdc++.h>

using namespace std;

int main() {
  int t; scanf("%d", &t);
  for(int _i=1; _i<=t; _i++) {
    int n, p; scanf("%d %d", &n, &p);
    vector<int> g(n);
    for(int i=0; i<n; i++) {
      scanf("%d", &g[i]);
    }
    printf("Case #%d: ", _i);
    if(p==2) {
      int even=0, odd=0;
      for(int i=0; i<n; i++) {
        if(g[i]%2==0) even++;
        else odd++;
      }
      printf("%d\n", even+(odd+1)/2);
    }
    if(p==3) {
      int three=0, two=0, one=0;
      for(int i=0; i<n; i++) {
        if(g[i]%3==0) three++;
        else if(g[i]%3==1) one++;
        else two++;
      }
      while(two>0 and one>0) {
        two--;
        one--;
        three++;
      }
      printf("%d\n", three+(one+2)/3+(two+2)/3);
    }
  }
}
