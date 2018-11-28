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
using namespace std;  // since cin and cout are both in namespace std, this saves some text
int main() {
  int t;
  string n;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> n; 
    int changed_digit = -10;
    for (int j = 0; j < n.length()-1; j++) {
    	if (n[j] > n[j+1]) {
    		if (changed_digit == -10) {
    			changed_digit = j;
    		}
    		n[j+1] = '9';
    		if (changed_digit == j) {
    			n[j] = n[j] - 1;
    		}
    	}
    }

    for (int j = n.length()-1; j > 0; j--) {
    	if (n[j] < n[j-1]) {
    		n[j] = '9';
    		n[j-1] = n[j-1] -1;
    	}
    }

    n = n.erase(0, n.find_first_not_of('0'));
    cout << "Case #" << i << ": " << n << " " << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
    
  }
  return 0;
}