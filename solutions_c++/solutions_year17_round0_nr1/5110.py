#include <iostream>
#include <string>

using namespace std;

int main() {
  ios::sync_with_stdio();

  int cases;
  cin >> cases;

  for (int c = 1; c <= cases; ++c) {
    string in;
    int n, cont = 0;
    getline(cin, in, ' ');
    cin >> n;
    for (int j = 0; j <= in.size()-n; ++j) {
      if (in[j] == '-') {
	cont++;
	for (int i = j; i < j + n; ++i) {
	  in[i] = (in[i] == '+')? '-' : '+';
	}
      }
    }

    string::size_type pew;
    pew = in.find("-");

    cout << "Case #" << c << ": ";
    if (pew == string::npos) {
      cout << cont;
    } else {
      cout << "IMPOSSIBLE";
    }
	      cout << endl;
    
  }
  
  return 0;
}
