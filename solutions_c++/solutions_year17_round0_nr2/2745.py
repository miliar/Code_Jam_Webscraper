#include <iostream>
using namespace std;

int main() {
int t;
cin>>t;
int m=0;
while(t>0)
{
t--;
m++;
cout<<"Case #"<<m<<": ";
string s;
cin>>s;
int index=s.size();
for(int i=s.size()-1;i>=1;i--)
{
	if(s[i]<s[i-1])
	{s[i-1]--;
	index=i;
	}
}
for(int j=index;j<s.size();j++)
s[j]='9';

int l=0;
for(int i=0;i<s.size();i++)
{
	if(s[i]=='0')
	l++;
}
for(int i=l;i<s.size();i++)
cout<<s[i];

cout<<endl;
}
	return 0;
}