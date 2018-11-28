#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
using namespace std;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,n,k,ans;
	string s;
	cin>>t;
	for (int q=1;q<=t;q++)
	{
		cin>>s>>k;
		n=s.length();
		ans=0;
		for (int i=0;i<n;i++)
		{
			if (s[i]=='-')
			{
				if (i+k<=n)
				{
					ans++;
					for (int j=i;j<i+k;j++)
					{
						if (s[j]=='-')
							s[j]='+';
						else
							s[j]='-';
					}
				}
				else
					break;
			}
		}
		for (int i=0;i<n;i++)
		{
			if (s[i]=='-')
			{
				ans=-1;
			}
		}
		if(ans<0)
		{
			cout<<"Case #"<<q<<": IMPOSSIBLE\n";
		}
		else
		{
			cout<<"Case #"<<q<<": "<<ans<<"\n";
		}
	}
	return 0;
}