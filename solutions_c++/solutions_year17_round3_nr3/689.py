#include <bits/stdc++.h>
typedef long long ll;

using namespace std;

vector<long double> p;

bool check(long double l, long double u) {
  int n = p.size();
  long double t = 0;
  for (int i = 0; i < n; i++)
    if (l > p[i]) t += (l-p[i]);
  return (t <= u);
}

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.precision(20);
  int T;
  cin >> T;
  for (int t = 1;  t <= T; t++) {
    int n, k; 
    cin >> n >> k;
    long double u;
    cin >> u;
    p = vector<long double>(n);
    for (int i = 0; i < n; i++)
      cin >> p[i];
    long double ld = 0., lu = 1.;
    while (lu - ld > 1.e-15) {
      long double l = 0.5*(ld + lu);
      if (check(l, u)) ld = l;
      else lu = l;
    }
    long double pr = 1.;
    for (int i = 0; i < n; i++) {
      pr *= max(p[i], ld);
    }
    
    cout << "Case #" << t << ": " << pr << "\n";
  }
  return 0;
}
