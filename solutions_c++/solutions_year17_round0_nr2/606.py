#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <cstring>


using namespace std;


int main(){
   int n_case;
   cin >> n_case;
   for( int loop = 0 ; loop < n_case ; loop++ ){
      long long N;
      cin >> N;
      long long bit = 1;
      while( (N/bit) >= 10 ) bit*=10;
      long long maskbit = bit;
      while( bit >= 10 ){
         int d1 = (N/bit)%10;
         int d2 = (N/(bit/10))%10;
         if( d1 > d2 ){
            N=(N/maskbit)*maskbit;
            N=N-1;
            break;
         }
         if( d1 != d2 ){
            maskbit = bit/10;
         }
         bit/=10;
      }
      cout << "Case #" << loop+1 << ": " <<N<< endl;
   }
   return 0;
}
