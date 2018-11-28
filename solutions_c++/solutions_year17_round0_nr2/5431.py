#include<iostream>
using namespace std;

int main()
{
int a,b,d,e,f,g[100],loop,loop2=0;
unsigned long long int c,h;
cin>>a;
for(b=0;b<a;b++)
{
cin>>c;
h=c;
d=0;
if(h==0)
{
d=0;
}
while(h!=0)
{
h/=10;
d++;
}
for(e=(d-1);e>=0;e--)
{
g[e]=c%10;
c/=10;
}
for(e=(d-1);e>0;e--)
{
if(g[e]>=g[e-1])
{
continue;
}
else
{
g[e-1]--;
for(loop=e;loop<d;loop++)
{
g[loop]=9;
}
}
}
cout<<"case #"<<b+1<<": ";
for(e=0;e<d;e++)
{
if(g[e]!=0||loop2!=0)
{
cout<<g[e];
loop2=1;
}
}
loop2=0;
cout<<endl;
}
return 0;
}