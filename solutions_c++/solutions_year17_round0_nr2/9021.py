/*
 * Name: Serena Shi
 * Date: 4/7/2017
 */

#include <iostream>
#include <cmath>

using namespace std;

bool isTidy( long int n ) {
    if( n < 10 )
      return true;
    else {
      int k = n % 10;
      n /= 10;
      int l = n % 10;

      if( k >= l )
        return isTidy(n);
      return false;
    }
}

int main() {
  long int t, n;
  
  // take in number of test cases
  cin >> t;

  // iterate through test cases
  for( int i = 1; i <= t; i++ ) {
    // get input value
    cin >> n;

    while( !isTidy(n) )
      n--;

    cout << "Case #" << i << ": " << n << endl;
  }

  return 0;
}
