#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main()
{
ll i,j,n,t,r,k,sz,pos,m,flag,fl;
cin>>t;
for(i=0;i<t;i++)
{
k=0,sz=0,flag=0,fl=1;
cin>>n;
ll  b[50];
ll a[50];
while(n!=0)
{
r=n%10;
b[sz]=r;
n=n/10;
sz++;
}
for(j=sz-1;j>=0;j--)
{
a[k]=b[j];
k++;
}
while(fl==1)
{
for(j=0;j<k-1;j++)
{flag=0;
if(a[j+1]>=a[j])
continue;
else
{flag=1;
pos=j;
break;
}
}
if(flag==1)
{
a[pos]=a[pos]-1;
for(m=pos+1;m<k;m++)
a[m]=9;
fl=1;
}
else
fl=0;
}
m=0;
while(a[m]==0)
m++;
cout<<"Case #"<<i+1<<": ";
for(j=m;j<k;j++)
{
cout<<a[j];
}
cout<<endl;
}
return 0;
}
