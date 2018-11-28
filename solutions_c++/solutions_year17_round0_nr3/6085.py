#include<bits/stdc++.h>
using namespace std;

int N,K;



void solve(){
  priority_queue< int > Q;
  cin>>N>>K;
  Q.push(N);
  int ansL,ansR;
  for(int i=0;i<K;i++){
    int value=Q.top();Q.pop();
    ansL=ansR=value/2;
    if(value%2==0)ansR--;
    Q.push(ansL);
    Q.push(ansR);
  }
  cout<<ansL<<' '<<ansR<<endl;
}

int main(){
  int Tc;
  cin>>Tc;
  for(int tc=1;tc<=Tc;tc++){
    cout<<"Case #"<<tc<<": ";
    solve();
  }
  return 0;
}
