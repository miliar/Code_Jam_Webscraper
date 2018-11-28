#include "bits/stdc++.h"

using namespace std;

bool isTidy(long long a){
  int prev = a % 10;
  bool t = true;
  while(a > 0) {
    int curr = a % 10;
    a /= 10;
    if(curr > prev) return false;
    prev = curr;
  }
  return true;
}


int main() {

  int TC;
  int N;
  int c = 1;

  scanf("%d",&TC);
  while(TC--) {
    long long n;
    scanf("%lld",&n);
    long long ans = -1;
    for (long long i = n; i >= 0; --i) {
      if(isTidy(i)) {
        ans = i;
        break;
      }
    }
    printf("Case #%d: %lld\n",c++,ans);

  }
}
