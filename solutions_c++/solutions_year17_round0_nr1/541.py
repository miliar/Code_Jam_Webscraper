#include <iostream>
#include <vector>
#include <cstdlib>

using namespace std;

vector<string> split(string s, char c) {
  char buf[1024];
  int l = 0;
  vector<string> rax;
  for (char x : s) {
    if (x == c) {
      rax.push_back(string(buf, l));
      l = 0;
    }
    else {
      buf[l++] = x;
    }
  }
  return rax;
}

int main (int argc, char* argv[]) {
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    string pancake;
    int k;
    cin >> pancake;
    cin >> k;
    int flips = 0;
    for (int j = 0; j < pancake.size() - k + 1; ++j) {
      if (pancake[j] == '-') {
        for (int l = 0; l < k; ++l) {
          pancake[j + l] = (pancake[j + l] == '-' ? '+' : '-');
        }
        flips++;
      }
    }
    bool success = true;
    for (char c : pancake) {
      if (c == '-') success = false;
    }
    if (success)
      cout << "Case #" << i + 1 << ": " << flips << endl;
    else
      cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
  }
}
