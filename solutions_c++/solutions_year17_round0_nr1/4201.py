#include <iostream>
#include<string>
using namespace std;
char a[1000],ch;
string str;
long t,n,ct,l,m,p,sum,s;
int main()
{
cin>>t;

for(long i=0;i<t;i++)
{
ct=0;
cin>>str;
cin>>m;
l=str.length();
for(long k=0;k<l;k++)
a[k]=str[k];


sum=0;
for(long k=0;k<=l-m;k++)
{
if(a[k]=='+')
continue;
else
if(a[k]=='-')
{
sum++;
for(long j=k;j<k+m;j++)
{
if(a[j]=='-')
a[j]='+';
else if(a[j]=='+')
a[j]='-';
}
s=0;
while(a[s]!='-')
s++;
if(s>k)
k=s-1;
}
}
p=1;
for(long j=0;j<l;j++)
{
if(a[j]=='-')
p=0;
}
/*
for(long k=0;k<l;k++)
cout<<a[k]<<" ";
*/
if(p==1)
cout<<"Case #"<<i+1<<":"<<" "<<sum<<"\n";
else
cout<<"Case #"<<i+1<<":"<<" "<<"IMPOSSIBLE"<<"\n";
}
return 0;
}
