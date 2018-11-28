#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
using namespace std;
#include<string>
void main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int testcases;
	cin>>testcases;

	string s;
	int k;
	int counter;
	for(int t=1;t<=testcases;t++)
	{
		counter=0;
		cin>>s;
		cin>>k;
		for(int i=0;i<s.length();i++)
		{
			if(s[i]=='-')
			{
				int j=i;
				if((s.length()-i)>=k)
				{
				for(int r=0;r<k;r++)
				{
					if(j<s.length())
					{
					if(s[j]=='-')
						s[j]='+';
					else
						s[j]='-';
					}
					j++;
				}
				counter++;
				}
			}
		}
		bool z=false;
		for(int i=0;i<s.length();i++)
		{
			if(s[i]=='-')
			{
				cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
				z=true;
				break;
			}
		}
		if(z==false)
		{
			cout<<"Case #"<<t<<": " << counter<<endl;
		}
	}
}