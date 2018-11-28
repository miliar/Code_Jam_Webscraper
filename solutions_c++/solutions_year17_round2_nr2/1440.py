/*
By Tianyi Chen. All rights reserved.
Date: 2017-04-22
*/
#include<bits/stdc++.h>
using namespace std;
int n,R,O,Y,G,B,V;
char buf[1111],vis[666][666][666];
bool check(){
 if(*buf==buf[n-1])return 0;
 for(int i=1;i<n;++i)if(buf[i]==buf[i-1])return 0;
 return 1;
}
bool put(int i,int r,int y,int b){
 if(i==n)return *buf!=buf[n-1];
 auto&rt=vis[r][y][b];
 if(~rt)return rt;
 switch(buf[i-1]){
 case 'R':
  if(y&&(buf[i]='Y')&&put(i+1,r,y-1,b))return rt=1;
  if(b&&(buf[i]='B')&&put(i+1,r,y,b-1))return rt=1;
  return rt=0;
 case'Y':
  if(r&&(buf[i]='R')&&put(i+1,r-1,y,b))return rt=1;
  if(b&&(buf[i]='B')&&put(i+1,r,y,b-1))return rt=1;
  return rt=0;
 case'B':
  if(r&&(buf[i]='R')&&put(i+1,r-1,y,b))return rt=1;
  if(y&&(buf[i]='Y')&&put(i+1,r,y-1,b))return rt=1;
 }
 return rt=0;
}
int main(){
 int T;scanf("%d",&T);for(int _=1;_<=T;++_){
  printf("Case #%d: ",_);
  scanf("%d",&n);scanf("%d%d%d",&R,&O,&Y);scanf("%d%d%d",&G,&B,&V);
  buf[n]=0;
  if(max({R,Y,B})*2>n){
   puts("IMPOSSIBLE");continue;
  }
  if(R){
   *buf='R';memset(vis,-1,sizeof vis);
   if(put(1,R-1,Y,B)){
    puts(buf);goto nx;
   }
  }
  if(Y){
   *buf='Y';memset(vis,-1,sizeof vis);
   if(put(1,R,Y-1,B)){
    puts(buf);goto nx;
   }
  }
  if(B){
   *buf='B';memset(vis,-1,sizeof vis);
   if(put(1,R,Y,B-1)){
    puts(buf);goto nx;
   }
  }
  puts("IMPOSSIBLE");
  nx:;
 }
}