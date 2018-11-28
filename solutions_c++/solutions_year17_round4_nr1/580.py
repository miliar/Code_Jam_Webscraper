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
      int N,P;
      cin >> N >> P;
      int G[N];
      for(int i=0; i<N; i++ ) cin >> G[i];
      for(int i=0; i<N; i++ ) G[i] %= P;
      int cnt[4];
      memset(cnt,0,sizeof(cnt));
      for(int i=0; i<N; i++ ) cnt[G[i]]++;
      int ans = cnt[0];
      if( P == 2 ){
         ans += (cnt[1]+1)/2;     
      }
      else if( P ==3 ){
         int offset = min(cnt[1],cnt[2]);
         //cout << ans << "+=" << offset << endl;
         ans+=offset;
         cnt[1]-=offset;
         cnt[2]-=offset;
         ans += (cnt[1]+2)/3;
         ans += (cnt[2]+2)/3;
      }
      else if( P == 4 ){
         int onethree = min(cnt[1],cnt[3]);
         ans += onethree;
         cnt[1]-=onethree;
         cnt[3]-=onethree;
         int two = cnt[2]/2;
         ans += two;
         cnt[2]-=two*2;
         cnt[1]=max(cnt[1],cnt[3]);
         cnt[3]=0;
         if( cnt[2] > 0){
            cnt[2]=0;
            cnt[1]-=2;
            ans++;
         }
         //cout << cnt[1] << ", "<< cnt[2] << ", "<< cnt[3]<<endl;
         if( cnt[1] > 0 ){
            ans += (cnt[1]+3)/4;
         }
         
      }
      cout << "Case #" << loop+1 << ": " <<ans<< endl;
   }
   return 0;
}
