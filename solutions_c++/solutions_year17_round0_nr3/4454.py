#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

void solve(ll N, ll K, int t) {
  priority_queue<ll> q;
  q.push(N);
  ll x = 0, y = 0;
  for (int i = 0; i < K; i++) {
    ll n = q.top();
    q.pop();
    n -= 1;
    if (n % 2 == 0) {
      x = n/2;
      y = x;
    } else {
      y = n/2;
      x = y+1;
    }
    q.push(x);
    q.push(y);
  }
  cout << "Case #" << t << ": " << x << " " << y << endl;
}


int main() {
  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    ll N, K;
    cin >> N >> K;
    solve(N, K, t);
  }
  return 0;
}
