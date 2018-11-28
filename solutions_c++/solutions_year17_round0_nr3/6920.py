#include <bits/stdc++.h>

using namespace std;

int main(){
ios_base::sync_with_stdio(false);cin.tie(NULL);
int t;
cin>>t;
for(int i=1;i<=t;i++){
  int n,k,ls,rs;
  cin>>n>>k;
  priority_queue<int> sets;
  if(n==k){
    rs=0;
    ls=0;
  }else{
    if(k==1){
      k=0;
    }
    while(k--){
      vector<int> ba(n,0);
      if(n%2==0){
        ba[n/2-1]=1;
        sets.push(n/2);
        sets.push(n/2-1);
      }else{
        ba[n/2]=1;
        sets.push(n/2);
        sets.push(n/2);
      }
      if(k!=1){
      n=sets.top();
      sets.pop();
     }
    }
    if(n%2==0){
      ls=n/2-1;
      rs=n-n/2;
    }else{
      ls=n/2;
      rs=n/2;
    }
  }
    cout<<"Case #"<<i<<": "<<max(ls,rs)<<" "<<min(ls,rs)<<"\n";
}
return 0;
}
