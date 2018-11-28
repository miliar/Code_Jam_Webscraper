#include<iostream>
#include<string.h>
#include<stdio.h>
using namespace std;

int main()
{
int a,b,c,d=0,e,f,ans[2000],i,j,n,o,p=0,r,z[5],v;
char g[2000],h,k,l,m,q='a',s='a',t='a',x='0';
for(e=0;e<2000;e++)
{
ans[e]=0;
}
cin>>a;
scanf(" ");
for(b=0;b<a;b++)
{
q='a';
s='a';
t='a';
for(e=0;e<5;e++)
{
z[e]=-1;
}
d=0;
p=0;







for(n=0,v=0;p!=2;n++)
{
q=getchar();
if(s=='a'&&q!=' ')
{
g[n]=q;
r=n;
}
else if(s=='a'&&q==' ')
{
s='b';
q='a';
p++;
continue;
}
if(s=='b'&&q!=' ')
{
if(q>47&&q<58)
{
z[v]=((int)q)-((int)(x));
v++;
}
else
{
goto thi;
}
}
if(s=='b'&&q==' ')
{
p++;
}
}
thi:
g[r+1]='\0';






if(z[3]==-1)
{
if(z[2]==-1)
{
if(z[1]==-1)
{
d+=z[0];
}
else if(z[1]!=-1)
{
d+=z[0]*10+z[1];
}
}
else if(z[2]!=-1)
{
d+=z[0]*100+z[1]*10+z[2];
}
}
else if(z[3]!=-1)
{
d+=z[0]*1000+z[1]*100+z[2]*10+z[3];
}






c=strlen(g);
for(e=0;e<=(c-d);e++)
{
h=g[e];
if(h=='-')
{
ans[b]+=1;
for(f=e;f<(e+d);f++)
{
if(g[f]=='-')
{
g[f]='+';
}
else if(g[f]=='+')
{
g[f]='-';
}
}
}
}
for(e=(c-d+1);e<c;e++)
{
h=g[e];
if(h=='-')
{
ans[b]=-1;
break;
}
}
}
for(e=0;e<a;e++)
{
if(ans[e]==-1)
{
cout<<"case #"<<e+1<<":  "<<"IMPOSSIBLE"<<endl;
}
else
{
cout<<"case #"<<e+1<<":  "<<ans[e]<<endl;
}
}
return 0;
}