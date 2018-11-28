#include <iostream>

using namespace std;

int main() {
  int t;
  cin >> t;
  int cas = 0;
  while(t--) {
    ++cas;
    cout << "Case #" << cas << ": ";
    string n;
    cin >> n;
    if(n.size() == 1) {
      cout << n << endl;
      continue;
    }
    int i;
    for(i = 0; i < n.size() - 1; ++i) {
      if(n[i] > n[i+1]) {
        n[i] -= 1;
        for(int j = i+1; j < n.size(); ++j) n[j] = '9';
      }
    }
    for(; i > 0; --i) {
      if(n[i-1] > n[i]) {
        n[i-1] -= 1;
        n[i] = '9';
      }
    }
    if(n[0] == '0') n = n.substr(1);
    cout << n << endl;
  }
  return 0;
};
