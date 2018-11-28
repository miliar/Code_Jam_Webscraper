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
      string S;
      int K;
      cin >> S >> K;
      int size = S.size();
      int ans = 0;
      string all_happy(size, '+');
      for( int i = 0 ; i+K-1 < size; i++ ){
         if(S[i] == '-'){
            ans++;
            for( int j = 0 ; j <K; j++){
               if( S[i+j] == '-' ){ S[i+j] = '+';}
               else{ S[i+j] = '-';}
            }
            //cout << "flipped at "<< i << ": "<< S<<endl;
         }
      }
      if( S == all_happy ) cout << "Case #" << loop+1 << ": " <<ans<< endl;
      else cout << "Case #" << loop+1 << ": " <<"IMPOSSIBLE"<< endl;
   }
   return 0;
}
