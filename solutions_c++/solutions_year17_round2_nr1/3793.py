#include <bits/stdc++.h>
typedef long long ll;

using namespace std;


int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.precision(20);
  int T;
  cin >> T;
  for (int t = 1;  t <= T; t++) {
    ll d, n;
    cin >> d >> n;
    vector<pair<ll, ll > > cab(n);
    for (int i = 0; i < n; i++) 
      cin >> cab[i].first >> cab[i].second;
    
    double ti = (d-cab[0].first)/double(cab[0].second);
    for (int i = 1; i < n; i++)
      ti = max (ti, (d-cab[i].first)/double(cab[i].second));
    
    cout << "Case #" << t << ": " << d/ti << endl;
  }
  return 0;
}
