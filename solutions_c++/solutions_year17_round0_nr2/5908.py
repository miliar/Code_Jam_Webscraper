#include <iostream>
#include <string>
#include <cmath>
using namespace std;


int main(int argc, char **argv) {
  int t;
  unsigned long long number, tidy;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  string s;

  for (int i = 1; i <= t; ++i) {
    cin >> number;

    s = std::to_string(number);

    tidy = number;


    for (unsigned long long j = 1; j < pow(10, s.length()-1); j*=10)
    {
      unsigned long long digit1, digit2;
      digit1 = (tidy/j) % 10;
      digit2 = (tidy/(j*10)) % 10;


      // cout << "Digit1: " << digit1 << endl;
      // cout << "Digit2: " << digit2 << endl;
      // cout << "--->" << digit1 << "|" << digit2 << endl;
      if (digit1 < digit2 || (digit1 == 0 && digit2 == 0))
      {
        // cout << "passs" << endl;
        tidy = tidy - (j*10);// + (9-digit1)*j;
        for (unsigned long long k = 1; k <= j; k*=10)
        {
            unsigned long long fill;
            fill = (tidy/k) % 10;

            tidy += (9-fill)*k;
        }
      }
      // cout << "---------->" << j << ":  " << tidy << endl;
    }
    // cout << "---------->" << tidy << ":  " << number << endl;
    // cout << "Case #" << i << ": " << (tidy < number ? tidy : number) << endl;
    cout << "Case #" << i << ": " << tidy  << endl;
  }
}