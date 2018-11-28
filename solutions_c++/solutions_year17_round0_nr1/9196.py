#include<iostream>
#include<fstream>
using namespace std;
char flip(char c)
{
	if(c=='-')
	{
		return '+';
	}
	return '-';
}
int main()
{
	int t,tc;
	cin>>t;
	ofstream f;
	f.open("pancake.txt");
	for(tc=0;tc<t;tc++)
	{
		int n,i,count=0,p,j;
		string s;
		cin>>s>>n;
		for(i=0;i<(s.length()-(n-1));i++)
		{
			if(s[i]=='-')
			{
				count++;
				j=i;p=0;
				while(p<n)
				{
					s[j]=flip(s[j]);
					j++;
					p++;
				}
			}
		}
		for(i=0;i<s.length();i++)
		{
			if(s[i]=='-')
			{
				break;
			}
		}
		if(i==s.length())
		{
			f<<"Case #"<<tc+1<<": "<<count<<endl;
		}
		else
		{
			f<<"Case #"<<tc+1<<": IMPOSSIBLE"<<endl;
		}
	}
}
