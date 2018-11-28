#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <numeric>
#include <map>
#include <set>
#include <tuple>
#include <string.h>

typedef long long ll;
using namespace std;

tuple<ll, ll> solve(ll N, ll K) {
  map<ll, ll> m;
  ll n1 = 0, n2 = 0;
  m[N] = 1;
  while (K > 0) {
    ll next, num;
    tie(next, num) = *(--m.cend());
    m.erase(--m.cend());
    //cout << "next=" << next << ", num=" << num << ", K=" << K << endl;
    if ((next-1) % 2 == 0) {
      n1 = (next-1)/2;
      n2 = n1;
      K -= num;
      if (n1 > 0)
        m[n1] += num*2;
    } else {
      n1 = next/2;
      n2 = (next-2)/2;
      K -= num;
      m[n1] += num;
      if (n2 > 0)
        m[n2] += num;
    }
  }
  return make_tuple(n1, n2);
}

int main()
{
  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    ll N, K;
    cin >> N >> K;
    ll y, z;
    tie(y, z) = solve(N, K);
    cout << "Case #" << i+1 << ": " << y << " " << z << "\n";
  }
}
