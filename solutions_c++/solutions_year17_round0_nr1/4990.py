#include <iostream>

using namespace std;

int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  int t;
  cin >> t;
  for (int ti = 0; ti < t; ++ti) {
    string s;
    int k;
    cin >> s >> k;
    int result = 0;
    for (int i = 0; i <= s.size()-k; ++i) {
      if (s[i] == '-') {
        result++;
        for (int j = 0; j < k; ++j) {
          s[i+j] = s[i+j] == '-' ? '+' : '-';
        }
      }
    }
    bool f=1;
    for (int i = 0; i < s.size(); ++i) if (s[i] == '-') f=0;
    cout << "Case #" << ti+1 << ": ";
    if (f) cout << result << endl;
    else cout << "IMPOSSIBLE\n";
  }
}
