#include<iostream>
#include<vector>
#include<map>


using namespace std;

typedef long long ll;


struct st{
  ll l, r;
};


bool operator<(const st &a, const st &b){
  if (a.l<b.l)
    return 0;
  if (a.l>b.l)
    return 1;
  if (a.r<b.r)
    return 0;
  if (a.r>b.r)
    return 1;
  return 0;
}



int main(){
  int T; cin>>T;
  for (int tc=1; tc<=T; ++tc){
    
    map<st,ll> ma=map<st,ll>();
    ll N, K; cin>>N>>K;
    st s, s2;
    s.l=(N+1)/2;
    s.r=(N+2)/2;
    ma[s]=1;
    while(1){
      s=ma.begin()->first;
      N=ma.begin()->second;
      K-=N;
      //cout<<N<<" "<<s.l<<" "<<s.r<<endl;
      if (K<=0)
	break;
      ma.erase(s);
      s2.l=s.l/2;
      s2.r=(s.l+1)/2;
      ma[s2]+=N;
      s2.l=s.r/2;
      s2.r=(s.r+1)/2;
      ma[s2]+=N;
    }
    cout<<"Case #"<<tc<<": "<<s.r-1<<" "<<s.l-1<<endl;


  }
  return 0;
}
