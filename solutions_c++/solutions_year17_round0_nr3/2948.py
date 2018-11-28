#include <bits/stdc++.h>
using namespace std ;

int main() {
  ifstream cin("p3_large.in") ;
  ofstream cout("p31.out") ;
  int t ;
  cin >> t ;
  for(int tc = 1 ; tc <= t ; tc ++) {
    long n , k ;
    cin >> n >> k ;
    cout << "Case #" << tc << ": " ;
    if(n == k)
      cout << "0 0\n" ;
    else {
      long n1 = n ;
      for(long i = k ; i > 0 ; i /= 2) {
        long m1 ;
        if((i != 1 && i % 2 != 0) || (n1 % 2 != 0)) {
          if(i == 1) {
            cout << (n1 - 1) / 2 << " " << (n1 - 1) / 2 << "\n" ;
          } else {
            m1 = (n1 - 1) / 2 ;
            n1 = m1 ;
          }
        } else {
          if(i == 1) {
            m1 = n1 / 2 ;
            cout << max((m1 - 1) , (n1 - m1)) << " " << min((m1 - 1) , (n1 - m1)) << "\n" ;
          } else {
            m1 = n1 / 2 ;
            n1 = max((m1 - 1) , (n1 - m1)) ;
          }
        }
      }
    }
  }
  return 0 ;
}
