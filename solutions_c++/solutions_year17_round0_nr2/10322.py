#include<iostream>
using namespace std;

void conv(int x,int *d){
int c[20],i=1;
//cout<<x<<endl;
while(x){
c[i++]=x%10;
x/=10;
}
//cout<<endl;
i--;
//cout<<"i="<<i<<endl;
c[0]=i;//cout<<"c[0]="<<c[0];
//cout<<"\nc array: ";
//i=1;
//while(i<=c[0])cout<<c[i++]<<" ";
int k=1;
d[0]=c[0];
while(i>0){
d[k++]=c[i--];
}
/*k=d[0];i=0;
cout<<" after conversion: ";
while(i<=k){
cout<<d[i++]<<" ";
}*/
}

bool istidy(int *x){
int a=x[0];
while(a>1){
if(x[a]<x[a-1])return false;
a--;
}
return true;
}

int main(){
int t;
cin>>t;
for(int i=1; i<=t; i++){
int n,ans=0;
cin>>n;
int a[20];
conv(n,a);
/*for(int j=1; j<=a[0]; j++){
cout<<a[j]<<" ";
}*/
if(n<10||istidy(a))ans=n;//{cout<<"if ";ans=n;}
else{
//cout<<"Else ";
int s=a[0],k=1;
while(k<s){
if(a[k]>a[k+1]){
//a[k]--;
int ind=k;
for(int l=k; l>1; l--){
if(a[l]-1<a[l-1]){ind=l-1;}
else break;
}
a[ind]--;
for(int j=ind+1; j<=s; j++){a[j]=9;}
goto cont;
}
k++;
}
cont:
k=1; s=a[0];
//cout<<"ans: ";
//while(k<=s)cout<<a[k++]<<" ";
//cout<<endl;
k=1; s=a[0];
while(k<=s){
ans= (ans*10)+a[k];
k++;
}
}
cout<<"Case #"<<i<<": "<<ans<<endl;
}
}
