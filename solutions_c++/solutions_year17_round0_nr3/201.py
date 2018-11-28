#include <bits/stdc++.h>
using namespace std;

#define int long long
#define inf 1000000007LL

#define rep(i, n) for(int i = 0; i < (n); i++)
#define rrep(i, n) for(int i = (n) - 1; i >= 0; i--)
#define trep(i, n) for(int i = 0; i <= (n); i++)
#define rep1(i, n) for(int i = 1; i <= (n); i++)
#define mfor(i, s, t) for(int i = (s); i < (t); i++)
#define tfor(i, s, t) for(int i = (s); i <= (t); i++)

signed main() {
  int t;
  cin >> t;
  rep1(_, t) {
    int n, k;
    cin >> n >> k;
    map<int, int> mp;
    mp[n] = 1;
    while(1) {
      auto it = mp.end();
      it--;
      int a = it->first;
      int b = it->second;
      mp.erase(it);
      if(k <= b) {
        cout << "Case #" << _ << ": " << (a - 1) - (a - 1) / 2 << " " << (a - 1) / 2 << endl;
        break;
      }
      mp[(a - 1) / 2] += b;
      mp[(a - 1) - (a - 1) / 2] += b;
      k -= b;
    }
  }
}
