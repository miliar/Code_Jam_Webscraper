#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
   freopen("y.out","w",stdout);
	long long t,k,l;
	string s;
    cin>>t;
	for(int m=0;m<t;m++)
	{
		cin>>s;
		cin>>k;
		int c=0;
		int flag=1;
		for(int i=0;i<s.size();i++)
		{
			if(s[i]=='-')
			{
				c++;
				for(int j=i;j<i+k;j++)
				{
					if(i+k>s.size())
					{
						flag=0;
						break;
					}
					if(s[j]=='-')
					{
						s[j]='+';
					}
					else
					{
						s[j]='-';
					}
				}

			}
			if(flag==0)
			{
				cout<<"Case #"<<m+1<<": IMPOSSIBLE"<<endl;
				break;
			}

		}
		if(flag==1)
		{
			cout<<"Case #"<<m+1<<": "<<c<<endl;
		}
	}
	return 0;
}
