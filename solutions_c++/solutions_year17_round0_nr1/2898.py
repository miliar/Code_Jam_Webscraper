#include <bits/stdc++.h>
using namespace std ;

int main() {
  ifstream cin("p1_large.in") ;
  ofstream cout("p1.out") ;
  int t ;
  cin >> t ;
  for(int tc = 1 ; tc <= t ; tc ++) {
    string str ;
    int k ;
    cin >> str >> k ;
    cout << "Case #" << tc << ": " ;
    if(str . find("-") == string::npos)
      cout << "0\n" ;
    else {
      int i = str . find_first_of("-") ;
      int j = str . find_last_of("-") ;
      int count = 0 ;
      while(i < j) {
        if(i + k > str . length()) {
          cout << "IMPOSSIBLE\n" ;
          break ;
        }
        for(int z = 0 ; z < k ; z ++) {
          if(str[i + z] == '-')
            str[i + z] = '+' ;
          else
            str[i + z] = '-' ;
        }
        count ++ ;
        if(str . find("-") == string::npos) {
            cout << count << "\n" ;
            break ;
        } else {
          i = str . find_first_of("-") ; // Can be optimized
          j = str . find_last_of("-") ; // Can be optimized
          if(i >= j) {
            break ;
          }
        }
        if(j - k < -1) {
          cout << "IMPOSSIBLE\n" ;
          break ;
        }
        for(int z = 0 ; z < k ; z ++) {
          if(str[j - z] == '-')
            str[j - z] = '+' ;
          else
            str[j - z] = '-' ;
        }
        count ++ ;
        if(str . find("-") == string::npos) {
            cout << count << "\n" ;
            break ;
        } else {
          i = str . find_first_of("-") ; // Can be optimized
          j = str . find_last_of("-") ; // Can be optimized
          if(i >= j) {
            break ;
          }
        }
        if((j - i) < (k - 1)) {
          cout << "IMPOSSIBLE\n" ;
          break ;
        }
      }
      if(i >= j)
        cout << "IMPOSSIBLE\n" ;
    }
  }
  return 0 ;
}
