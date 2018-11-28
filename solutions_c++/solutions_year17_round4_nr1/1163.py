#include <iostream>
#include <vector>
#include <string>
using namespace std ;
int main() {
   int T ;
   string s ;
   cin >> T ;
   for (int kase=1; kase<=T; kase++) {
      int N, P ;
      cin >> N >> P ;
      vector<int> cnts(P) ;
      for (int i=0; i<N; i++) {
         int v ;
         cin >> v ;
         cnts[v % P]++ ;
      }
      int r = cnts[0] ;
      cnts[0] = 0 ;
      for (int i=1; i+i<P; i++) {
         int t = min(cnts[i], cnts[P-i]) ;
         r += t ;
         cnts[i] -= t ;
         cnts[P-i] -= t ;
      }
      if (P % 2 == 0) {
         int t = cnts[P/2] / 2 ;
         r += t ;
         cnts[P/2] -= 2*t ;
      }
      if (P == 2) {
         if (cnts[1])
            r++ ;
      } else if (P == 3) {
         int t = cnts[1] / 3 + cnts[2] / 3 ;
         if (cnts[1])
            cnts[1] -= 3 * t ;
         if (cnts[2])
            cnts[2] -= 3 * t ;
         r += t ;
         if (cnts[1] || cnts[2])
            r++ ;
      } else if (P == 4) {
         int odds = cnts[1] + cnts[3] ;
         if (cnts[2] && odds >= 2) {
            r++ ;
            cnts[2]-- ;
            odds -= 2;
         }
         int t = odds / 4 ;
         r += t ;
         odds -= 4 * t ;
         if (odds || cnts[2])
            r++ ;
      }
      cout << "Case #" << kase << ": " << r << endl ;
   }
}
