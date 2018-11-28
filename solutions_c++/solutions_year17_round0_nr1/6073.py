#include<bits/stdc++.h>
using namespace std;
int arr[2000];
char s[10002];
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,l;
	cin>>t;
	for(l=1;l<=t;l++)
	{
		int i,n,k;
		scanf("%s%d",s,&k);
		for(i=0;s[i]!=0;i++)
		{
			if(s[i]=='+')
				arr[i]=1;
			else
				arr[i]=0;
		}
		n=i;
		int ans=0;
		for(i=0;i<=min(n-1,(n-k));i++)
		{
			if(arr[i]==1)
				continue;
			ans++;
			for(int j=0;j<k;j++)
				arr[j+i]^=1;
		}
		int ispos=1;
		for(i=0;i<n;i++)
			if(arr[i]==0)
				ispos=0;
		printf("Case #%d: ",l);
		if(ispos==0)
		{
			printf("IMPOSSIBLE\n");
		}
		else
		{
			printf("%d\n",ans);
		}
	}
	return 0;
}
