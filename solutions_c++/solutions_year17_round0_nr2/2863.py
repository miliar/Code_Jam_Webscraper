#include <bits/stdc++.h>
using namespace std ;

bool isTidy(long n) {
  int r = n % 10 ;
  n /= 10 ;
  while(n != 0) {
    int l = n % 10 ;
    if(l > r)
      return false ;
    else {
      r = l ;
      n /= 10 ;
    }
  }
  return true ;
}

int main() {
  ifstream cin("p2_large.in") ;
  ofstream cout("p2.out") ;
  int t ;
  cin >> t ;
  for(int tc = 1 ; tc <= t ; tc ++) {
    long n ;
    cin >> n ;
    cout << "Case #" << tc << ": " ;
    if(isTidy(n))
      cout << n << "\n" ;
    else {
        int i = 1 ;
        while(! isTidy(n)) {
          long p = (long)pow(10 , i) ;
          n = ((n / p - 1) * p + (p - 1)) ;
          i ++ ;
        }
        cout << n << "\n" ;
    }
  }
  return 0 ;
}
