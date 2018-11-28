/*
By Tianyi Chen. All rights reserved.
Date: 2017-04-30
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
double Ans[101];
const double eps=1e-8;
struct {
 double p[55],t;int n,k,tint,pi[55],ins_id;
 void read(){
  scanf("%d%d",&n,&k);scanf("%lf",&t);tint=(t+eps)*10000;
  for(int i=0;i<n;++i)scanf("%lf",p+i),pi[i]=(p[i]+eps)*10000;
 }
 void solve(){
  sort(pi,pi+n);
  if(n==1){
   pi[0]+=tint;
  }else while(tint){
   while(pi[0]<=pi[1]&&tint)--tint,++pi[0];
   sort(pi,pi+n);
  }
  if(pi[0]>=10000){
   Ans[ins_id]=1;return;
  }
  for(int i=0;i<n;++i)p[i]=pi[i]/10000.;
  double ans=1;
  for(int i=0;i<n;++i)ans*=p[i];
  Ans[ins_id]=ans;
 }
}sr[10];
int main(){
 scanf("%d",&T);solve(sr);
 for(int i=0;i<T;++i)printf("Case #%d: %.8lf\n",i+1,Ans[i]);
}