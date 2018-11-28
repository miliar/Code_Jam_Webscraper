/*
By Tianyi Chen. All rights reserved.
Date: 2017-04-30
*/
#include<bits/stdc++.h>
using namespace std;
int T,S,E,ac,aj,dp[2][1500],ndp[2][1500],occ[1500];
int main(){
 scanf("%d",&T);for(int _=1;_<=T;++_){
  memset(dp,0x33,sizeof dp);dp[0][0]=dp[1][0]=1;
  scanf("%d%d",&ac,&aj);
  memset(occ,-1,sizeof occ);
  for(int _=0;_<ac;++_){
   scanf("%d%d",&S,&E);fill(occ+S,occ+E,0);
  }
  for(int _=0;_<aj;++_){
   scanf("%d%d",&S,&E);fill(occ+S,occ+E,1);
  }


  for(int i=1;i<=1440;++i){
   memset(ndp,0x33,sizeof ndp);
   int k;

   switch(occ[i]){
   case -1:for(int k=0;k<2;++k)for(int j=0;j<i;++j)ndp[k][j+1]=min(ndp[k][j+1],dp[k][j]);
    if(i<5)for(int k=0;k<2;++k)for(int j=0;j<i;++j){
    }
    for(int k=0;k<2;++k)for(int j=0;j<i;++j)ndp[k][j+1]=min(ndp[k][j+1],dp[!k][i-j-1]+1);
    break;
   case 0:k=0;
    for(int j=0;j<i;++j)ndp[k][j+1]=min(ndp[k][j+1],dp[k][j]);
    for(int j=0;j<i;++j)ndp[k][j+1]=min(ndp[k][j+1],dp[!k][i-j-1]+1);
    break;
   case 1:k=1;
    for(int j=0;j<i;++j)ndp[k][j+1]=min(ndp[k][j+1],dp[k][j]);
    for(int j=0;j<i;++j)ndp[k][j+1]=min(ndp[k][j+1],dp[!k][i-j-1]+1);
   }
   memcpy(dp,ndp,sizeof dp);
  }
  printf("Case #%d: %d\n",_,0xfffe&min(dp[0][720],dp[1][720]));
 }
}