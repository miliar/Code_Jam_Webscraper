#include <iostream>
#include<stdio.h>
using namespace std;
long long t,n;
long long a[100],l,num,s,r,sum,p;
int main()
{
scanf("%lld",&t);

for(long long i=0;i<t;i++)
{
scanf("%lld",&n);
sum=0;
num=n;
l=0;
while(num!=0)
{
num=num/10;
l++;
}
num=n;
s=l;
s--;
while(num!=0)
{
r=num%10;
a[s]=r;
s--;
num=num/10;
}
/*
for(int j=0;j<l;j++)
{
cout<<a[j]<<" ";
}
*/

for(long long k=l-1;k>0;k--)
{
if(a[k-1]>a[k])
{
for(long long j=k;j<l;j++)
a[j]=9;
a[k-1]=a[k-1]-1;
}
}

for(long long k=0;k<l;k++)
{
p=1;
for(long long j=1;j<=l-k-1;j++)
p=p*10;

sum=sum+a[k]*p;
}/*
for(int j=0;j<l;j++)
{
cout<<a[j]<<" ";
}
*/
//cout<<"\n";
cout<<"Case #"<<i+1<<":"<<" "<<sum<<"\n";
}
return 0;
}
