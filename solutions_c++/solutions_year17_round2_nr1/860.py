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
      int D,N;
      cin >> D >> N;
      double max_time = 0;
      for( int i = 0 ; i < N; i++ ){
         int d, s;
         cin >> d >> s;
         double rest_dist = D-d;
         double cur_time = rest_dist/s;
         max_time = max(max_time, cur_time);
      }
      double speed = D/max_time;
      cout << "Case #" << loop+1 << ": " ;
      cout << fixed << setprecision(10) <<speed<< endl;
   }
   return 0;
}
