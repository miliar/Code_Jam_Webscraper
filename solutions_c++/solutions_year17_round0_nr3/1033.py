#pragma GCC optimize ("O2")
#include <bits/stdc++.h>
#include <unistd.h>

using namespace std;

#define IOS ios_base::sync_with_stdio(0); cin.tie(0)
#define fst first
#define snd second
typedef long long ll;

template<typename A, typename B>
ostream& operator <<(ostream& s, const pair<A, B>& p)
{
  return s << "(" << p.first << "," << p.second << ")";
}
template<typename T>
ostream& operator <<(ostream& s, const vector<T>& c)
{
  s << "[ ";
  for (auto it : c) s << it << " ";
  s << "]";
  return s;
}

int main()
{
  IOS;
  int T;
  cin >> T;
  ll n, k;
  for (int tt = 1; tt <= T; ++tt) {
    cin >> n >> k;
    
    ll tmp = 1;
    int cnt = 0;
    while (2 * tmp - 1 < k) {
      tmp *= 2;
      cnt++;
    }
    // the cnt-th round
    ll remain = k - tmp + 1;

    ll empty = n - tmp + 1;
    ll size = empty / tmp;
    ll plusone = empty % tmp;

    if (remain > plusone)
      size -= 1;

    cout << "Case #" << tt << ": ";
    cout << (size / 2 + (size & 1)) << " " << (size / 2) << endl;
  }
  return 0;
}
