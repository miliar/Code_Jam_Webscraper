#include<cstdio>
#include<iostream>
using namespace std;
int main()
{
int x, a=1, b, i;
string c, s;
cin>>x;
while(a<=x)
{
b=0;
cin>>c;
if(c[1]!='\0')
{
while(c[b]!='\0') {
if(c[b+1]<c[b] && c[b+1] != '\0')
{
c[b]=c[b]-1;
++b;
while(c[b]!='\0')
{
c[b]='9';
++b;
}
}
else if(c[b+1]==c[b]) {
i=b;
while(c[b]==c[b+1])
{++b;}
if(c[b]>c[b+1] && c[b+1]!='\0') {
c[i++]--;
while(c[i]!='\0')
{
c[i++]='9';
b=i;
}
}
}
++b;
}
}
while(c[0]=='0')
{
c.erase(0,1);
}
cout<<"Case #"<<a<<": "<<c<<endl;
++a;
}
return 0;
}
