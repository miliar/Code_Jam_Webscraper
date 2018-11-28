#include <iostream>
using namespace std;
int main(){
   long t,n;
   cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
   for (int i = 1; i <= t; ++i) {
      cin >> n;
      long bitLength = n;
      long x = 10;
      long left, right;
      while(bitLength) {
         bitLength /= 10;
		 left = n % x;  
         right = (n % (x * 10)) / 10; 
         if (left >= right) {
            x = x*10;
			continue; 
         }
         n = n / x * x - 1;
         x = x*10;
      }
      cout << "Case #" << i << ": " << n  << endl;
   }

}
