#include<bits/stdc++.h>
using namespace std;
typedef long long ll;

ll N,P;

ll A[50];

ll t[50][50];

ll calc(ll a,ll b){
  return a/b + (a%b==0LL?0LL:1LL);
}


int solve(){
  int cc[50]={};
  ll res=0;

  while(1){
    bool flg=false;
    for(int i=0;i<N;i++)if(cc[i]==P)flg=true;
    if(flg)break;
    
    ll left=1,right=(1LL<<40);
    for(int i=0;i<N;i++){
      int id=cc[i];
      left=max(left, calc( t[i][id]*10,11*A[i]) );
      right=min(right, t[i][id]*10/ (9*A[i]) );
    }
    
    if(left<=right){
      res++;
      for(int i=0;i<N;i++)cc[i]++;
    }else{
      for(int i=0;i<N;i++){
        int id=cc[i];
        ll pp=t[i][id]*10/ (9*A[i]);
        if(pp==right)cc[i]++;
      }
    }
  }
  return res;
}

int main(){
  int Tc;
  cin>>Tc;
  for(int tc=1;tc<=Tc;tc++){
    cout<<"Case #"<<tc<<": ";
    
    cin>>N>>P;
    for(int i=0;i<N;i++)cin>>A[i];
    for(int i=0;i<N;i++){
      for(int j=0;j<P;j++){
        cin>>t[i][j];
      }
      sort(t[i],t[i]+P);
    }

    cout<<solve()<<endl;
  }
  return 0;
}
