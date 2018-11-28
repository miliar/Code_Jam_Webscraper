#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std ;
typedef long long ll ;
int main() {
   long long T, N, K ;
   cin >> T ;
   for (int kase=1; kase<=T; kase++) {
      cin >> N >> K ;
      map<ll,ll> gapcounts ;
      gapcounts[N] = 1 ;
      ll lft=0, rght=0 ;
      while (K > 0) {
         auto it = gapcounts.rbegin() ;
         ll size = it->first ;
         rght = size / 2 ;
         lft = (size - 1) / 2 ;
         K -= it->second ;
         gapcounts[lft] += it->second ;
         gapcounts[rght] += it->second ;
         gapcounts.erase(size) ;
      }
      cout << "Case #" << kase << ": " << rght << " " << lft << endl ;
   }
}
