#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

pair<long long,long long> solve(long long n,long long k);
int maximal=0;

int main(){
  int t;
  cin>>t;
  for(int i=0;i<t;i++){
    long long n,k;
    cin>>n>>k;
    pair<long long,long long> ret=solve(n,k);
    cout<<"Case #"<<i+1<<": "<<ret.first<<' '<<ret.second<<'\n';
  }
}

void push(vector<pair<long long,long long> >& q,pair<long long,long long> p){
  for(int i=0;i<q.size();i++)
    if(q[i].first==p.first){
      q[i].second+=p.second;
      return;
    }
  q.push_back(p);
  sort(q.begin(),q.end(),greater<pair<long long,long long> >());
}

pair<long long,long long> pop(vector<pair<long long,long long> >& q){
  pair<long long,long long> ret=q[0];
  q.erase(q.begin());
  return ret;
}

pair<long long,long long> solve(long long n,long long k){
  vector<pair<long long,long long> > q;
  push(q,make_pair(n,1LL));

  long long served=0;
  while(true){
    maximal=max(maximal,static_cast<int>(q.size()));
    pair<long long,long long> p=pop(q);
    pair<long long,long long> next=make_pair(p.first/2,(p.first-1)/2);
    if(k<=p.second)
      return next;
    k-=p.second;
    served+=p.second;
    push(q,make_pair(next.first,p.second));
    push(q,make_pair(next.second,p.second));
  }
}
