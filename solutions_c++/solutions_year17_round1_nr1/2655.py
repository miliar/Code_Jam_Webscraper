/*
By Tianyi Chen. All rights reserved.
Date: 2017-04-15
*/
#include<bits/stdc++.h>
using namespace std;
char g[33][33],og[33][33];
int n,m;
int main(){
 int T;scanf("%d",&T);for(int _=1;_<=T;++_){
  scanf("%d%d",&n,&m);
  for(int i=0;i<n;++i)scanf("%s",g[i]);memcpy(og,g,sizeof g);
  for(int i=0;i<n;++i)for(int j=0;j<m;++j)if(g[i][j]!='?'){
   int jj=j;
   while(--jj>=0&&g[i][jj]=='?')g[i][jj]=g[i][j];
  }
  for(int i=0;i<n;++i)for(int j=0;j<m;++j)if(g[i][j]!='?'){
   int jj=j;
   while(++jj<m&&g[i][jj]=='?')g[i][jj]=g[i][j];
  }
  for(int i=0;i<n;++i)for(int j=0;j<m;++j)if(g[i][j]!='?'){
   int ii=i,jj=j;
   while(jj<m&&g[i][jj]==g[i][j])++jj;
   while(--ii>=0&&all_of(og[ii]+j,og[ii]+jj,[&](char c){return c=='?';})){
    fill(g[ii]+j,g[ii]+jj,g[i][j]);
   }
   j=jj-1;
  }
  for(int i=0;i<n;++i)for(int j=0;j<m;++j)if(g[i][j]!='?'){
   int ii=i,jj=j;
   while(jj<m&&g[i][jj]==g[i][j])++jj;
   while(++ii<n&&all_of(og[ii]+j,og[ii]+jj,[&](char c){return c=='?';})){
    fill(g[ii]+j,g[ii]+jj,g[i][j]);
   }
   j=jj-1;
  }
  printf("Case #%d:\n",_);
  for(int i=0;i<n;++i)puts(g[i]);
 }
}