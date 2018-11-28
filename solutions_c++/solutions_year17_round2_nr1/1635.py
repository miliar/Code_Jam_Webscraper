/*
By Tianyi Chen. All rights reserved.
Date: 2017-04-22
*/
#include<bits/stdc++.h>
using namespace std;
int T,n,D;double k[1001],s[1001],h,l,mid,rec;
int main(){
 scanf("%d",&T);for(int _=1;_<=T;++_){
  h=1e100;l=0;
  scanf("%d%d",&D,&n);
  for(int i=0;i<n;++i)scanf("%lf%lf",k+i,s+i);
  for(int _=0;_<500;++_){
   rec=1e100;
   mid=(h+l)/2;
   for(int i=0;i<n;++i)rec=min(rec,k[i]+s[i]*mid);
   (rec>D?h:l)=mid;
  }
  printf("Case #%d: %.10lf\n",_,D/mid);
 }
}