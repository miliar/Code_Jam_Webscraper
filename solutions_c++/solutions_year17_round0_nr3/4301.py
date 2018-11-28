#include<iostream>
#include<algorithm>
using namespace std;

long long a[1000002],t,n,k,pin,g,s,c,h;
long long b[2][1000002];
long long d[1000002],maxi,num,r,l,tin,bin,jin,tt,rs,ls,ttt;
long long st[1000002],top;
long long e[1000002],kk;
int main()
{
cin>>t;

for(long long i=0;i<t;i++)
{
cin>>n>>k;
top=-1;
a[0]=1;
a[n+1]=1;
h=g=s=c=pin=num=maxi=r=tt=jin=rs=ls=ttt=0;

for(long long j=1;j<=n;j++)
a[j]=0;

b[0][0]=n;
if(n%2==0)
b[1][0]=n/2;
else b[1][0]=n/2+1;
g=1;
s=0;
while(s!=g)
{
pin=b[0][s];
c=b[1][s];
if(pin%2!=0&&pin>1)
{
if(pin/2>0)
{
b[0][g]=pin/2;
b[1][g]=c-b[0][g]/2-1;
g++;
b[0][g]=pin/2;
if(b[0][g]%2==0)
b[1][g]=c+b[0][g]/2;
else b[1][g]=c+b[0][g]/2+1;
g++;
}
}
else if(pin%2==0&&pin>1)
{
if(pin/2>1)
{
b[0][g]=pin/2-1;
b[1][g]=c-b[0][g]/2-1;
g++;
}
if(pin/2>0)
{
b[0][g]=pin/2;
if(b[0][g]%2==0)
b[1][g]=c+b[0][g]/2;
else b[1][g]=c+b[0][g]/2+1;
g++;
}
}
s++;
}


/*
for(long long x=0;x<g;x++)
cout<<b[0][x]<<" ";
cout<<"\n";
for(long long x=0;x<g;x++)
cout<<b[1][x]<<" ";
cout<<"\n";
*/

maxi=b[1][0];

for(long long j=1;j<g;j++)
{
 maxi=max(maxi,b[1][j]);
}
num=maxi;
r=0;
while(num!=0)
{
r++;
num=num/10;
}

num=1;
for(long long j=0;j<r;j++)
{
num=num*10;
}
l=num;
for(long long j=0;j<g;j++)
d[j]=b[0][j]*num+b[1][j];

sort(d,d+g);
num=0;
for(long long j=0;j<g;j++)
{
num=d[j];
for(long long x=1;x<=r;x++)
{
num=num/10;
}
b[0][j]=num;
b[1][j]=d[j]-num*l;
}

for(long long x=g-1;x>=0;x--)
{
top++;
st[top]=x;
if(x-1>=0)
{
while(b[0][x]==b[0][x-1])
{
top++;
st[top]=x-1;
x--;
}
}
while(top!=-1)
{
e[h]=st[top];
h++;
if(h==k)
{
ttt=1;
break;
}
top--;
}
//cout<<"h="<<h<<"\n";
//cout<<"k="<<k<<"\n";
if(ttt==1)
{
break;
}
}
/*
for(long long x=0;x<g;x++)
cout<<b[0][x]<<" ";
cout<<"\n";
for(long long x=0;x<g;x++)
cout<<b[1][x]<<" ";
cout<<"\n";

for(long long x=0;x<h;x++)
cout<<e[x]<<" ";
cout<<"\n";
*/
for(long long x=0;x<h;x++)
{
tin=e[x];
bin=b[1][tin];
a[bin]=1;
}
kk=e[h-1];
jin=b[1][kk];
tt=jin+1;
//cout<<jin<<"\n";
ls=0;
rs=0;
while(a[tt]!=1)
{
rs++;
tt++;
}
tt=jin-1;
while(a[tt]!=1)
{
ls++;
tt--;
}
/*
for(long long x=0;x<n+2;x++)
cout<<a[x]<<" ";
cout<<"\n";
*/
cout<<"Case #"<<i+1<<":"<<" "<<max(ls,rs)<<" "<<min(ls,rs)<<"\n";
}
return 0;
}
