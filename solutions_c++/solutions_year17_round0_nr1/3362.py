#include <bits/stdc++.h>
using namespace std;

int main() {
  string s;
  int T, K;
  cin >> T;
  
  for (int t=1; t<=T; t++) {
    vector<int> p;
    int ans=0;
    cin >> s;
    cin >> K;
    for (auto c : s)
      p.push_back(c=='+' ? 0 : 1);
    for (unsigned int i=0; i<p.size()-K+1; i++) {
      if (p[i]==1) {
        ans++;
        for (int j=0; j<K; j++) {
          p[i+j] ^= 1;
        }
      }
    }
    for (unsigned int i=p.size()-K; i<p.size(); i++) {
      if (p[i]) ans = -1;
    }

    cout << "Case #" << t << ": ";
    if (ans == -1) {
      cout << "IMPOSSIBLE" << endl;
    } else {
      cout << ans << endl;
    }
  }
}