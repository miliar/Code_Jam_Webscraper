#include <bits/stdc++.h>

using namespace std;

typedef long long ll;


priority_queue<ll> q;

ll n, k;

void read() {
  cin >> n >> k;
}

void kill() {
  q = priority_queue<ll>();
  q.push(n);
  for (int i = 0; i < k; ++i) {
    ll len = q.top();
    --len;

    q.pop();
    ll l = len / 2;
    ll r = (len + 1) / 2;

    q.push(l);
    q.push(r);

    if (i + 1 == k)
      cout << r << " " << l << endl;
  }
}

int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cout << "Case #" << i << ": ";
    read();
    kill();
    cerr << "Case #" << i << " done.\n";
  }
  return 0;
}
