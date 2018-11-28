
#include<bits/stdc++.h>
using namespace std;

char str[1002],c;
int t,n,k;

int main()
{
	int i,j,ans,p=0;
	scanf("%d",&t);
	while(t--)
	{
		p++;
		ans=0;
		scanf("%s%d",&str,&k);
		n=strlen(str);
		for(i=0;i<=n-k;i++)
		{
			if(str[i]=='-')
			{
				ans++;
				for(j=i;j<i+k;j++)
					if(str[j]=='-')
						str[j]='+';
					else
						str[j]='-';
			}
		}
		for(;i<n;i++)
			if(str[i]=='-')
				break;
		//cout<<str<<endl;
		if(i==n)
			printf("Case #%d: %d\n",p,ans);
		else
			printf("Case #%d: IMPOSSIBLE\n",p);
	}
	return 0;
}
