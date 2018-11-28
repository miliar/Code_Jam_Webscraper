#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

map<ll,ll> m;
ll N, K;

inline void solve(ll a, ll multi){
  if(a <= 0) return;
  if(a % 2LL){
    m[-a] += multi;
    solve(a / 2LL, 2LL * multi);
  } else {
    m[-a] += multi;
    m[-(a/2LL)] += multi;
    if(a >= 4){
      m[-(a/2LL-1)] += multi;
      ll tmp = (a / 2LL - 1LL) / 2;
      solve(tmp, 3LL * multi);
      solve(tmp + ((a/2LL-1LL)%2 ? 1LL : -1LL), multi);
    }
  }
}

int main()
{
  ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
  int T; cin >> T;

  for(int cases = 1; cases <= T; cases++){
    m.clear(); cin >> N >> K;
    solve(N,1LL);
    cout << "Case #" << cases << ": ";
    for(auto it = m.begin(); it != m.end(); it++){
      if(it->second >= K){
        ll tmp = -it->first;
        if(tmp % 2)
          cout << tmp / 2LL << " " << tmp / 2LL << "\n";
        else
          cout << tmp / 2LL << " " << tmp / 2LL - 1 << "\n";
        break;
      } else {
        K -= it->second;
      }
    }
  }
}
