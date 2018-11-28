#include<iostream>
using namespace std;
int main()
{
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
int n,i,j,k,l,o;
string s;
cin>>n;
for(i=0;i<n;i++)
{
cin>>s>>l;
k=0;
for(j=0;j<s.length()-l+1;j++)
{
if(s[j]=='-')
{
for(o=j;o<j+l;o++)
{
s[o]='+'+'-'-s[o];
}
k++;
}
}
for(;j<s.length();j++)
{
if(s[j]=='-') k=-1;
}
if(k>=0) cout<<"Case #"<<i+1<<": "<<k<<endl;
else cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
}
return 0;
}