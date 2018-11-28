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
const int N=1e6+10;
const double pi=acos(-1);
double VV(double r,double h){
 return pi*r*r+2*pi*r*h;
}
double Ans[101];
struct{
 double dp[1001][1010];
 int n,maxr,k,ins_id,h[1001],r[1001];
 pair<int,int>hr[1001];
 double vb[1001],vm[1001];
 void read(){
  scanf("%d%d",&n,&k);
  for(int i=0;i<n;++i)scanf("%d%d",r+i,h+i);
 }
 void st(){
  for(int i=0;i<n;++i)hr[i]=make_pair(r[i],h[i]);
  sort(hr,hr+n,greater<pair<int,int>>());
  for(int i=0;i<n;++i)tie(r[i],h[i])=hr[i];
 }
 void solve(){
  st();
  vector<int>rs;
  for(int i=0;i<n;++i){
   vb[i]=pi*r[i]*r[i]+(vm[i]=2*pi*r[i]*h[i]);
   rs.push_back(r[i]);
  }


  sort(rs.begin(),rs.end());
  rs.erase(unique(rs.begin(),rs.end()),rs.end());
  for(int i=0;i<n;++i)r[i]=lower_bound(rs.begin(),rs.end(),r[i])-rs.begin();
  fill_n(*dp,1001*1010,-1);
  fill(dp[k],dp[k]+1010,0);
  for(int x=0;x<n;++x){
   for(int i=0;i<k;++i)for(int j=r[x];j<=1000;++j){
    dp[i][r[x]]=max(dp[i][r[x]],dp[i+1][j]+(i==k-1?vb:vm)[x]);
   }
  }
  Ans[ins_id]=*max_element(dp[0],dp[0]+1010);
 }
}sr[10];
int main(){
 scanf("%d",&T);solve(sr);
 for(int i=0;i<T;++i)printf("Case #%d: %.10lf\n",i+1,Ans[i]);
}