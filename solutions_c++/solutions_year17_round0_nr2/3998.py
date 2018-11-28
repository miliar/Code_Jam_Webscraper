#include<bits/stdc++.h>
using namespace std;


typedef long long int ll;

int main(){
ll l,t;
cin>>t;
for(ll r=1;r<=t;r++){
ll n[20]={0};
ll n1;
cin>>n1;
ll y=0;
while(n1>0){
  ll q=n1%10;
  n[y]=q;
  n1/=10;
  y++;
}
ll arr[y];ll x=0,x1=0;
for(ll i=19;i>=0;i--){
  if(x) arr[x1++]=n[i];
   else if(n[i]!=0) {arr[x1++]=n[i];x=1;   }
}ll po=1;bool a=false;ll pop;
int lk=1;
while(lk){ll val=0;
for(ll i=0;i<y-1;i++){
  if(arr[i]>arr[i+1] && po==1) {arr[i]=arr[i]-1; po=0;pop=i;a=true;}
  
}
if(a)
for(ll i=pop+1;i<y;i++)
  arr[i]=9;
  for(ll i=0;i<y-1;i++) if(arr[i]<=arr[i+1]) val++;
 if(val==y-1) lk=0;
po=1;
}  
 ll sum=0;
for( ll i=0;i<y;i++) sum=sum*10+arr[i];

 cout<<"Case #"<<r<<": "<<sum<<endl;

}
return 0;
}
