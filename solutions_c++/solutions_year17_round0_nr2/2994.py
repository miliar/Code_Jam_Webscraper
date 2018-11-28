#include <iostream>
#include <vector>
#include <string>

using std::cin;  using std::cout;  using std::endl;
using std::vector; using std::string;

int main() {

  int T;
  cin >> T;

  string s;
  getline(cin,s);

  long N, currentN, cN;

  for (int i=1; i<=T; ++i) {

    string digits;
    getline(cin, digits);

    int len = digits.length();

    int count = 0;
    for (int j = 0; j < len-1;  ++j) {
      if (digits[j] <= digits[j+1])
	continue;
      else {
	if (digits[j] == '0') {
	  digits[j] = '9';
	  --digits[j-1];
	}
	else 
	  --digits[j];
	int k = 1;
	while ( j-k>=0 && digits[j-k] > digits[j-k+1] ) {
	  if (digits[j-k] == '0') {
	    digits[j-k] = '9';
	    --digits[j-k-1];
	  }
	  else 
	    --digits[j-k];
	  digits[j-k+1] = '9';
	  ++k;
	}
	for (int k = j+1; k < len;  ++k) {
	  digits[k] = '9';
	}
	break;
      }
    }

    cout << "case #" << i << ": ";
    if (digits[0] == '0') {
      int j=1;
      while (j<len) {
	cout << digits[j];
	++j;
      }
      cout << endl;
    }
    else
      cout << digits << endl;
  }

  return 0;
}
