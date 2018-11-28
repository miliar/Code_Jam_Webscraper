#include <bits/stdc++.h>
using namespace std;
int main()
{
	string s;
	int t,k;
	int flag=0;
	int count = 0;
	cin >> t;
	for(int l=0;l<t;l++)
	{
		cin>>s>>k;
		flag = 0;
		count=0;
		for(int i = 0; i < s.size(); i++)
		{
			if(s[i]=='-')
			{
				for(int j = i; j < k + i; j++)
				{
					if(j == s.size() && j < k + i)
					{
						flag=1;
						break;
					}
					if(s[j] == '-')
						s[j]='+';
					else
						s[j]='-';
				}
				count++;
			}	
			if(flag==1)
			{
				break;
			}		
		}
		cout<<"Case #"<<l+1<<": ";
		if(flag == 1)
		{
			cout<<"IMPOSSIBLE"<<endl;
		}
		else
		{
			cout<<count<<endl;
		}
	}
	return 0;
}
