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
      int N, R, O, Y, G, B, V;
      cin >> N >> R >> O >> Y >> G >> B >> V;
      if( R == G && B == 0 && O == 0 && Y == 0 && V == 0 ){
         string ans = "";
         for( int i = 0 ; i < R; i++ ) ans += "RG";
         cout << "Case #" << loop+1 << ": " << ans << endl ;
         continue;
      }
      if( B == O && R == 0 && G == 0 && Y == 0 && V == 0 ){
         string ans = "";
         for( int i = 0 ; i < B; i++ ) ans += "BO";
         cout << "Case #" << loop+1 << ": " << ans << endl ;
         continue;
      }
      if( Y == V && R == 0 && G == 0 && B == 0 && O == 0 ){
         string ans = "";
         for( int i = 0 ; i < Y; i++ ) ans += "YV";
         cout << "Case #" << loop+1 << ": " << ans << endl ;
         continue;
      }
      if( (R!= 0 && R <= G) || (B!=0 && B <= O) || (Y!=0 && Y <= V) ){
         cout << "Case #" << loop+1 << ": IMPOSSIBLE" << endl ;
         continue;
      }
      string str2[3] = {"", "", ""};
      for( int i = 0 ; i < G; i++ ) str2[0] += "RG";
      str2[0] += "R";
      for( int i=0; i < O; i++ ) str2[1] += "BO";
      str2[1] += "B";
      for( int i=0; i<V; i++ ) str2[2] +="YV";
      str2[2] += "Y";
      R-=(G); G=0;
      B-=(O); O=0;
      Y-=(V); V=0;
      if( R > B+Y ||  Y > R+B || B > R+Y ){
         cout << "Case #" << loop+1 << ": IMPOSSIBLE" << endl ;
         continue;
      }
      int cnt[3] = {R,B,Y};
      bool used[3];
      used[0]=used[1]=used[2]=false;
      string str1[3] = {"R", "B", "Y"};
      int ind = 0;
      for( int i = 0 ; i < 3; i++ ){
         if(cnt[i] > cnt[ind] ) ind = i;
      }
      int start_ind = ind;
      string ans ="";
      bool ok = true;
      while( cnt[0] != 0 || cnt[1] != 0 || cnt[2] != 0 ){
         if( cnt[ind] <= 0 ){
            ok = false;
            break;
         }
         if( used[ind] == true ){
            ans += str1[ind];
         }
         else{
            ans += str2[ind];
            used[ind]=true;
         }
         cnt[ind]--;
         int next_ind = -1;
         for( int i = 0 ; i < 3; i++ ){
            if( i!=ind && (next_ind==-1 || cnt[next_ind] < cnt[i] || (cnt[next_ind] == cnt[i] && i== start_ind))){
               next_ind = i;
            }
         }
         ind = next_ind;
      }
      if( ok ){
         cout << "Case #" << loop+1 << ": "<<ans <<endl;
      }else{
         cout << "Case #" << loop+1 << ": IMPOSSIBLE"<<endl;
      }
   }
      
   return 0;
}
