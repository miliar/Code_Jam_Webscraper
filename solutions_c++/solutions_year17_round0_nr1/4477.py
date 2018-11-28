#include<bits/stdc++.h>
using namespace std;
int main()
{
int i,j,n,t,k,m,count,flag;
cin>>t;
for(i=0;i<t;i++)
{count=0,flag=0;
string s;
cin>>s>>k;
for(j=0;j<s.size();j++)
{
if(s[j]=='-' and j<=(s.size()-k))
{
for(m=0;m<k;m++)
{
if(s[j+m]=='-')
{
s[j+m]='+';
}
else
s[j+m]='-';
}
count++;
}
}
for(j=0;j<s.size();j++)
{
if(s[j]=='-')
{
flag=1;
break;
}
}
if(flag==0)
cout<<"Case #"<<i+1<<": "<<count<<endl;
else
cout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<endl;
}
return 0;
}
