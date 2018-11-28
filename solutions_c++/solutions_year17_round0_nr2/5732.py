#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>

using namespace std;  // since cin and cout are both in namespace std, this saves some text
int main() {
  int t, n, m;
  string inputNumber;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  //cout << t << endl;
  for (int j = 1; j <= t; ++j) {
    cin >> inputNumber;  // read n and then m.
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.

    // Check if current number is valid, then return

    int invalidPoint = 0;

    // keep looping while invalid
    while (1){


      int prevDigit = inputNumber.at(0) - '0';
      if (prevDigit == 0){
        // remove the first digit of zero
        inputNumber = inputNumber.substr(1, inputNumber.size() - 1);
        prevDigit = inputNumber.at(0) - '0';
      }


      // check if valid
      bool isValid = true;
      for (int i = 1; i < inputNumber.length(); i++){
        int currDigit = inputNumber.at(i) - '0';

        if (currDigit < prevDigit){
          isValid = false;
        }
        prevDigit = currDigit;
      }

      if (isValid) { break; }

      prevDigit = inputNumber.at(0) - '0';

      //cout << "Not valid: " << inputNumber << endl;
      // fix since invalid
      for (int i = 1; i < inputNumber.length(); i++){

        int currDigit = inputNumber.at(i) - '0';

        if (currDigit < prevDigit){
          // Change digit - 1 to digit
          //cout << "Changing digit " << inputNumber[i] << " to " << currDigit << endl;


          inputNumber[i - 1] = '0' + (inputNumber.at(i - 1) - '0' - 1);
          for (int k = 0; i + k < inputNumber.length(); k++){
            // change everything after to 9
            inputNumber[i + k] = '9';
          }
          break;

          //invalidPoint = i;

        }

        prevDigit = currDigit;

      }

      //cout << inputNumber << endl;
    }



    cout << "Case #" << j << ": " << inputNumber << endl;


  }

  return 0;

}
