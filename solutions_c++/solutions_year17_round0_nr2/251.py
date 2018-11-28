#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std ;
typedef unsigned long long ull ;
int main() {
   ull T, N ;
   cin >> T ;
   for (int kase=1; kase<=T; kase++) {
      cin >> N ;
      vector<int> digits ;
      while (N) {
         digits.push_back(N%10) ;
         N /= 10 ;
      }
      int tidy = 0 ;
      while (!tidy) {
         tidy = 1 ;
         for (int i=0; i+1<digits.size(); i++)
            if (digits[i] < digits[i+1]) {
               tidy = 0 ;
               digits[i+1]-- ;
               for (int j=0; j<=i; j++)
                  digits[j] = 9 ;
               break ;
            }
      }
      cout << "Case #" << kase << ": " ;
      for (int i=digits.size()-1; i>=0; i--)
         if (digits[i] > 0)
            cout << digits[i] ;
      cout << endl ;
   }
}
