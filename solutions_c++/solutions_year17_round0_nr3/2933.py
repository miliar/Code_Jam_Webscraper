#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

pair<ll, ll> solve(ll n, ll k)
{
  queue<pair<ll, ll>> q;
  q.push({ n / 2, (n - 1) / 2 });

  map< pair<ll, ll>, ll> cnt;
  cnt[q.front()]++;
  
  ll total_cnt = 0;
  while (!q.empty())
  {
    total_cnt += cnt[q.front()];

    if (total_cnt >= k)
      break;

    ll max_v = q.front().first;
    ll min_v = q.front().second;
    pair<ll, ll> max_pair = { max_v / 2, (max_v - 1) / 2 };
    pair<ll, ll> min_pair = { min_v / 2, (min_v - 1) / 2 };
    for (auto child_pair : { max_pair, min_pair })
    {
      if (!cnt[child_pair])
        q.push(child_pair);
      
      cnt[child_pair] += cnt[q.front()];
    }

    q.pop();
  }

  return q.front();
}

int main()
{
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  int T;
  cin >> T;
  for (int test_case = 1; test_case <= T; test_case++)
  {
    ll n, k;
    cin >> n >> k;

    auto res = solve(n, k);

    cout << "Case #" << test_case << ": "
         << res.first << ' ' << res.second
         << '\n';
  }
}
