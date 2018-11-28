/*
By Tianyi Chen. All rights reserved.
Date: 2017-04-08
*/
#include<bits/stdc++.h>
using namespace std;
int64_t n,k,l,r;
map<int64_t,pair<int64_t,int64_t>>m;
void ins(int64_t v,int64_t d) {
 if(v)(v&1?m[v+1>>1].first:m[v+1>>1].second)+=d;
}
void gendata() {
 freopen("e:/gcj/cex.in","w",stdout);
 mt19937 mt;
 uniform_int_distribution<int64_t>gen(1,1e18);
 printf("%d\n",200);
 for(int i=0;i<200;++i) {
  int64_t n=gen(mt);
  cout<<n<<' '<<gen(mt)%n+1<<'\n';
 }
 exit(0);
}
int main() {
 int T;scanf("%d",&T);for(int _=1;_<=T;++_) {
  scanf("%lld%lld",&n,&k);
  m.clear();ins(n,1);
  for(;;) {
   auto P=--m.end();
   auto&p=P->second;
   if(p.second) {
    r=P->first;
    l=r-1;
    ins(l,p.second);ins(r,p.second);
    if((k-=p.second)<=0)break;
   }
   if(p.first) {
    ins(l=P->first-1,p.first);ins(r=P->first-1,p.first);
    if((k-=p.first)<=0)break;
   }
   m.erase(P);
  }
  printf("Case #%d: %lld %lld\n",_,r,l);
 }
}