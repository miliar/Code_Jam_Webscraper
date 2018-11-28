#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

const int infinity = 1e9 + 9;

long long N, K;

int main()
{
  int T;
  scanf("%d", &T);
  for (int Ti = 1; Ti <= T; Ti++)
  {
    // input
    scanf("%lld %lld", &N, &K);
    
    // compute binary expansion of K
    vector<long long> L;
    L.push_back(N);
    while (K > 0) {
      // serve from L
      if (L.size() >= K) {
        sort(L.begin(), L.end());
        reverse(L.begin(), L.end());
        long long a = L[K - 1];
        long long l = (a - 1) / 2;
        long long r = (a - 1) - l;
        //printf("%lld %lld %lld\n", a, l, r);
        printf("Case #%d: %lld %lld\n", Ti, r, l);
        break;
      }

      // compute next generation
      K = K - L.size();
      vector<long long> L_new;
      for (int i = 0; i < L.size(); ++i) {
        long long a = (L[i] - 1) / 2;
        long long b = (L[i] - 1) - a;
        L_new.push_back(a);
        L_new.push_back(b);
      }
      L = L_new;
    }
  }
  return 0;
}
