#include <bits/stdc++.h>
typedef long long ll;

using namespace std;

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL);
  int T;
  cin >> T;
  for (int t = 1;  t <= T; t++) {
    string s;
    int k; 
    cin >> s >> k;
    int n = s.size();
//    cerr << "n = " << n << endl; 
    vector<int> p(n, 0);
    for (int i = 0; i < n; i++)
      if (s[i] == '+') p[i] = 1;
//    for (int i = 0; i < n; i++)
//      cerr << p[i] << " ";
//    cerr << endl;
    vector<bool> fl(k, false);
    int flips = 0, tf = 0;
    for (int i = 0; i + k <= n; i++) {
      if (fl[i%k]) {
        fl[i%k] = false;
        flips--;
      }
      if ((p[i] + flips)%2 == 0) {
        flips++;
        fl[i%k] = true;
        tf++;
      }
//      cerr << "i = "  << i << ", flips = " << flips << ", tf = " << tf << endl;
    }
    bool cara = true;
    for (int i = n + 1 - k; i < n; i++) {
      if (fl[i%k]) {
        fl[i%k] = false;
        flips--;
      }
      if ((p[i] + flips)%2 == 0) cara = false;
    }
    cout << "Case #" << t << ": ";  
    if (!cara) cout << "IMPOSSIBLE\n";
    else cout << tf << "\n";
  }
  return 0;
}
