#include <bits/stdc++.h>
using namespace std;
#define ull unsigned long long
int sz ;
string s;
ull dp[20][10][3];
ull p[20];
void power(){
   p[0] = 1;
   for(int i = 1 ; i<= 18 ; i++)
      p[i] = p[i-1]*10;;

}
ull call(int indx , int prev,bool ishigh, ull send){
     if(indx >= sz){
        return send;
     }
     ull ret;
     ull mmax = 0;
     if(dp[indx][prev][ishigh] != -1){
          int temp = sz-indx;
          ull right = dp[indx][prev][ishigh]%p[temp];
          return max(dp[indx][prev][ishigh],send*p[temp]+right);
     }
     for(int i = 0 ; i< 10 ; i++){
         if(ishigh && (i>s[indx]-48)) break;
         if(i >= prev){
            ret = call(indx+1 , i ,(ishigh && (i==s[indx]-48)) , send*10+i);
            mmax = max(ret, mmax);
         }
     }
     return dp[indx][prev][ishigh] = mmax;
}
int main()
{
  int test , cs =  1 ;
  power();
  scanf("%d",&test);
  while(test--){
       cin >> s;
       sz = s.size();
       memset(dp,-1,sizeof dp);
       ull res = call(0,0,1,0);
       printf("Case #%d: %llu\n",cs++ , res);
  }
}
