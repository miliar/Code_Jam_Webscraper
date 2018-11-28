#include <bits/stdc++.h>
int n , k;
using namespace std;
#define pii pair <double,double>
#define ff first
#define ss second
#define PI acos(-1.0)
pii a[1005];
bool vis[1005][1005];
double dp[1005][1005];
bool cmp(pii a , pii b){
   if(a.ff == b.ff){
     return  a.ss > b.ss;
   }
   return a.ff < b.ff;
}


double call(int indx, int rem,double send){
     if(indx >= n){
        if(rem == 0) return 0;
        else return 1e-10;
     }
     double p1 = 0.0;
     double p2 = 0.0;
     if(vis[indx][rem] == 1){
         return dp[indx][rem];
     }
     if(rem > 0){
        p1 = PI*a[indx].ff*a[indx].ff - PI*send*send + 2*PI*a[indx].ff*a[indx].ss+call(indx+1,rem-1,a[indx].ff);
     }
     p2 = call(indx+1,rem,send);
     return dp[indx][rem]=  max(p1,p2);
}
int main()
{
     int test , cs  = 1;
     scanf("%d",&test);
     while(test--){
         memset(vis,0,sizeof vis);
         scanf("%d%d",&n,&k);
         for(int i = 0 ; i< n ; i++){
             scanf("%lf %lf",&a[i].ff ,&a[i].ss);
         }
         sort(a,a+n,cmp);
         // for(int i = 0 ; i< n ; i++){
         //     cout << a[i].ff << ' ' << a[i].ss << endl;
         // }
         double res = call(0, k,0);
         printf("Case #%d: %.9lf\n",cs++ , res);
     }
}
