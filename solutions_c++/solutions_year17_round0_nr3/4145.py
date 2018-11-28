#include <bits/stdc++.h>

using namespace std;

typedef pair <int, int> pii;
typedef long long LL;

LL bestSolve(LL n, LL k)
{
  vector < pair <LL, LL> > a;
  a.push_back(make_pair(n, 1LL));
  int i = 0;
  while ( a.back().first > 1LL )
  {
    LL ai = a[i].first, num = a[i].second;
    if ( ai%2LL == 1LL ) //ai le
      if ( a.back().first == ai/2LL )
        a.back().second += 2LL*num;
      else
        a.push_back(make_pair(ai/2LL, 2LL*num));
    else //ai chan
    {
      if ( a.back().first == ai/2LL )
        a.back().second += num;
      else
        a.push_back(make_pair(ai/2LL, num));
      a.push_back(make_pair(ai/2LL - 1LL, num));
    }
    i++;
  }

  while ( !a.empty() && a.back().first <= 1LL ) a.pop_back();

  for (i = 0; i < (int)a.size() && k; i++)
    if ( a[i].second >= k )
      return a[i].first;
    else
      k -= a[i].second;

  if ( k ) return 1LL;
  return -1LL;
}

int main()
{
  ios_base::sync_with_stdio(false);
//  freopen("c.in", "r", stdin);
//  freopen("c.out", "w", stdout);

  int Q;  cin >> Q;
  for (int _case_ = 1; _case_ <= Q; _case_++)
  {
    cout << "Case #" << _case_ << ": ";
    LL N, K;  cin >> N >> K;
    LL lastRange = bestSolve(N, K);
    cout << lastRange/2LL << ' ' << (lastRange-1LL)/2LL << "\n";
  }
  return 0;
}
