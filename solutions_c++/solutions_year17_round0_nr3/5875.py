/*
	Google Code Jam - Tidy Numbers - Attempt #1
	-------------------------------------------
	Created by:   Ben Dittmer
	Created on:   04-08-2017
	Last updated: 04-08-2017
	-------------------------------------------

	This program will read in a string n of size n
	and returnd the largest integer with the digits
	in non-decreasing order.
*/

#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <cmath>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
int main() {
  int t, n, k, min, max, power;
  int div, remainder;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> n >> k;
    power = pow(2,floor(log(k)/log(2)));
    div  = (n-k)/power;
    remainder = (n-k)%power;
    if (remainder == 0) {
      min = int(div/2);
      max = min + div%2;
    }
    else if ((k+1)-power == 0) {
      min = div;
      max = div+1;
    }
    else if ((k+1)-power <= remainder){
      min = int(div/2);
      max = min + div%2;
    }
    else {
      min = int(div/2);
      max = min + div%2;
    }
    /*
    cout << "n: " << n << " " << "k: " << k << endl;
    cout << "div: " << div << endl;
    cout << "remainder: " << remainder << endl;
    cout << "power: " << power << endl;
    cout << endl;
    */
    cout << "Case #" << i << ": " << max << " " << min << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
  return 0;
}