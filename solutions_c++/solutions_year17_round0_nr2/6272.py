#include <cstring>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long int64;

int T;
int64 n;

int64 solve(int64 n){
   vector <int> digits;
   int64 on = n;
   if( n < 10 ) return n;
   digits.clear();
   while(n) {
      digits.push_back(n%10);
      n /= 10;
   }
   reverse(digits.begin(), digits.end());
   int sz = digits.size();
   int bk = 0;
   for( ; bk < sz -1 ; ++bk )
      if( digits[bk] > digits[bk+1] ) break; 

   if( bk == sz - 1) return on;
   int64 temp_n  = 0; 
   digits[bk] -= 1;
   for(int i=0; i<=bk; ++i) temp_n = temp_n * 10 + digits[i];
   int64 temp_res = solve(temp_n);
   int64 res = temp_res;
   for(int i=bk+1; i<sz; ++i) res = res * 10 + 9;
   return res;
}

int main(){
  cin >> T;
  for(int tcase = 1; tcase <= T; ++tcase) {
     cin >> n;
     cout << "Case #" << tcase << ": " << solve(n) << endl; 
  }
  return 0;
}
