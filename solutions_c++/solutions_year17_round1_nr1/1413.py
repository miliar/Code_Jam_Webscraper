#include<iostream>
using namespace std;

int main()
{
	int t,ti,i,n,j,bp,fp,k;
	cin>>t;
	for(ti = 1;ti<=t;ti++)
	{
		int r,c;
		string s[30];
		cin>>n>>c;
		for(i = 1;i<=n;i++)
		{
			cin>>s[i];
		}
		int fi = 0;
		for(i = 1;i<=n;i++)
		{
			bool found = false;
			for(j = 0;j<c;j++)
			{
				if(s[i][j] != '?')
				{
					fi = i;
					found = true;
					break;
				}
			}
			if(found == true)
			{
				break;
			}
		}
		for(i = fi;i<=n;i++)
		{
			bool avail = false;
			bp = 0;
			for(fp = 0;fp<c;fp++)
			{
				if(s[i][fp] != '?')
				{
					for(k = bp;k<fp;k++)
					{
						s[i][k] = s[i][fp];
					}
					bp = fp+1;
					avail = true;
				}
			}
			if(avail == true)
			{
				for(k = bp;k<c;k++)
				{
					s[i][k] = s[i][bp-1];
				}
			}
			else
			{
				for(j = 0;j<c;j++)
				{
					s[i][j] = s[i-1][j];
				}
			}
		}
		for(i = 1;i<fi;i++)
		{
			for(j = 0;j<c;j++)
			{
				s[i][j] = s[fi][j];
			}
		}
		cout<<"Case #"<<ti<<":"<<"\n";
		for(i = 1;i<=n;i++)
		{
			for(j = 0;j<c;j++)
			{
				cout<<s[i][j];
			}
			cout<<"\n";
		}
	}
}
