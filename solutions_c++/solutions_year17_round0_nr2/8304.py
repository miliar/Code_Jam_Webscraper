#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
int main() {
  int t, n,count,skip,switched;
  string max_number;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> max_number;  // read max number read.    
    switched = max_number.length();
    for(int j = max_number.length() - 1; j > 0; j--) {
        if (max_number[j] < max_number[j-1]) {
            max_number[j-1] = max_number[j-1] - 1;
            switched = j;
        }
    }
    skip = 1;
    cout << "Case #" << i << ": ";
    for(int j = 0; j < max_number.length(); j++) {
        if (j >= switched) {
            max_number[j] = '9';
        }
        if (max_number[j] == '0') {
            if (skip == 1) {
                skip = 0;
                continue;
            }
        }
        cout << max_number[j];
    }      
    cout << endl;
  }
  return 0;
}