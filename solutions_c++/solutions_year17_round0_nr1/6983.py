#include <bits/stdc++.h>
using namespace std;

int main()
{
	int cs=1,t,k;
	cin>>t;
	string str;
	while(t--)
	{
		cin>>str>>k;
		int cnt=0;
		int len = str.length();
		for(int i=0;i<len;i++)
		{
			if(str[i]=='-')
			{
				if(i+k <= len)
				{
					cnt++;
					for(int j=i;j<i+k;j++)
					{
						if(str[j]=='-')str[j]='+';
						else str[j]='-';
					}
				}
			}
			// cout<<"i = "<<i<<"   str== "<<str<<endl;
		}

		bool ans = true;
		for(int i=0;i<len;i++)
		{
			if(str[i]=='-')
			{
				ans = false;
				break;
			}
		}

		cout<<"Case #"<<cs++<<": ";
		if(ans)cout<<cnt<<endl;
		else cout<<"IMPOSSIBLE\n";
	}
}