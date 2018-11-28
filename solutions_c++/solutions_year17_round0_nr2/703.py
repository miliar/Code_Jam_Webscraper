#include <iostream>
using namespace std;
void prop(string &n, int i) {
  if (i + 1 == n.size()) return;
  prop(n, i + 1);
  if (n[i] > n[i + 1]) {
    for (int j = i + 1; j < n.size(); j++) n[j] = '9';
    n[i] -= 1;
  }
}
int main() {
  int t, tt;
  string n;
  cin >> t;
  for (tt = 1; tt <= t; tt++) {
    cin >> n;
    prop(n, 0);
    if (n[0] == '0') n = n.substr(1);
    cout << "Case #" << tt << ": " << n << endl;
  }
  return 0;
}
