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
      string num; 
      cin >> num; 
      int len = (int)num.size();
      bool large = false, small = false;
      int ith = 0;
      for (int j=0; j<len-1; j++){
         if (!small && num[j+1]>num[j]){
            large = true;
         }else if (num[j+1]<num[j]){
            small = true;
            ith = j; 
            break;
         }
      }
      cout << "Case #" << i+1 << ": ";
      if (large && small){
         string rst = num.substr(0,ith);
         rst.push_back(char(num[ith]-1));
         for (int j=ith+1; j<len; j++)
            rst += "9";
         cout << rst << endl;
      }else if (!small){
         cout << num << endl;
      }else{
         string rst = "";
         if (num[0]=='1'){
            for (int j=0; j<len-1; j++)
               rst += "9";
         }else{
            rst.push_back(char(num[0]-1));
            for (int j=0; j<len-1; j++)
               rst += "9";
         }
         cout << rst << endl;
      }
   }
   return 0;
}
