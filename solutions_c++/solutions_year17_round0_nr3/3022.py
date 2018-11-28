#include <map>
#include <vector>
#include <iostream>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> pr;

pr traverse(vector<pr> v, ll k) {
  map<ll, ll, greater<ll>> counts;

  for (auto p : v) {
    ll n = p.first;
    ll c = p.second;

    ll n1 = n / 2;
    ll n2 = (n - 1) / 2;

    counts[n1] += c;
    counts[n2] += c;
    k -= c;

    if (k <= 0) {
      return pr(n1, n2);
    }
  }

  return traverse(vector<pr>(counts.begin(), counts.end()), k);
}

int main() {
  int T; scanf("%d", &T);
  for (int t = 0; t < T; ++t) {
    ll n, k; scanf("%lld %lld", &n, &k);
    auto v = vector<pr>({pr(n, 1)});
    auto p = traverse(v, k);
    printf("Case #%d: %lld %lld\n", t + 1, p.first, p.second);
  }
}
