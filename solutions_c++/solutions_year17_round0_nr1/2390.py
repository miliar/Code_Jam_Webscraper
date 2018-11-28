#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);


	int t;
	cin>>t;

	int n,k;
	string str;


	for(int trm=1;trm<=t;trm++)
	{
		cout<<"Case #"<<trm<<": ";
		cin>>str;
		cin>>k;

		int n=str.length();

		int ans=0;

		int flag=0;


		for(int i=0;i<n;i++)
		{
			if(str[i]=='-')
			{
				if(i+k<=n)
				{
					ans++;

					for(int j=i;j<(i+k);j++)
					{
						if(str[j]=='+') str[j]='-';
						else str[j]='+';
					}
				}
				else
				{
					flag=1;
					break;
				}
			}
		}

		if(flag)
		{
			cout<<"IMPOSSIBLE\n";
		}
		else
		{
			cout<<ans<<endl;
		}

		


	}
}