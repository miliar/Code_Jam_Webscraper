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
#include <iomanip>


using namespace std;


int main(){
   int n_case;
   cin >> n_case;
   for( int loop = 0 ; loop < n_case ; loop++ ){
      int N, Q;
      cin >> N >> Q;
      int power[N];
      int speed[N];
      for( int i = 0 ; i < N; i++ ) cin >> power[i] >> speed[i];
      int dist[N][N];
      for( int i = 0 ; i < N; i++ ){
         for( int j = 0 ; j < N ; j++){
            cin >> dist[i][j];
         }
      }
      double ans[N+1];
      ans[0]=0;
      for( int i = 1 ; i <N+1; i++ ){
         ans[i] = DBL_MAX;
      }
      for( int i = 0 ; i < N; i++ ){
         double cur_time = ans[i];
      //   cout << ans[i] << endl;
         int d=0;
         for( int j = i+1 ; j < N ; j++ ){
            d+=dist[j-1][j];
            if( d > power[i] ) break;
            ans[j] = min(ans[j], cur_time + d*1.0/speed[i]);
         }
      }
      for(int i =0 ; i < Q; i++){
         int u,v;
         cin >> u >> v;
      }
      cout << "Case #" << loop+1 << ": ";
      cout << fixed << setprecision(10) <<ans[N-1]<< endl;
   }
   return 0;
}
