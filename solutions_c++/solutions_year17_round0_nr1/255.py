#include <iostream>
#include <vector>
#include <string>
using namespace std ;
int main() {
   int T, K ;
   string s ;
   cin >> T ;
   for (int kase=1; kase<=T; kase++) {
      cin >> s >> K ;
      int r = 0 ;
      for (int i=0; i<=s.size()-K; i++)
         if (s[i] == '-') {
            r++ ;
            for (int j=0; j<K; j++)
               s[i+j] = '+' + '-' - s[i+j] ;
         }
      for (int i=0; i<s.size(); i++)
         if (s[i] == '-')
            r = -1 ;
      cout << "Case #" << kase << ": " ;
      if (r < 0)
         cout << "IMPOSSIBLE" << endl ;
      else
         cout << r << endl ;
   }
}
