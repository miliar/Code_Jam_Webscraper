#include <bits/stdc++.h>
using namespace std ;

int main() {
  ifstream cin("p21_large.in") ;
  ofstream cout("p21_large.out") ;
  int t ;
  cin >> t ;
  for(int tc = 1 ; tc <= t ; tc ++) {
    long d , n ;
    cin >> d >> n ;
    double max = 0.0 ;
    for(int i = 0 ; i < n ; i ++) {
      long k , s ;
      cin >> k >> s ;
      double time = (d - k) / (double) s ;
      if(max < time)
        max = time ;
    }
    double max_s = (double) d / max ;
    cout << "Case #" << tc << ": " << fixed << setprecision(6) << max_s << "\n" ;
  }
  return 0 ;
}