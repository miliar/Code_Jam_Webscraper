#include<iostream>
#include<cstring>

using namespace std;

int main()
{
string s;
int t,k;

cin>>t;

for(int i=1;i<=t;i++)
{
cin>>s>>k;

cout<<"Case #"<<i<<": ";

if(k>s.size())
{
	int g =0;

	for(int j=0;j<=s.size();j++)
	{
		if(s[j]=='-')
		{
			g=1;
		}
	}
	if(g==0)
	{
		cout<<0<<endl;
	}
	else
	{
		cout<<"IMPOSSIBLE"<<endl;
	}
	continue;
}

int count = 0;
for(int j=0;j<=s.size()-k;j++)
{
	if(s[j]=='-')
	{
		count++;
		for(int l = 0; l<k; l++)
		{
			if(s[j+l]=='-')
			{
				s[j+l] = '+';
			}
			else
			{
				s[j+l] = '-';
			}
		}
	}
}

int f=0;


for(int j=s.size()-k; j<s.size(); j++)
{
	if(s[j]=='-')
	{
		f=1;
	}
}



if(f==0)
{
	cout<<count<<endl;
}
else
{
	cout<<"IMPOSSIBLE"<<endl;
}

}

}