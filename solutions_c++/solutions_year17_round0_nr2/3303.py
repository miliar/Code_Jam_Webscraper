#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

int main() {
  int t;
  string n;
  scanf("%d", &t);
  for (int cas = 1; cas <= t; ++cas) {
    cin >> n;
    for (int i = 0; i < n.size() - 1; ++i) {
      bool found = false;
      for (int j = i + 1; j < n.size(); ++j) {
        if (n[i] < n[j])
          break;
        if (n[i] > n[j]) {
          found = true;
          break;
        }
      }
      
      if (found) {
        n[i]--;
        for (int j = i + 1; j < n.size(); ++j)
          n[j] = '9';
      }
    }

    for (int i = 0; n[i] == '0'; ++i)
      n.erase(n.begin() + i);
    cout << "Case #" << cas << ": " << n << endl;
  }
  return 0;
}
