#include <algorithm>
#include <array>
#include <cstdio>
#include <iostream>
#include <map>
#include <string>
#include <limits>
#include <vector>

using ll = long long;

// static std::map<ll, bool> dp;
static std::map<std::string, bool> dp;

bool IsTidy(const std::string &n) {
  if (dp.find(n) != dp.end()) {
    return dp[n];
  }

  if (n.size() == 1) {
    return dp[n] = true;;
  }

  const char head = n[0];
  const std::string tail = n.substr(1, n.size() - 1);
  if (dp.find(tail) != dp.end()) {
    return dp[tail] && (head <= tail[0]);
  }
  if (!IsTidy(tail)) {
    dp[tail] = false;
    return dp[n] = false;
  }

  if (head <= tail[0]) {
    return dp[n] = true;
  } else {
    return dp[n] = false;
  }
}

ll findTidy(ll l, ll to, ll max) {
  if (l > to) {
    return max;
  }
  ll m = max;

  if (IsTidy(std::to_string(l))) {
    if (l > m) {
      m = l;
    }
  }

  return findTidy(l + 1, to, m);
}

ll FindTidy(ll to) {
  return findTidy(0, to, 0);
}

ll FindTidyIter(ll to) {
  ll m = 0;

  for (ll i = 0; i < to; i++) {
    if (IsTidy(std::to_string(i))) {
      if (i > m) {
        m = i;
      }
    }
  }

  return m;
}

ll FindTidyIterRev(ll to) {
  ll m = 0;

  for (ll i = to; i >= 0; i--) {
    if (IsTidy(std::to_string(i))) {
      m = i;
      break;
    }
  }

  return m;
}


int main(int argc, char *argv[]) {
  int n;
  std::scanf("%d\n", &n);

  std::string result;

  for (int i = 1; i <= n; ++i) {
    ll l;
    std::scanf("%lld\n", &l);
    // ll tidy = FindTidy(l);
    ll tidy = FindTidyIterRev(l);
    // dp.clear();
    result += "Case #" + std::to_string(i) + ": ";
    result += std::to_string(tidy);
    result += "\n";
  }

  std::cout << result;

  return 0;
}
