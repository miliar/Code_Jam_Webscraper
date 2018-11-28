using namespace std;
#include<iostream>
#include<stdio.h>
#include<string.h>
int main ()
{///////////////////////////////////////////////////////
freopen("input.in","r",stdin);                //////////
freopen("longpancakes.out","w",stdout);//////////////
////////////////////////////////////////////////////
long long int num;int test,i,g,j,c,f;int a[20],a1[20];cin>>test;
for(int k=0;k<test;k++)
{i=0;c=0;g=0;cin>>num;
if(num<10){cout<<"Case #"<<k+1<<": "<<num<<endl;}
else{while(num>0){a[i]=num%10; num=num/10; i++;}
for(j=i-1;j>=0;j--){a1[g]= a[j];g++;}
c=g;
do{f=0;
for(int w=0;w<c;w++){if(a1[w]>a1[w+1]){a1[w]=a1[w]-1;
for(int e=w+1;e<c;e++){a1[e]=9;}break;}}
for(int w=0;w<c-1;w++){if(a1[w]>a1[w+1]){  f=1;break; }}} while(f);
cout<<"Case #"<<k+1<<": ";
long long int h=1,s=0;for(int q=c-1;q>=0;q--){s=a1[q]*h+s;h=h*10;}cout<<s<<endl;}}return 0;}
