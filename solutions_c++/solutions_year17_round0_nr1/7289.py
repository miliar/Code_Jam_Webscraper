#include<iostream>
using namespace std;
int main()
{
int a, b=1, c, d, i, j;
string s;
cin>>a;
while(b<=a)
{
d=0;
i=0;
cin>>s;
cin>>c;
while(s[i+c-1]!='\0')
{
if(s[i]=='-')
{
++d;
j=0;
while(j<c) {
if(s[i+j]=='-')
s[i+j]='+';
else
s[i+j]='-';
++j;
}
}
++i;
}
while(s[i]!='\0')
{
if(s[i]=='-')
d=-1;
++i;
}
if(d==-1)
cout<<"Case #"<<b<<": IMPOSSIBLE\n";
else
cout<<"Case #"<<b<<": "<<d<<endl;
++b;
}
return 0;
}
