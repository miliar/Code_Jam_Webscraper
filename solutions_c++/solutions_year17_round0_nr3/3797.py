 /* Copyright VisualOn 2017. All Rights Reserved. */
 /* =====================================================================================
 *       Filename:  a.cpp
 *    Description:  
 *        Created:  04/08/17 14:58:02 CST
 *         Author:  Bo-Han Gary Wu (VisualOn), bhwu@visualon.com
 * ===================================================================================== */

#include <iostream>
#include <vector>
#include <string>

using namespace std;

uint64_t N;

int main(){
   cin >> N;
   for (uint64_t i=0; i<N; i++){
      uint64_t T, K;
      cin >> T >> K; 
      uint64_t v = 1, level = 1;
      for (int j=0; j<64; j++){
         if (v>K)
            break;
         level++;
         v *= 2;
      }
      v /= 2;
      uint64_t d = (T-v+1)/v;
      uint64_t r = (T-v+1)%v;

      cout << "Case #" << i+1 << ": ";
      if (v*2>T){
         cout << 0 << " " << 0 << endl;
      }else if (K>v+r-1){ //small
         if ( (d&1)==0 ) cout << (d-1)/2+1 << " " << (d-1)/2 <<endl;
         else cout << (d-1)/2 << " " << (d-1)/2 << endl;
      }else{ //large
         if ( ((d+1)&1)==0 ) cout << d/2+1 << " " << d/2 <<endl;
         else cout << d/2 << " " << d/2 << endl;
      }
   }
   return 0;
}
