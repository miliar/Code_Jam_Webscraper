#include<bits/stdc++.h>
using namespace std;

void foo()
{
	string s;
	cin>>s;

	int n = s.length();

	int i;
	int dipindex = -1;

	for(i=0;i<n-1;i++)
	{
		if(s[i]>s[i+1])
		{
			dipindex = i;
			break;
		}
	}

	if(dipindex==-1)
	{
		cout<<s<<endl;
		return;
	}

	int lefteq =0 ;
	char x = s[dipindex];

	for(i=dipindex;i>=0;i--)
	{
		if(s[i]!=x)
		{
			lefteq = i+1;
			break;
		}
	}
	s[lefteq]--;
	for(i=lefteq+1;i<n;i++)
	{
		s[i]='9';
	}

	for(i=0;i<n;i++)
	{
		if(s[i]!='0')
			break;
	}

	for(;i<n;i++)
	{
		cout<<s[i];
	}
	cout<<endl;


}

int main(int argc, char const *argv[])
{
	int t;
	cin>>t;
	int i;
	for(i=1;i<=t;i++)
	{
		cout<<"Case #"<<i<<": ";
		foo();
	}
	return 0;
}