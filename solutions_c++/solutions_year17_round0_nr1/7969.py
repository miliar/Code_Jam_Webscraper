#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main () {
  long long t;
  cin >> t;
  string pancakes;
  int flipper, flips = 0;
  for (int j = 0; j < t; j++) {
    cin >> pancakes >> flipper;
    flips = 0;
    for (int i = 0; i < pancakes.size() - flipper + 1; i++) {
      if (pancakes[i] == '-') {
	flips ++;
	for (int k = i; k < i + flipper; k++) {
// 	  cout << k << i << endl;
	  if (pancakes[k] == '-') {
	    pancakes[k] = '+';
	  } else {
	    pancakes[k] = '-';
	  }
	}
      }
//       cout << pancakes << endl;
    }
    bool onlySmiles = true;
    for (int i = 0; i < pancakes.size(); i++) {
      if (pancakes[i] == '-') {
	onlySmiles = false;
      }
    }
    if (onlySmiles) {
      cout << "Case #" << j + 1 << ": " << flips << endl;
    } else {
      cout << "Case #" << j + 1 << ": IMPOSSIBLE" << endl;
    }
  }
  return 0;
}