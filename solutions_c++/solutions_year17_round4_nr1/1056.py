#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
int t;
vector<ll> V;
int main(){
  ios::sync_with_stdio(false);
  cin>>t;
  for(int sada=1;sada<=t;sada++){
    ll n,p,vsledok=0;
    cin>>n>>p;
    V.resize(n);
    vector<ll> zvysky(p,0);
    for(int i=0;i<n;i++){
        cin>>V[i];
        zvysky[V[i]%p]++;
    }
    cout <<"Case #"<<sada<<": ";
    vsledok=zvysky[0];
    if(p==2){
      vsledok+=zvysky[1]/2;
      if(zvysky[1]%2==1)vsledok++;
    }
    else if(p==3){
        while(zvysky[1]>0 && zvysky[2]>0){
          zvysky[1]--;
          zvysky[2]--;
          vsledok++;
        }
        if(zvysky[1]>0){
          vsledok+=(zvysky[1]/3);
          if(zvysky[1]%3>0)vsledok++;
        }
        else if(zvysky[2]>0){
          vsledok+=(zvysky[2]/3);
          if(zvysky[2]%3>0)vsledok++;
        }
    }
    else if(p==4){
        while(zvysky[1]>0 && zvysky[3]>0){
          zvysky[1]--;
          zvysky[3]--;
          vsledok++;
        }
      while(zvysky[2]>1){
        zvysky[2]--;
        vsledok++;
      }
      if(zvysky[2]==0){
          if(zvysky[1]>0){
          vsledok+=(zvysky[1]/4);
          if(zvysky[1]%4>0)vsledok++;
        }
        else if(zvysky[3]>0){
          vsledok+=(zvysky[3]/4);
          if(zvysky[3]%4>0)vsledok++;
        }
      }
      else {
        if(zvysky[1]>0){
          if(zvysky[1]>1){
            zvysky[1]-=2;
            vsledok++;
            vsledok+=(zvysky[1]/4);
            if(zvysky[1]%4>0)vsledok++;
          }
          else vsledok++;
        }
        else if(zvysky[3]>0){
            if(zvysky[3]>1){
            zvysky[3]-=2;
            vsledok++;
            vsledok+=(zvysky[3]/4);
            if(zvysky[3]%4>0)vsledok++;
          }
          else vsledok++;
        }
      }
    }
    cout <<vsledok<<endl;
  }
  return 0;
}
