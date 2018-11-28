#include<bits/stdc++.h>
using namespace std;
int main(){
  int t;
  cin>>t;
  for(int i=1;i<=t;i++){
    cout<<"Case #"<<i<<": ";
    int n,k;
    cin>>n>>k;
    priority_queue<int> q;
    q.push(n);
    int cnt=0;
    while(!q.empty()){
      cnt++;
      int a=q.top();q.pop();
      a--;
      if(cnt==k){cout<<a/2+a%2<<" "<<a/2<<endl;break;}
      q.push(a/2),q.push(a/2+a%2);
    }
  }
  return 0;
}
