#include <iostream>
#include <map>

using namespace std;

using ll = long long;

int main() {
  ios::sync_with_stdio(false);
  int tt;
  cin >> tt;
  for (int t = 1; t <= tt; ++t) {
    ll n, k;
    cin >> n >> k;
    map<ll, ll> M;
    M[n] = 1;
    while (k > 0) {
      auto it = M.end();
      --it;
      ll trec = it->second;
      ll len = it->first;
      ll a = (len - 1) / 2;
      ll b = len - 1 - a;
      if (k > trec) {
        if (a > 0) M[a] += trec;
        if (b > 0) M[b] += trec;
        k -= trec;
      } else {
        cout << "Case #" << t << ": " << b << ' ' << a << endl;
        break;
      }
      M.erase(it);
    }
  }
}
