#include <bits/stdc++.h>
using namespace std;

int main() {
  int t; scanf("%d", &t);
  for(int _i=1; _i<=t; _i++) {
    printf("Case #%d: ", _i);
    long long int n, k; scanf("%lld %lld", &n, &k);
    map<long long int, long long int> counts;
    counts[n] = 1;
    while(true) {
      long long int n = (*counts.rbegin()).first;
      long long int count = (*counts.rbegin()).second;
      if(count < k) {
        // printf("Putting %lld people in spaces of size %lld\n", count, n);
        counts.erase(n);
        counts[(n-1)/2]+=count;
        counts[n-1-((n-1)/2)]+=count;
        k-=count;
      } else {
        break;
      }
    }
    n = (*counts.rbegin()).first;
    printf("%lld %lld\n", n-1-(n-1)/2, (n-1)/2);
  }
}
