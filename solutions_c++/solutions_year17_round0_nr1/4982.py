#include<bits/stdc++.h>

using namespace std;

int main()
{
	int t,n,cs=0,ans=0,k,i;
	char c;
	vector<int> v;
	scanf("%d",&t);
	while(t--)
	{	
		cs++;
		printf("Case #%d: ",cs);
		v.clear();
		ans=0;
		string inp;
		cin>>inp;
		n = inp.length();
		v.resize(n,0);
		for(i=0;i<n;i++)
		{
			if(inp[i]=='+')
				v[i] = 1;
		}
		scanf("%d",&k);
		for(i=0; i< n-k+1 ;i++)
		{
			if(v[i] == 0)
			{
				for(int j=0;j<k;j++)
				{

						v[i+j] = 1 - v[i+j];
				}
				ans++;
			}
		}
		bool ok=true;
	for(i=0;i<n;i++)
	{
		if(v[i]==0)
		{
			ok = false;
			break;
		}
	}
		if(ok)
			printf("%d\n",ans);
		else
			printf("IMPOSSIBLE\n");
	}

	return 0;
}