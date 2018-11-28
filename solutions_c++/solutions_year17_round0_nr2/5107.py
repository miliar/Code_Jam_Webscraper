#include <iostream>
#include <string>
typedef long long ll;

using namespace std;

int main() {
  ios::sync_with_stdio(false);

  int cases;
  string n;
  cin >> cases;

  for (int c = 1; c <= cases; ++c) {
    cin >> n;
    char a = n[0];
    int last = a;
    int lastpos = 0;
    bool tidy = true;
    for (int i = 1; i < n.size(); ++i) {
      char b = n[i];
      if (a > b) {
	tidy = false;
	break;
      } else if (a != b) {
	last = b;
	lastpos = i;
      }
      a = b;
    }

    if (!tidy) {
      --n[lastpos];
      for (int i = ++lastpos; i < n.size(); ++i) {
	n[i] = '9';
      }
    }

    cout << "Case #" << c << ": ";
    if (n[0] != 48) cout << n[0];
    for (int i = 1; i < n.size(); ++i) {
      cout << n[i];
    }
    cout << endl;
  }
  
  
  return 0;
}
