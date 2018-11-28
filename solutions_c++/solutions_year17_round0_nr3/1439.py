#include <cstdio>
#include <map>

using namespace std;

int T, test_case = 1;
long long N, K;
map<long long, long long, greater<long long> > M;

int main(void) {
  scanf("%d", &T);

  while (T--) {
    scanf("%lld %lld", &N, &K);
    M.clear();
    M[N] = 1;

    pair<long long, long long> last;
    while (K > 0) {
      long long range = M.begin()->first;
      long long cnt = M.begin()->second;

      K -= cnt;
      M.erase(M.begin());

      long long idx = (range + 1) / 2;

      long long left = idx - 1;
      long long right = range - idx;

      if (left > 0) M[left] += cnt;
      if (right > 0) M[right] += cnt;

      last = make_pair(max(left, right), min(left, right));
    }
    printf("Case #%d: %lld %lld\n", test_case++, last.first, last.second);
  }
 
  return 0;
}
