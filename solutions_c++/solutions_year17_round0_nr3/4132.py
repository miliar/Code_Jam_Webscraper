#include<bits/stdc++.h>
using namespace std;

typedef long long int ll; 
int main(){
ll t;
cin>>t;
for(ll r=1;r<=t;r++){
ll n,k;
cin>>n>>k;
priority_queue<int>Q;
Q.push(n);
ll p;
for(ll i=1;i<=k-1;i++){
   p=Q.top();
  Q.pop();
  if(p%2==0) {Q.push((p/2)-1); Q.push(p/2);}
  else{Q.push(p/2); Q.push(p/2);}
}
p=Q.top();
  Q.pop();ll lt,rt;
  if(p%2==0) {lt=((p/2)-1); rt=(p/2);}
  else{lt=rt=p/2;}
if(lt>rt) rt=lt;
 cout<<"Case #"<<r<<": "<<rt<<" "<<lt<<endl;
}
return 0;
}
