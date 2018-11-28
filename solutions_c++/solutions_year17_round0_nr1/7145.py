#include<iostream>
#include<string>
using namespace std;
int main()
{
int test;
cin>>test;
int i=1;
while(i<=test)
{
int k;
int cou1=0;
string str;
cin>>str>>k;
int cou2=0;
int flag=0;
int l=0;
while(l<str.length())
{    
if(str[l]=='-')
{
int cou=0;
int h1=l;
while(cou<k)
{
cou++;
if(h1<str.length()&&str[h1]=='-')
{
str[h1]='+';
h1++;
}
else if(str[h1]=='+'&&h1<str.length())
{
str[h1]='-';
h1++;
cou2++;
}
else
{
flag=1;
break;
}
}
cou1++;
}
l++;
}
if(flag==1)
cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
else
cout<<"Case #"<<i<<": "<<cou1<<endl;
i++;
}
}