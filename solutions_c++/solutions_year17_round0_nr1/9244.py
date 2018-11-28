#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int p=1;p<=t;p++)
	{
		int count=0,flag=1;
		string str;
		cin>>str;
		int k;
		cin>>k;
		for(int i=0;i<str.size();i++)
		{
			if(str[i]=='-')
			{
				if((i+k-1)<str.size())
				{
					int j;
					for(j=i;j<=(i+k-1);j++)
					{
						if(str[j]=='-')
						{
							str[j]='+';
						}
						else
						{
							str[j]='-';
						}
						
					}
					count++;
					
				}
				else
				{
					flag=0;
					break;
				}
			}
		}
		if(flag==0)
		{
			cout<<"Case #"<<p<<": IMPOSSIBLE"<<endl;
		}
		else
		{
			cout<<"Case #"<<p<<": "<<count<<endl;
		}
	}
	return 0;
}
