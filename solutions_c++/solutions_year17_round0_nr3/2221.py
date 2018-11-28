#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

pair<ll,ll> get_min_max(ll N)
{
  N--;

  ll small = N/2, large = N-N/2;
  return pair<ll,ll>(small,large);
}

void solve()
{
  ll K, N;

  cin >> N >> K;

  map<ll,ll> gaps;

  gaps[N] = 1;
  while (true) {
    auto it = gaps.rbegin();
    pair<ll,ll> entry = *it;
    gaps.erase(entry.first);

    auto r = get_min_max(entry.first);
    if (entry.second >= K) {
      cout << ' ' << r.second << ' ' << r.first << endl;
      return;
    }

    K -= entry.second;
    gaps[r.first] += entry.second;
    gaps[r.second] += entry.second;
  }
}

int main()
{
  int T;
  cin >> T;

  for (int i = 1; i <= T; i++) {
    cout << "Case #" << i << ": ";
    solve();
  }

  
  return 0;
}
