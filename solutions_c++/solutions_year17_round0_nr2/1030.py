#include <bits/stdc++.h>

using namespace std;



typedef long long ll;
ll solve(ll N) {
  ll M=N, last=9, p=1, cur=1;
  while (M) {
    ll d = M % 10;
    if (d>last) {
      N -= cur;
      cur = 0;
      last = d ? d-1 : 9;
    } else {
      last = d;
    }
    cur += d*p;
    M /= 10;
    p *= 10;
  }
  return N;
}

int main() {
  int n;
  cin >> n;
  for (int i = 1; i <= n; ++i) {
    ll N;
    cin >> N;
    cout << "Case #" << i << ": " << solve(N) << endl;
  }
  return 0;
}
