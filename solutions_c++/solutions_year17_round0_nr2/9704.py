#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main(){
int t;
cin>>t;
int i=1;
while(i<=t){
long long int n;
cin>>n;
while(n>=1){
long long int no=n;
int rem1=no%10;
no=no/10;
int flag=0;
while(no){
int rem2=no%10;
if(rem1<rem2){
flag=1;
break;
}
rem1=rem2;
no=no/10;
}

if(flag==0)
break;
n--;
}

cout<<"Case #"<<i<<": "<<n;

cout<<endl;
i++;
}


return 0;
}
