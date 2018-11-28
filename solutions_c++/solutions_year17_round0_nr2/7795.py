#include <iostream>
using namespace std;

int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; i++) {
    string n;
    cin >> n;
    for (int j = 1; j < n.length(); j++) {
      if (n[j] < n[j - 1]) {
	n[j - 1]--;
	int r = j;
	while (j < n.length()) {
	  n[j] = '9';
	  j++;
	}
	for (int k = r - 1; k > 0; k--) {
	  if (n[k] < n[k - 1]) {
	    n[k] = '9';
	    n[k - 1]--;
	  }
	}
      }
    }
    n.erase(0, min(n.find_first_not_of('0'), n.size()-1));
    cout << "Case #" << i + 1 << ": " << n << endl;
  }
}
