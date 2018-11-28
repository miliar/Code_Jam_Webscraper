#include <iostream>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int t=1; t<=T; t++) {

  cout << "Case #" << t << ": ";

  string s;
  int k;

  cin >> s >> k;

  string good_s(s.length(), '+');

  int max_flippable_index = s.length() - k;

  bool possible = false;
  int min_flips = s.length() + 1;

  for (int bitmask=0; bitmask<(2<<max_flippable_index); bitmask++) {
    int flips = 0;
    string flipped_s = s;
    for (int j=0; j<=max_flippable_index; j++) {
      if ((1 << j) & bitmask) {
        flips++;
        for (int u=j; u<j+k; u++) {
          if (flipped_s.at(u) == '+') flipped_s.at(u) = '-';
          else flipped_s.at(u) = '+';
        }
      }
    }
    if (flipped_s == good_s) {
      possible=true;
      min_flips = min(flips, min_flips);
    }
  }

  if (possible) {
    cout << min_flips << endl;
  }
  else {
    cout << "IMPOSSIBLE" << endl;
  }

  }
}
