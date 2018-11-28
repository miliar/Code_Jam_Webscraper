#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef pair<ll, ll> pll;


int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.precision(20);
  const long double pi = 3.14159265358979323846L;
  int T;
  cin >> T;
  for (int t = 1;  t <= T; t++) {
    int n, k;
    cin >> n >> k;
    vector<ll> r(n), h(n);    
    vector<pll> pr(n);

    for (int i = 0; i < n; i++) {
      cin >> r[i] >> h[i];
      pr[i] = pll(r[i], 2*r[i]*h[i]);
    }

    sort(pr.begin(), pr.end());
    ll sum = 0;
    priority_queue<ll, vector<ll>, greater<ll> > grans;
    for (int i = 0; i < k-1; i++) {
      grans.push(pr[i].second);
      sum += pr[i].second;
    }
    ll best = 0;
    for (int i = k-1; i < n; i++) {
      ll cand = pr[i].second + pr[i].first*pr[i].first + sum;
      best = max(best, cand);
      grans.push(pr[i].second);
      sum += pr[i].second;
      sum -= grans.top();
      grans.pop();
    }
    
    cout << "Case #"  << t << ": " << best*pi << "\n";
  }
  return 0;
}
