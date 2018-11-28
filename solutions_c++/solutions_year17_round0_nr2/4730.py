#include <iostream>
#include <string>

using namespace std;

int main()
{
  int t,i,j,k,l,f;
string s;
cin>>t;
k=1;
while(k<=t)
{
cin>>s;
 f=0;
while(f==0)
{
l=s.length();
i=1;
while(i<l && s[i]>=s[i-1])
i++;
if(i!=l)
{
j=i-1;
if(s[i-1]=='1')
while(j>=1 && s[j]=='1')
j--;

s[j]--;
i=j+1;
while(i<l)
{
s[i]='9';
i++;
}
}
else
f=1;
 
i=0;
while(i<l-1 && s[i]=='0')
i++;

s=s.substr(i);

}
cout<<"Case #"<<k<<": ";

cout<<s<<endl;
k++;
}
}
