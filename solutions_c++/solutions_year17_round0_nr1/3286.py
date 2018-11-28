#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <vector>
#include <stdint.h>
#include <algorithm>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

vector<bool> flip;
vector<int8_t> current_cake;
int pos_len;
int flip_len;

bool tryFlip(int pos) {
	if (pos == pos_len) {
		return (find(current_cake.begin(), current_cake.end(), 0) == current_cake.end());
	}
	else if (tryFlip(pos+1)) {
		return true;
	}
	else {
		for (int i = pos; i < pos+flip_len; ++i) {
			current_cake[i] ^= 1;
		}
		flip[pos] = true;
		if (tryFlip(pos+1)) {
			return true;
		}
		else {
			for (int i = pos; i < pos+flip_len; ++i) {
				current_cake[i] ^= 1;
			}
			flip[pos] = false;
			return false;
		}
	}
}

string flipCake(string& cake, int flipper) {
	current_cake = vector<int8_t>(cake.size(), 0);
	for (size_t i = 0; i < cake.size(); ++i) {
		if (cake[i] == '+') {
			current_cake[i] = 1;
		}
	}
	pos_len = (int)cake.size() - flipper + 1;
	flip_len = flipper;
	flip = std::vector<bool>(pos_len, false);
	if (tryFlip(0)) {
		size_t rtn = 0;
		for (const bool v : flip) {
			if (v) {
				++rtn;
			}
		}
		return to_string(rtn);
	}
	else {
		return "IMPOSSIBLE";
	}
}

int main() {
  int t, f;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  cin.ignore();
  string cake;
  for (int i = 1; i <= t; ++i) {
    getline(cin, cake, ' ');
    cin >> f;
    cin.ignore();
    cout << "Case #" << i << ": " << flipCake(cake, f) << endl;
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
    // out put
    // Case #x: y
  }
}