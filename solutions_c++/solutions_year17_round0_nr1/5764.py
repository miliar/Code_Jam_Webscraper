#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>

using namespace std;  // since cin and cout are both in namespace std, this saves some text
int main() {
  int t, n, m;
  string inputNumber;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  //cout << t << endl;
  for (int j = 1; j <= t; ++j) {
    cin >> inputNumber >> n;  // read n and then m.
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.

    // Check if current number is valid, then return

    // keep looping while invalid

    bool possible = true;
    int numFlips = 0;
    for (int i = 0; i < inputNumber.size(); i++){

      if (inputNumber.at(i) == '-'){
        numFlips++;
        if (i + (n - 1) > inputNumber.size() - 1){
          possible = false;
          break;
        }
        // flip this and consecutive k
        for (int k = 0; k < n; k++){
          if (inputNumber.at(i + k) == '+'){
            inputNumber[i + k] = '-';

          } else {
            inputNumber[i + k] = '+';
          }

        }
      }


    }



    if (!possible){
      cout << "Case #" << j << ": " << "IMPOSSIBLE" << endl;

    } else {
      cout << "Case #" << j << ": " << numFlips << endl;
      
    }


  }

  return 0;

}
