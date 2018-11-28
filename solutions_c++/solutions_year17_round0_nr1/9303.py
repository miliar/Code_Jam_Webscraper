#include<iostream>
#include<cstdlib>
using namespace std;
int main()
{
int t,p,l,n,c;
string s;
cin>>t;
for(int i=0;i<t;i++)
{
cin>>s>>n;
l=s.length();
p=0;c=0;
for(int j=0;j<l-n+1;j++)
{
if(s[j]=='-')
{
c++;
for(int k=j;k<j+n;k++)
{
if(s[k]=='-')s[k]='+';
else s[k]='-';
}
}
}
for(int j=l-n+1;j<l;j++)if(s[j]=='-'){p=1;break;}
cout<<"Case #"<<i+1<<": ";
if(p)cout<<"IMPOSSIBLE"<<endl;
else cout<<c<<endl;
}
return 0;
}
