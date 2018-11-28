#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

vector<int> digits(ll n) {
  vector<int> ret;
  while (n) {
    ret.push_back(n % 10);
    n /= 10;
  }
  vector<int> ret2;
  for (int i = (int)ret.size() - 1; i >= 0; i--) {
    ret2.push_back(ret[i]);
  }
  return ret2;
}

ll solve(ll n) {
  vector<int> dig = digits(n);
  int ind = -1;
  for (int i = 0; i < (int)dig.size() - 1 && ind == -1; i++) {
    if (dig[i] > dig[i + 1]) ind = i;
  }
  if (ind == -1) return n;
  ll ret = 0;
  int ind2 = -1;
  for (int i = 0; i < (int)dig.size() && ind2 == -1; i++) {
    if (dig[i] == dig[ind]) ind2 = i;
  }
  for (int i = 0; i < dig.size(); i++) {
    ret *= 10;
    if (i < ind2) ret += dig[i];
    else if (i == ind2) ret += dig[i] - 1;
    else ret += 9;
  }
  return ret;
}

int main(void) {
  if (fopen("probBsmall.in", "r")) {
    freopen("probBsmall.in", "r", stdin);
    freopen("probBsmall.out", "w", stdout);
  }
  if (fopen("probBlarge.in", "r")) {
    freopen("probBlarge.in", "r", stdin);
    freopen("probBlarge.out", "w", stdout);
  }
  int t;
  ll n;
  cin >> t;
  for (int i = 1; i <= t; i++) {
    cin >> n;
    printf("Case #%d: %lld\n", i, solve(n));
  }
  return 0;
}
