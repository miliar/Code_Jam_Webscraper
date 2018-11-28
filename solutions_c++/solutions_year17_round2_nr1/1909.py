#include<bits/stdc++.h>
using namespace std;
int main(){
               cin.sync_with_stdio(false);
               freopen("a.txt","r",stdin);
               freopen("b.txt","w",stdout);
               int T , tt = 1;
               cin >> T;
               while(T--){
                 double mx = 0.0;
                 int d , n;
                 cin >> d >> n;
                 for(int i = 1 ; i <= n ; ++i ){
                  int pos , sp;
                  cin >> pos >> sp;
                  double ti = ((d - pos) * 1.0)/sp;
                  mx = max(mx , ti);
                 }
                 double ans = d/mx;
                 printf("Case #%d: %.6lf\n",tt, ans);
                 ++tt;
               }
}
