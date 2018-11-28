#include<bits/stdc++.h>
using namespace std;

typedef long long int ll; 
int main(){
ll t;
cin>>t;
for(ll r=1;r<=t;r++){
  char S[2000];ll po;
  cin>>S>>po;
  ll sum=0;ll flag=0;
  ll k=strlen(S);
  for(ll i=0;i<k;i++){
     if(S[i]=='-'){
         if(i+po-1<k){
         for(int j=0;j<po;j++) {if(S[i+j]=='-') S[i+j]='+'; else S[i+j]='-';}
         sum++;}
         else flag=1;
     }
  }
  if(!flag)
 cout<<"Case #"<<r<<": "<<sum<<endl;
 else cout<<"Case #"<<r<<": IMPOSSIBLE"<<endl;
   
}
return 0;
}
