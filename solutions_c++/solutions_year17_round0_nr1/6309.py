#include <string>
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int T, K;
#define MAXN 1005
char S[MAXN];

int calculate(){
   int i = 0;
   int len = strlen(S);
   int res = 0;
   for(int i=0; i<=len-K; ++i) {
      if( S[i] == '-') {
          res++;
          for(int j=i; j<i+K; ++j)
            S[j] = (S[j]=='+')?'-':'+';
      } 
   }
   for(int i=0; i<len; ++i) if(S[i] == '-') return -1;
   return res;
}

int main(){
   cin >> T;
   for(int tcase=1; tcase<=T; ++tcase){
       cin >> S >> K;
       int res = calculate();
       if( res == -1) 
        cout << "Case #" << tcase << ": " <<  "IMPOSSIBLE" << endl;
       else 
        cout << "Case #" << tcase << ": " << res << endl;
   }
   return 0;
}
