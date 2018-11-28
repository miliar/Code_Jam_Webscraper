#include<iostream>
#include<cstring>
using namespace std;
int main()
{
long long int s,r,att,tem,o,n,no;
cin>>s;
no=1;
while(s--)
{
att=0,tem=0;
string a;
cin>>a;
cin>>o;
long long int l=a.length();
if (o<=0)
cout<<"Case #"<<no<<": "<<"IMPOSSIBLE"<<endl;
else
{
for(n=0;n<=(l-o);n++)
{
if(a[n]=='-')
{
a[n]='+';
for(r=n+1;r<n+o;r++)
{
if(a[r]=='-')
a[r]='+';
else if(a[r]=='+')
a[r]='-';
}
att++;
}
}
for(n=0;n<l;n++)
{
if(a[n]=='-')
{
tem=1;
break;
}
}
if(tem==0)
{
cout<<"Case #"<<no<<": "<<att<<endl;
}
else
cout<<"Case #"<<no<<": "<<"IMPOSSIBLE"<<endl;
}
no++;
}
return 0;
}