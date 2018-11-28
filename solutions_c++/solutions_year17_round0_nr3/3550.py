#include<bits/stdc++.h>
using namespace std;
#define int long long
signed main(){
  int T;
  cin>>T;
  for(int t=1;t<=T;t++){
    cout<<"Case #"<<t<<": ";
    priority_queue<int> q;
    int n,k;
    cin>>n>>k;
    q.push(n);
    int p,l,r;
    for(int i=0;i<k;i++){
      p=q.top();q.pop();
      l=(p-1)/2;
      r=(p-1)-l;
      q.push(l);
      q.push(r);
    }
    cout<<r<<" "<<l<<endl;
  }
  return 0;
}
