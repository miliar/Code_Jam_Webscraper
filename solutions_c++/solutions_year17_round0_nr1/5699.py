#include <iostream>
using namespace std;
string flip(string pancakes, int position, int size) {
	for (int i = position; i < position + size; i++) {
		if (pancakes[i] == '+') {
			pancakes[i] = '-';
		} else {
			pancakes[i] = '+';
		}
	}
	return pancakes;
}

int main() {
  int t;
  string pancakes;
  string happy;
  int flipper;
  int attempts;
  int flips;
  int length;
  cin >> t;

  for (int i = 1; i <= t; ++i) {
    cin >> pancakes >> flipper;
    length = pancakes.length();
    flips = 0;
    attempts = 0;
    happy = string(length, '+');

    while(pancakes != happy && attempts < length * length) {
    	attempts++;

			for (int i = 0; i < length - (flipper - 1); i++){
    		if (pancakes[i] == '-') {
    			pancakes = flip(pancakes, i, flipper);
    			flips++;
    		}
    	}
    }

    if (attempts >= length * length) {
    	cout << "Case #" << i << ": IMPOSSIBLE" << endl;
    } else {
	    cout << "Case #" << i << ": " << flips << endl;
	  }
  }

  return 0;
}