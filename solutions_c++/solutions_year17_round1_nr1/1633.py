#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;
int main()
{
	ios_base::sync_with_stdio(false);
	string s[50];
	long long x,i,j,T,R,C;
	cin>>T;
	for(x=1;x<=T;x++)
	{
		cin>>R>>C;
		for(i=0;i<R;i++)
		{
			cin>>s[i];
		}
		for(j=0;j<C;j++)
		{
			for(i=0;i<R;i++)
			{
				if(s[i][j]!='?'&&s[0][j]=='?')
				{
					s[0][j]=s[i][j];
					break;
				}
			}
		}
		for(j=0;j<C;j++)
		{
			for(i=1;i<R;i++)
			{
				if(s[i][j]=='?')
				{
					s[i][j]=s[i-1][j];
				}
			}
		}
		for(i=0;i<R;i++)
		{
			for(j=0;j<C;j++)
			{
				if(s[i][j]!='?'&&s[i][0]=='?')
				{
					s[i][0]=s[i][j];
					break;
				}
			}
		}
		for(i=0;i<R;i++)
		{
			for(j=1;j<C;j++)
			{
				if(s[i][j]=='?')
				{
					s[i][j]=s[i][j-1];
				}
			}
		}
		cout<<"Case #"<<x<<":\n";
		for(i=0;i<R;i++)
		{
			for(j=0;j<C;j++)
			{
				cout<<s[i][j];		
			}
			cout<<"\n";
		}
	}

	return 0;
}
