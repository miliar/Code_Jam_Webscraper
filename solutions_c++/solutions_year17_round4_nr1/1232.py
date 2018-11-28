/*
By Tianyi Chen. All rights reserved.
Date: 2017-05-13
*/
#include<bits/stdc++.h>


//mt_solve begin
#include<memory>
#include<thread>
using namespace std;
int T;
template<class C>
void _solve(C*s) {
	s->solve();
	s->~C();
}
template<class C>
void solve(C*__S) {
	C*S=new C[T];
	for(int i=0;i<T;++i)S[i].ins_id=i,S[i].read();
	thread*t=new thread[T];
	for(int i=0;i<T;++i)t[i]=thread(_solve<C>,S+i);
	for(int i=0;i<T;++i)t[i].join();
}
//mt_solve end
using namespace std;
int Ans[100];
struct{
 int n,p,g[111],t,ans,ins_id,rem[4],mem[100][100][100];
 int dp(int i,int j,int k,int r){
  if(!i&&!j&&!k)return 0;
  int&rt=mem[i][j][k];
  if(~rt)return rt;
  rt=0;
  if(i){
   if(!r)rt=max(rt,1+dp(i-1,j,k,3));
   else rt=max(rt,dp(i-1,j,k,(r+4-1)%4));
  }
  if(j){
   if(!r)rt=max(rt,1+dp(i,j-1,k,2));
   else rt=max(rt,dp(i,j-1,k,(r+4-2)%4));
  }
  if(k){
   if(!r)rt=max(rt,1+dp(i,j,k-1,1));
   else rt=max(rt,dp(i,j,k-1,(r+4-3)%4));
  }
  return rt;
 }
 void read(){
  scanf("%d%d",&n,&p);
  for(int i=0;i<n;++i)scanf("%d",g+i);
 }
 void solve(){
  memset(rem,0,sizeof rem);
  for(int i=0;i<n;++i)++rem[g[i]%p];
  ans=rem[0];
  switch(p){
  case 2:ans+=rem[1]/2+rem[1]%2;
   break;
  case 3:ans+=t=min(rem[1],rem[2]);
   rem[1]-=t;rem[2]-=t;
   ans+=(rem[1]+rem[2])/3+!!((rem[1]+rem[2])%3);
   break;
  case 4:memset(mem,-1,sizeof mem);
   ans+=dp(rem[1],rem[2],rem[3],0);
  }
  Ans[ins_id]=ans;
 }
}sr[33];
int main(){
 scanf("%d",&T);solve(sr);
 for(int i=0;i<T;++i)printf("Case #%d: %d\n",i+1,Ans[i]);
}