/*
By Tianyi Chen. All rights reserved.
Date: 2017-04-08
*/
#include<bits/stdc++.h>
using namespace std;
char ans[22],in[22];
int n;
bool place(int i,char pre,char ls=0) {
 if(i==n)return 1;
 if(ls) {
  return place(i+1,ans[i]='9',1);
 }
 if(in[i]>=pre) {
  if(place(i+1,ans[i]=in[i],0))return 1;
 }
 for(int c=in[i]-1;c>=pre;--c) {
  return place(i+1,ans[i]=c,1);
 }
 return 0;
}
int main() {
 int T;scanf("%d",&T);for(int _=1;_<=T;++_) {
  scanf("%s",in);ans[n=strlen(in)]=0;
  place(0,'0');
  printf("Case #%d: %s\n",_,find_if(ans,ans+n,[](char c) {return c-'0';}));
 }
}