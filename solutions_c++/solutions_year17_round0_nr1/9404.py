#include<iostream>
#include<string>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=0; i<t;i ++)
	{
		string s;
		cin>>s;
		int n;
		cin>>n;
		int count=0;
		for(int j=0; j<s.length();j++)
		{
			if(s[j]=='-')
			{
			count+=1;
				for(int q=j;q<s.length() && q<(j+n)&& j+n<=s.length();q++)
				{
				if(s[q]=='-')
				{s[q]='+';}
				else if(s[q]=='+')
				{s[q]='-';}
				}
			}
		}
		bool sol=true;
		for(int j=0;j<s.length();j++)
		{
		if(s[j]=='-')
		{sol=false;
		break;}
		}
		
		if(sol==true)
		{cout<<"Case #"<<i+1<<": "<<count<<endl;}
		else
		{cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;}	
	}

return 0;
}
