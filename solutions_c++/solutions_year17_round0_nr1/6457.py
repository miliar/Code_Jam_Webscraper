#include <bits/stdc++.h>

using namespace std;

//use scanint(variable) for integer input instead of scanf
int main()
{
	int t;
	scanf("%d", &t);
	for(int p=1;p<=t;p++)
	{
		string str;
		cin>>str;
		int k;
		scanf("%d", &k);
		int n=str.size();
		int i=0,count=0;
		for (i = 0; i <= n-k; ++i)
		{
			if (str[i]=='-')
			{
				for (int j = 0; j < k; ++j)
				{
					if (str[i+j]=='+')
					{
						str[i+j]='-';
					}
					else
						str[i+j]='+';
				}
				count++;
			}
		}
		int flag=1;
		for (; i < n; ++i)
		{
			if (str[i]=='-')
			{
				flag=0;
				break;
			}
		}
		if (flag)
		{
			cout<<"Case #"<<p<<": "<<count<<endl;
		}
		else
			cout<<"Case #"<<p<<": "<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}