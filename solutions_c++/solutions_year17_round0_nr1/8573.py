#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	long long int test;
	cin>>test;
	for(long long int t=1;t<=test;t++)
	{
		long long int k,n;
		char str[2000];
		cin>>str;
		cin>>k;
		n=strlen(str);
		long long int steps=0;
		bool flag=true;
		for(long long int i=0;i<n;i++)
		{
//			cout<<str<<" ";
			if(str[i]=='-')
			{
				if(i+k-1<n)
				{
					steps++;
					for(long long int j=i;j<=i+k-1;j++)
					{
						if(str[j]=='-')
						str[j]='+';
						else
						str[j]='-';
					}
				}
				else
				{
					flag=false;
					break;
				}
			}
		}
		if(!flag)
		cout<<"Case #"<<t<<": "<<"IMPOSSIBLE\n";
		else
		cout<<"Case #"<<t<<": "<<steps<<"\n";
	}
	return 0;
}
