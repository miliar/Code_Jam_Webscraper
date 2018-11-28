#include <algorithm>
#include <array>
#include <cstdio>
#include <iostream>
#include <map>
#include <string>
#include <limits>
#include <vector>

using ll = long long;

static const int INF = std::numeric_limits<int>::max() >> 1;
// static const int INF = -1;

// static std::map<ll, bool> dp;
static std::map<std::string, bool> dp;

using stall = std::tuple<ll, ll, bool>;

inline std::string P(const stall &s) {
  ll l, r;
  bool o;
  std::tie(l, r, o) = s;
  std::string res;
  res +=  "("  + std::to_string(l) + ", " + std::to_string(r) + ", " + std::to_string(o) + ")";
  return res;
}

void updateStalls(std::vector<stall>& v, std::vector<stall>::iterator& it) {
  auto &occupied = std::get<2>(*it);
  occupied = true;

  const auto ls = std::get<0>(*it);
  const auto rs = std::get<1>(*it);

  for (auto i = it - ls; i < it; i++) {
    // std::cout << "updating right: " << P(*i) << std::endl;
    // std::get<1>(*i) = std::get<1>(*i) - 1;
    auto &r = std::get<1>(*i);
    r = it - i - 1;
    // std::cout << "update right: " << P(*i) << std::endl;
  }

  for (auto i = it + rs; i > it; i--) {
    // std::cout << i - v.begin() << std::endl;
    // std::cout << "updating left: " << P(*i) << std::endl;
    // std::get<0>(*i) = std::get<0>(*i) - 1;
    auto &l = std::get<0>(*i);
    l = i - it - 1;
    // std::cout << "update left: " << P(*i) << std::endl;
  }

  // for (auto s : v) {
  //   std::cout << P(s) << std::endl;
  // }
}

bool StallComparator(const stall &a, const stall &b) {
  ll als, ars, bls, brs;
  bool aoccupied, boccupied;
  std::tie(als, ars, aoccupied) = a;
  std::tie(bls, brs, boccupied) = b;
  // std::cout << "(" << als << ", " << ars << ", " << aoccupied << ") < --- (" 
  //           << bls << ", " << brs << ", " << boccupied << ")";

  if (aoccupied && !boccupied) {
    // return true;
    return false;
  }
  if (!aoccupied && boccupied) {
    // return false;
    return true;
  }

  if (aoccupied && boccupied) {
    return false;
  }

  ll amin = std::min(als, ars);
  ll bmin = std::min(bls, brs);

  if (amin == bmin) {
    ll amax = std::max(als, ars);
    ll bmax = std::max(bls, brs);
    if (amax == bmax) {
      return false;
    } else {
      return amax > bmax;
    }
  }

  bool r = (amin > bmin);
  // std::cout << std::min(als, ars) << "<" << std::min(bls, brs) << ": " << r << std::endl;
  return r;
}

// std::vector<stall>::iterator FindStall(std::vector<stall> &v) {
std::vector<stall>::iterator FindStall(std::vector<stall> &v,
                                       const std::vector<stall>::iterator &from,
                                       const std::vector<stall>::iterator &to) {
  // ll min;
  std::vector<stall>::iterator rit = from + 1;

  for (auto it = from; it <= to; it++) {
    auto c = StallComparator(*it, *rit);
    if (c) {
      // std::cout << P(*it) << "vs" << P(*rit) << ": " << c << std::endl;
      rit = it;
    }
  }

  // return std::move(rit);
  return rit;
}

stall GetLastStall(std::vector<stall>& v, ll k) {
  ll l, r;
  bool occupied;

  std::vector<stall>::iterator tmp = v.begin();
  // std::vector<stall>::iterator tmp = v.end();

  for (int i = 0; i < k - 1; i++) {
    // auto it = std::max_element(std::begin(v), std::end(v), StallComparator);
    std::vector<stall>::iterator it;
    int half = (v.end() - v.begin()) / 2 - 1;
    if ((tmp - v.begin()) <= half) {
      it = FindStall(v, v.begin() + half + 1, v.end() - 1);
    } else {
      it = FindStall(v, v.begin() + 1, v.begin() + half);
    }
    
    // std::cout << "it: " << P(*it) << std::endl;
    updateStalls(v, it);
    tmp = it;
  }

  // auto it = std::max_element(std::begin(v), std::end(v), StallComparator);
  std::vector<stall>::iterator it;
  int half = (v.end() - v.begin()) / 2 - 1;
  if ((tmp - v.begin()) <= half) {
    it = FindStall(v, v.begin() + half + 1, v.end() - 1);
  } else {
    it = FindStall(v, v.begin() + 1, v.begin() + half);    
  }
  // auto it = FindStall(v);
  std::tie(l, r, occupied) = *it;
  // std::cout << "max: (" << l << ", " << r << ", " << occupied << ")" << std::endl;
  return *it;
}

void InitializeStalls(std::vector<stall>& v, ll n) {
  auto left_guard = std::make_tuple(INF, n-2, true);
  // *v.begin() = left_guard;
  v[0] = left_guard;
  auto right_guard = std::make_tuple(n-2, INF, true);
  // *v.end() = right_guard;
  v[v.size()-1] = right_guard;

  for (auto it = v.begin() + 1; it < v.end() - 1; it++) {
    // std::cout << "it: " << it - v.begin() << std::endl;
    ll ls = it - v.begin() - 1;
    ll rs = v.end() - it - 2;
    // std::cout << ls << std::endl;
    // std::cout << rs << std::endl;
    *it = std::make_tuple(ls, rs, false);
  }

  // for (auto s : v) {
  //   std::cout << P(s) << std::endl;
  // }
}


int main(int argc, char *argv[]) {
  int n;
  std::scanf("%d\n", &n);

  std::string result;

  for (int i = 1; i <= n; ++i) {
    ll n, k, l, r;
    bool occupied;
    result += "Case #" + std::to_string(i) + ": ";

    std::scanf("%lld %lld\n", &n, &k);
    // std::cout << n << " " << k << std::endl;
    if (n == k) {
      result += "0 0";
    } else {
      // ll tidy = FindTidy(l);
      std::vector<stall> v(n + 2);
      InitializeStalls(v, n + 2);
      // ll tidy = FindTidyIterRev(l);
      std::tie(l, r, occupied) = GetLastStall(v, k);
      // dp.clear();
      
      result += std::to_string(std::max(l, r)) + " " + std::to_string(std::min(l, r));
    }
    result += "\n";
  }

  std::cout << result;

  return 0;
}
