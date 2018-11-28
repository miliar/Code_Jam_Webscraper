#include <iostream>

typedef unsigned int ui;
using namespace std;


void flip(string& pancakes, ui k, ui j) {
  pancakes[j] = '+';
  for (ui i = j + 1; i < j + k; ++i)
    if (pancakes[i] == '+')
      pancakes[i] = '-';
    else
      pancakes[i] = '+';
}


int main() {
  ui t, k;
  cin >> t;
  string pancakes;

  for (ui i = 0; i < t; ++i) {
    cin >> pancakes >> k;
    bool impossible = false;
    ui flips = 0;

    for (ui j = 0; j < pancakes.size(); ++j) 
      if (pancakes[j] == '-') {
        if (j < pancakes.size() - k + 1) {
          flip(pancakes, k, j);
          ++flips;
        } else {
          impossible = true;
          break;
        }
      }
    if (!impossible)
      cout << "Case #" << i + 1 << ": " << flips << "\n";
    else
      cout << "Case #" << i + 1 << ": " << "IMPOSSIBLE"<< "\n";
  }
}
