#include<iostream>
#include<string>

using namespace std;

bool allUp(bool v[], int n) {
  for (int i = 0; i < n; i++) {
    if (!v[i]) {
      return false;
    }
  }
  return true;
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    string s;
    cin >> s;
    int k;
    cin >> k;
    int n = s.length();
    bool v[n];
    for (int i = 0; i < n; i++) {
      if (s[i] == '+') {
        v[i] = true;
      } else {
        v[i] = false;
      }
    }
    int r = 0;
    for (int i = 0; i < n - k + 1; i++) {
      if (!v[i]) {
        r++;
        for (int j = i; j < i + k; j++) {
          v[j] = !v[j];
        }
      }
    }
    cout << "Case #" << t << ": ";
    if (allUp(v, n)) {
      cout << r;
    } else {
      cout << "IMPOSSIBLE";
    }
    cout << endl;
  }
}
