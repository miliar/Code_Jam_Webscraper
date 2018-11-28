#include <bits/stdc++.h>
using namespace std;

int Main() { 
  long long n, k;
  scanf("%lld %lld", &n, &k);
  
  map<long long, long long> cnt;
  long long sum = 0;
  cnt[n] = 1;
  
  while (1) {
    long long cur = cnt.rbegin()->first;
    long long c = cnt.rbegin()->second;
    
    if (sum + c >= k) {
      if (cur & 1) printf("%lld %lld\n", cur >> 1, cur >> 1);
      else printf("%lld %lld\n", cur >> 1, cur - 2 >> 1);
      return 0;
    }
    sum += c;
    
    if (cur & 1) cnt[cur >> 1] += c << 1;
    else {
      cnt[cur >> 1] += c;
      cnt[cur - 2 >> 1] += c;
    }
    cnt.erase(cur);
  }
  return 0;
}

int main() {
  int t;
  scanf("%d", &t);
  for (int tc=0; tc<t; ++tc) {
    printf("Case #%d: ", tc+1);
    Main();
  }
  return 0;
}