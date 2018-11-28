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
      int N,C,M;
      cin >> N >> C >> M;
      int cnt[C][N];
      memset(cnt,0,sizeof(cnt));
      for( int i = 0 ; i < M; i++ ){
         int p,b;
         cin >> p >> b;
         p--;b--;
         cnt[b][p]++;
      }
      int sumc[C];
      int sumn[N];
      int max_buy=0;
      memset(sumc,0, sizeof(sumc));
      memset(sumn,0, sizeof(sumn));
      for( int i = 0 ; i < C; i++ ){
         for( int j = 0 ; j < N; j++ ){
            sumc[i] += cnt[i][j];
            sumn[j] += cnt[i][j];
         }
         max_buy =max(max_buy, sumc[i]);
      }
      for( int ans = max_buy; ans <= M; ans++ ){
         int margin = 0;
         int move = 0;
         bool ok = true;
         for( int j = 0 ; j < N; j++ ){
            if( sumn[j] > ans ){
               int diff = sumn[j]-ans;
               if( diff > margin ){
                  ok=false;
                  break;
               }
               else{
                  move += diff;
                  margin -=diff;
               }
            }else{
               margin += ans-sumn[j];
            }
         }
         if( ok ){
            cout << "Case #" << loop+1 << ": " <<ans <<" "  << move << endl;
            break;
         }
      }
   }
   return 0;
}
