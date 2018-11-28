#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

int T, n;
string s;
vector<int> buf;

string solve() {
  if (n == 1) {
    return s;
  }
  buf.clear();
  for (int i = 0; i < n; ++i) {
    buf.push_back(s[i] - '0');
  }
  for (int i = 1; i < n; ++i) {
    if (buf[i] < buf[i-1]) {
      int j = i;
      while (j >= 1) {
        if (buf[j] < buf[j-1]) {
          --buf[j-1];
          --j;
        } else {
          break;
        }
      }
      for (int k = j+1; k < n; ++k) {
        buf[k] = 9;
      }
      break;
    }
  }
  int i;
  for (i = 0; i < n; ++i) {
    if (buf[i] == 0)
      continue;
    break;
  }
  ostringstream ss;
  for (; i < n; ++i) {
    ss << buf[i];
  }
  return ss.str();
}

int main() {
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cin >> s;
    n = s.length();
    cout << "Case #" << t << ": " << solve() << endl;
  }
  return 0;
}