#include <bits/stdc++.h>
#define ll long long
#define int long long
#define M 1000000007
using namespace std;

main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	ios::sync_with_stdio(0);
	cin.tie(0);

	int t;
	cin>>t;

	cin.get();

	for(int test=1;test<=t;test++)
	{
		char arr[1009];
		cin.getline(arr,1009,' ');

		int len=strlen(arr),na[1009];
		for(int i=0;i<len;i++)
		{
			if(arr[i]=='+')
				na[i]=0;
			else
				na[i]=1;
		}

		int k;
		cin>>k;
		cin.get();

		int final[1009]={0},cnt=0;

		for(int i=0;i+k-1<len;i++)
		{
			if(final[i]==na[i])
				continue;

			cnt++;
			for(int j=i;j<i+k;j++)
				final[j]=final[j]^((int)1);
		}

		int xx=1;
		for(int i=0;i<len;i++)
		{
			if(final[i]!=na[i])
			{
				xx=0;
				break;
			}
		}

		if(xx)
			cout<<"Case #"<<test<<": "<<cnt<<"\n";
		else
			cout<<"Case #"<<test<<": "<<"IMPOSSIBLE"<<"\n";
	}
}