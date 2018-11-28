#include <iostream>
using namespace std;

int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; i++) {
    string t;
    cin >> t;
    int r;
    cin >> r;
    int num = 0;
    for (int j = 0; j < t.length() - r + 1; j++) {
      if (t[j] == '-') {
	num++;
	for (int l = 0; l < r; l++) {
	  if (t[l + j] == '-') {
	    t[l + j] = '+';
	  } else {
	    t[l + j] = '-';
	  }
	}
      }
    }
    bool good = true;
    for (int j = 0; j < t.length(); j++) {
      if (t[j] == '-') {
	good = false;
	break;
      } 
    }
    if (good) {
      cout << "Case #" << i + 1 << ": " << num << endl;
    } else {
      cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
    }
  }
}
