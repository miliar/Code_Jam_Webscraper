#include <iostream>

using namespace std;

int main() {
  int t;
  cin >> t;
  int cas = 1;
  while(t--) {
    string s;
    int k;
    cin >> s >> k;
    int range = s.size() - k;
    int n = 0;
    for(int i = 0; i <= range; ++i) {
      if(s[i] == '-') {
        for(int j = i; j < i + k; ++j) {
          s[j] = s[j] == '-' ? '+' : '-';
        }
        ++n;
      }
    }

    range = s.size() - range - 1;
    for(int i = s.size() - 1; i >= range; --i) {
      if(s[i] == '-') {
        for(int j = i; j > i - k; --j) {
          s[j] = s[j] == '-' ? '+' : '-';
        }
        ++n;
      }
    }

    bool correct = true;
    cout << "Case #" << cas << ": ";
    for(auto c : s) {
      if(c == '-') {
        correct = false;
        cout << "IMPOSSIBLE" << endl;
        break;
      }
    }
    if(correct) cout << n << endl;
    ++cas;
  }
  return 0;
};
