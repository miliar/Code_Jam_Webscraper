/*
By Tianyi Chen. All rights reserved.
Date: 2017-04-15
*/
#include<bits/stdc++.h>
using namespace std;
int n,p,r[60],q[60][60],ans;
int mmix(pair<int,int>i,pair<int,int>j){
 if(i>j)swap(i,j);
 if(i.second<j.first)return 0;
 return i.second;
}
pair<int,int>dv(int64_t i,int64_t j){
 static map<pair<int,int>,pair<int,int>>md;
 if(md.count({i,j}))return md[{i,j}];
 int a,b=0;
 int rof=(i+i/10)/j;
 for(int x=12000000;x>=0;--x)
  if(i<=j/10*x*11&&j/10*x*9<=i){
   b=x;break;
  }
 if(!b)return md[{i,j}]={0,0};
 rof=(i-i/10)/j;
 for(int x=0;x<=12000000;++x)
  if(i<=j/10*x*11&&j/10*x*9<=i){
   a=x;break;
 }
 return md[{i,j}]={a,b};
}
int main(){
 int T;scanf("%d",&T);for(int _=1;_<=T;++_){
  scanf("%d%d",&n,&p);ans=0;
  for(int i=0;i<n;++i)scanf("%d",r+i),r[i]*=10;
  for(int i=0;i<n;++i)for(int j=0;j<p;++j)scanf("%d",q[i]+j),q[i][j]*=10;
  if(n==1){
   for(int i=0;i<p;++i)ans+=!!dv(q[0][i],r[0]).second;
  } else if(n==2){
   sort(q[1],q[1]+p);
   int tans;
   do{
    tans=0;
    for(int i=0;i<p;++i)tans+=!!mmix(dv(q[0][i],r[0]),dv(q[1][i],r[1]));
    ans=max(ans,tans);
   } while(next_permutation(q[1],q[1]+p));
  } else{
  }
  printf("Case #%d: %d\n",_,ans);
 }
}