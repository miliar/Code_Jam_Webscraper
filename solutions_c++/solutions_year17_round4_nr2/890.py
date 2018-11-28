#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,u=1;
	cin>>t;
	while(t--)
	{
		int arr[3][1032]={0};
		int i,n,c,m;
		cin>>n>>c>>m;
		for(i=0;i<m;i++)
		{
			int a,b;
			cin>>a>>b;
			arr[b][a]++;
		}
		int ans=0,req=0,kk=2;
		for(i=1;i<=n;i++)
		{
			int r=arr[1][i];
			int j=i+1;
			while(j<=n&&r>0)
			{
				int k=min(arr[2][j],r);
				r-=k;
				arr[2][j]-=k;
				ans+=k;
				j++;
			}
			arr[1][i]=r;
		}
		for(i=1;i<=n;i++)
		{
			int r=arr[2][i];
			int j=i+1;
			while(j<=n&&r>0)
			{
				int k=min(arr[1][j],r);
				r-=k;
				arr[1][j]-=k;
				ans+=k;
				j++;
			}
			arr[2][i]=r;
		}
		int f=0;
		for(i=1;i<=n;i++)
		{
			if(arr[1][i]==0&&arr[2][i]==0)
			continue;
			f++;
			if(arr[1][i]>0&&arr[2][i]>0)
			{
				if(i==1)
				ans+=arr[1][i]+arr[2][i];
				else
				{
					req=min(arr[1][i],arr[2][i]);
					ans+=max(arr[1][i],arr[2][i]);
				}
			}
			else
			ans+=arr[1][i]+arr[2][i];
		}
		//assert(f<=1);
		printf("Case #%d: %d %d\n",u,ans,req);
		u++;
	}
	return 0;
}
