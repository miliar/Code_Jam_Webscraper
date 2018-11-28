#include<iostream>
#include<cstring>
#include<vector>
#define ll long long

using namespace std;

int main()
{
ll t;

cin>>t;
for(ll j=1;j<=t;j++)
{

string a;
vector<int> s;

cin>>a;

if(a=="0")
{
	cout<<"Case #"<<j<<": 0"<<endl;
	continue;
}

for(ll i=0;i<a.size();i++)
{
	s.push_back(a[i]-'0');
}

int f = 0,in = s.size()-1;
for(ll i=0;i<s.size();i++)
{

	if(f==1)
	{
		s[i] = 9;
	}

	if(s[i]>s[i+1] && f==0 && i!=s.size()-1)
	{
		f=1;
		s[i]--;
		in = i;
	}

}

for(ll i=in;i>0;i--)
{
	if(s[i]<s[i-1])
	{
		s[i-1]--;
		s[i]=9;
	}
	else
	{
		break;
	}
}


cout<<"Case #"<<j<<": ";

for(int i=0;i<s.size();i++)
{
	if(s[i]!=0)
	cout<<s[i];
}
cout<<endl;

}

return 0;
}