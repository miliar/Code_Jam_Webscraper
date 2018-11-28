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
      string cakes;
      uint64_t K;
      cin >> cakes >> K;
      uint64_t cnt = 0;
      for (int j=0; j<=cakes.size()-K; j++){
         if (cakes[j]=='-'){
            cnt++;      
            for (int k=j; k<j+K; k++)
               cakes[k] = (cakes[k]=='+') ? '-' : '+';
         }
      }
      cout << "Case #" << i+1 << ": ";
      bool pass = true;
      for (int j=cakes.size()-K+1; j<cakes.size(); j++){
         if (cakes[j]=='-'){
            cout << "IMPOSSIBLE" << endl;
            pass = false;
            break;
         }
      }
      if (pass)
         cout << cnt << endl;
   }
   return 0;
}
