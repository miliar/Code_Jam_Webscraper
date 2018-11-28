#include<bits/stdc++.h>
using namespace std;
int main()
{
	int test;
	cin>>test;
	int g=1;
	while (test--)
	{
		string str;
		int k;
		cin>>str;
		cin>>k;
		cout<<"CASE #"<<g<<": ";
		g++;
		int length=str.length();
		int cnt=0;
		bool flag=false;
		
		for (int i=0;i<length;i++)
		{
			if (str[i]=='-')
			{
				if ((i+k)>length)
				{
					break;
				}
				else
				{
					cnt++;
					int j=i;
					for (int m=0;m<k;m++)
					{
						if (str[j]=='-')
							str[j]='+';
						else
							str[j]='-';
						j++;
					}
				}
			}
		}
		for (int i=0;i<length;i++)
		{
			if (str[i]=='-')
			{
				flag=true;
				break;
			}
		}
		if (flag==false)
			cout<<cnt<<endl;
		else
			cout<<"IMPOSSIBLE"<<endl;
	}
	return 0;
	
}