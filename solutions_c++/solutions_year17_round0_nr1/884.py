#include <iostream>
#include <vector>
#include <queue>
#include <string>

using namespace std;

vector<bool> flip(vector<bool> s, int size, int start) {
  for (int i = 0; i < size; i++) {
    s[start + i] = !s[start + i];
  }
  return s;
}

int main() {
  int num;
  cin >> num;
  for (int i = 1; i <= num; i++) {
    int res = 0, k;
    bool flag = true;
    string in;
    cin >> in;
    cin >> k;
    int len = in.size();

    vector<bool> inb(in.size());
    transform(in.begin(), in.end(), inb.begin(), [](char c) { return c == '+'; });
    for (int j = 0; j <= len - k; j++) {
      if (!inb[j]) {
        inb = flip(inb, k, j);
        res++;
      }
    }
    for (int j = len - k + 1; j < len; j++) {
      if (!inb[j]) {
        flag = false;
        cout << "Case #" << i << ": IMPOSSIBLE" << endl;
        break;
      }
    }
    if (flag) cout << "Case #" << i << ": " << res << endl;
  }
  return 0;
}
