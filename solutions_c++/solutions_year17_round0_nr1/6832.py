#include<iostream>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		string s;
		long long int k;
		cin>>s;
		cin>>k;
		 int a[s.length()];
		for(int j=0;j<s.length();j++)
		{
			if(s[j]=='+')
			{
				a[j] = 1;
			}
			else
			{
				a[j] = 0;
			}
		}
		int n = s.length();
	
		long long int ans=0;
		int flag=0;
		n--;
		while(1)
		{
			if(n==-1)
			{
				break;
			}
			if(a[n]==0 && (n+1-k)>=0)
			{
				for(int z = 0;z<k;z++)
				{
					a[n-z] = !a[n-z];
				}
				ans++;
			}
			else if(a[n]==0 && (n+1-k)<0)
			{
				flag=1;
				break;
			}
			n--;
		}
		if(flag==1)
		{
			printf("Case #%d: IMPOSSIBLE\n",i+1);
		}
		else
		{
			printf("Case #%d: %lld\n",i+1,ans);
			
		}
	}
	return 0;
}
