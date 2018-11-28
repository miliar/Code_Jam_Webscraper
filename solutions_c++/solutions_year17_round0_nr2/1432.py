#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

bool is_tidy(long long k) {
  int prev = 10;
  while (k > 0) {
    int res = k % 10;
    if (res > prev) {
      return false;
    }

    k /= 10;
    prev = res;
  }

  return true;
}

long long prev_tidy(long long k) {
  vector<int> v;

  if (k <= 1) {
    return 1;
  }

  if (is_tidy(k)) {
    return k;
  }

  k--;
  int prev = 10;
  while (k > 0) {
    int res = k % 10;
    if (res > prev) {
      res--;
      std::fill(v.begin(), v.end(), 9);
    }

    v.push_back(res);
    k /= 10;
    prev = res;
  }

  std::reverse(std::begin(v), std::end(v));
  if (v[0] == 0) { v.erase(v.begin()); }

  long long p = v[0];
  for (std::size_t i = 1; i < v.size(); ++i) {
    p *= 10; p += v[i];
  }

  return p;
}




int main() {
  int t;
  scanf("%d", &t);
  for (int test = 1; test <= t; ++test) {
    long long n;
    scanf("%lld", &n);
    printf("Case #%d: %lld\n", test, prev_tidy(n));
  }

  return 0;
}
