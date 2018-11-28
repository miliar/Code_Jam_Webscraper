#include <iostream>
#include <algorithm>
#include <string>
typedef long long ll;
using namespace std;

inline bool ascending(string a) {
  for (int i = 1; i < a.size(); i++)
    if (a[i] < a[i - 1])
      return false;
  return true;
}

template <typename Type>
inline printCase(int i, Type sol) {
  cout << "Case #" << i << ": " << sol << endl;
}

int main() {
  int T; cin >> T;
  for (int test = 1; test <= T; test++) {
    string a; cin >> a;
    while (!ascending(a)) {
      int found = -1;
      for (int i = 0; i < a.size() - 1; i++) {
        if (a[i] > a[i + 1]) {
          found = i;
          break;
        }
      }
      
      a[found]--;
      for (int i = found +1; i < a.size(); i++) {
        a[i] = '9';
      }
      if (found == 0 && a[found] == '0') {
        a.erase(0, 1);
      }
    }
    printCase(test, a);
  }
}