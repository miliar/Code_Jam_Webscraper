#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		int x;
		char a[1002];
		cin>>a>>x;
		int l=strlen(a);
		int flag=1,count=0;
			for(int k=0;k<l;k++)
			{
				if(a[k]=='-'&&k<=l-x)
				{
					for(int f=k;f<x+k;f++)
					{
						if(a[f]=='-')
						a[f]='+';
						else
						a[f]='-';
					}
					count++;
				}
			}
			for(int k=0;k<l;k++)
			{
				if(a[k]=='-')
				{
					flag=0;
					break;
				}
			}
			if(flag)
			cout<<"Case #"<<i<<": "<<count<<endl;
			else
			cout<<"Case #"<<i<<": IMPOSSIBLE\n";
	}
	return 0;
}
