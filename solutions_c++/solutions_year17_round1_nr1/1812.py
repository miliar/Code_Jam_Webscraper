#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using std::cin;  using std::cout;  using std::endl;
using std::vector; using std::string;

int main() {

  int T;
  cin >> T;

  for (int i=1; i<=T; ++i) {

    int R, C;
    cin >> R;
    cin >> C;

    char nl;
    vector<vector<char> > cake(R);
    for (int r = 0; r< R;  ++r) {
      cake[r] = vector<char>(C);
      for (int c = 0; c< C;  ++c) {
	cin >> cake[r][c];
      }
    }

    char last;

    for (int r = 0; r< R;  ++r) {
      last = '?';
      for (int c = 0; c< C;  ++c) {
	if (cake[r][c] != '?') {
	  last = cake[r][c];
	  int i = 1;
	  while (c>0 && i<=c && cake[r][c-i] == '?') {
	    cake[r][c-i] = cake[r][c];
	    ++i;
	  }
	}
	else if (last != '?')
	  cake[r][c] = last;
      }
    }

    for (int c = 0; c< C;  ++c) {
      last = '?';
      for (int r = 0; r< R;  ++r) {
	if (cake[r][c] != '?') {
	  last = cake[r][c];
	  int i = 1;
	  while (r>0 && i<=r && cake[r-i][c] == '?') {
	    cake[r-i][c] = cake[r][c];
	    ++i;
	  }
	}
	else if (last != '?')
	  cake[r][c] = last;
      }
    }

    cout << "case #" << i << ": " << endl;
    for (int r = 0; r< R;  ++r) {
      for (int c = 0; c< C;  ++c) {
	cout << cake[r][c] ;
      }
      cout << endl;
    }
  }

  return 0;
}
