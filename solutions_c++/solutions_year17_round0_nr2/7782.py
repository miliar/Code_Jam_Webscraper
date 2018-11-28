#include<iostream>
using namespace std;
int main()
{
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
int n,i,j;
string s;
cin>>n;
for(i=0;i<n;i++)
{
cin>>s;
for(j=s.length()-1;j>0;j--)
{
if(s[j]<s[j-1])
{
s[j-1]--;
while(j<s.length())
{
s[j]='9';
j++;
}
}
}
while(s[0]=='0') s.erase(s.begin());
cout<<"Case #"<<i+1<<": "<<s<<endl;
}
return 0;
}