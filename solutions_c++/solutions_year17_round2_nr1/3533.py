#include<bits/stdc++.h>
using namespace std;

#define endl '\n'
#define D(x) cout << #x << " = " << (x) << endl;

int main() {
  int TC = 1;
  int T;
  cin >> T;
  
  while (T --> 0) {
  int x, n;
  cin >> x >> n;
  
  double ans = 0;
  for (int i = 0; i < n; ++i) {
    double t, v;
    cin >> t >> v;
    double tmp = (x - t) / v;
    ans = max(tmp, ans);
  }
  
  cout << "Case #" << TC ++ << ": ";
  cout << fixed << setprecision(20) << x / ans << endl;
  
  }
  return 0;
}
