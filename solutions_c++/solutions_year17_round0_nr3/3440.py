#include<bits/stdc++.h>
using namespace std;
#define int long long
#define rep(i,n) for(int i=0;i<n;i++)
typedef pair<int,int> P;
int log2(int n){
  int res=0;
  while(n>>=1)res++;
  return res;
}
P solve(int n,int k){
  n-=k;
  int l=log2(k)+1;
  int n1,n2;
  rep(i,l){
    n2=n>>1;
    n1=n-n2;
    n=n2;
  }
  return P(n1,n2);
}
signed main(){
  int t;
  cin>>t;
  rep(cs,t){
    int n,k;
    cin>>n>>k;
    P p=solve(n,k);
    cout<<"Case #"<<(cs+1)<<": "<<p.first<<" "<<p.second<<"\n";
  }
  return 0;
}
