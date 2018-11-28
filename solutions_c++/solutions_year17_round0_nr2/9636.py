#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <cstdint>
#include <sstream>

using namespace std;  // since cin and cout are both in namespace std, this saves some text
int main() {
  int t;
  uint64_t num;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> num;
    string number;
    ostringstream convert;

    convert << num;
    number = convert.str();

    string output = "";

    for(int i = number.length() - 1; i >= 0; i--){
            if(i > 0){
                if(number[i] - '0' < number[i - 1] - '0'){
                    number[i - 1] = ((number[i - 1] - '0') - 1) + '0';
                    output = "";
                    for(int j = number.length() - 1; j >= i; j--){
                        output += '9';
                    }
                }
                else{
                    output = number[i] + output;
                }
            }
            else{
                if(number[i] - '0' != 0)
                    output = number[i] + output;
            }
    }

    cout << "Case #" << i << ": " << output << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
}