#include <cstdio>
#include <cstring>
#include <vector>
#include <set>
#include <tuple>
#include <algorithm>

using namespace std;

struct interval {
  long long span;
  long long count;

  bool operator<(const interval& rhs) const {
    return span > rhs.span;
  }

  bool operator=(const interval& rhs) const {
    return span == rhs.span;
  }
};

std::tuple<long long, long long> split(long long n, long long k) {
  n--;
  k--;

  set<interval> S;
  std::tuple<long long, long long> res(n/2 + n%2, n/2);
  if (n % 2 == 1) {
    S.insert({.span = n/2, .count = 1});
    S.insert({.span = n/2 + 1, .count = 1});
  } else {
    S.insert({.span = n/2, .count = 2});
  }

  while (k > 0) {
    auto inter = *S.begin();
    S.erase(S.begin());


    k -= inter.count;
    // printf("span: %lld; count: %lld\n", inter.span, inter.count);
    auto new_span = inter.span - 1;
    // printf("l: %lld, r: %lld\n", new_span / 2 + new_span % 2, new_span / 2);
    res = std::make_tuple(new_span / 2 + new_span % 2, new_span / 2);

    interval left = {.span = new_span / 2, .count = inter.count};
    auto fl = S.find(left);
    if (fl != S.end()) {
      left.count += fl->count;
      S.erase(fl);
    }
    S.insert(left);

    interval right = {.span = new_span / 2 + new_span % 2, .count = inter.count};
    auto fr = S.find(right);
    if (fr != S.end()) {
      right.count += fr->count;
      S.erase(fr);
    }

    S.insert(right);
  }

  return res;
}

int main() {
  int t;
  scanf("%d", &t);
  for (int test = 1; test <= t; ++test) {
    long long n, k;
    scanf("%lld %lld", &n, &k);

    auto res = split(n, k);
    printf("Case #%d: %lld %lld\n", test, get<0>(res), get<1>(res));
  }

  return 0;
}
