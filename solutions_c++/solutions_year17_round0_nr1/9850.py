#include<bits/stdc++.h>
using namespace std;
main()
{
	int t;
	cin>>t;
	ofstream file("oversizedPanckaes.txt");
	for(int i=1;i<=t;i++)
	{
		long long ans=0;
		int sz;
		char s[1001];
		scanf("%s %d",s,&sz);
		int l=strlen(s);
		for(int j=0;j<=l-sz;j++)
		{
			if(s[j]=='-')
			{
				for(int k=j;k<j+sz;k++)
				{
					if(s[k]=='-')
					s[k]='+';
					else
					s[k]='-';
				}
				ans++;
			}
			for(int k=0;k<l;k++)
			{
				cout<<s[k];
			}
			cout<<endl;
		}
		int out=1;
		for(int j=0;j<l;j++)
		{
			if(s[j]=='-')
			{
				out=0;
				break;
			}
		}
		if(out)
		{
			file<<"Case #"<<i<<": "<<ans<<endl;
		}
		else
		{
			file<<"Case #"<<i<<": IMPOSSIBLE"<<endl;
		}
	}	
	file.close();
	return 0;
}
