#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;
typedef long long ll;
ll n, k;
vector<pair<ll, ll>> a;

void search(ll l, ll r) {
  ll mid = (l + r) >> 1;
  a.push_back({mid - l, r - mid});
  if (r <= l) return;
  search(l, mid - 1);
  search(mid + 1, r);
}

bool cmp(const pair<ll, ll>& a, const pair<ll, ll>& b) {
  return (a.first + a.second > b.first + b.second);
}

int main() {
  ios_base::sync_with_stdio(false);
  int t; cin >> t;
  for (int i = 1; i <= t; ++i) {
    cin >> n >> k;
    a.clear();
    search(1, n);
    sort(a.begin(), a.end(), cmp);
    cout << "Case #" << i << ": " << max(a[k - 1].first, a[k - 1].second) << " " << min(a[k - 1].first, a[k - 1].second) << endl;
  }

  return 0;
}
