#include<bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0;i<n;i++)
int S[1002];
int main(){
  int t;
  cin>>t;
  rep(cs,t){
    string s;
    int k;
    rep(i,1002)S[i]=0;
    cin>>s>>k;
    int len=s.size();
    int state=1;
    int res=0;
    rep(i,len-k+1){
      state^=S[i]&1;
      if(state==(s[i]=='-')){
        S[i]++;S[i+k]--;
        res++;
        state^=1;
      }
    }
    bool yes=true;
    rep(i,k-1){
      state^=S[len-k+1+i]&1;
      if(state==(s[len-k+1+i]=='-')){
        yes=false;
        break;
      }
    }
    cout<<"Case #"<<(cs+1)<<": ";
    yes?(cout<<res):(cout<<"IMPOSSIBLE");
    cout<<"\n";
  }
  return 0;
}
