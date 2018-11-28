#include<bits/stdc++.h>
using namespace std;

int main()
{
	int T;
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		char num[25];
		scanf("%s",num);
		int l=strlen(num);
		for(int i=l-1;i>0;i--)
		{
			int curr=num[i]-'0';
			int prev=num[i-1]-'0';
			if (prev>curr)
			{
				for(int j=i;j<l;j++)
				{
					if (num[j]=='9')
						break;
					num[j]='9';
				}
				prev=prev-1;
				num[i-1]=prev+'0';
			}
		}
		if(num[0]=='0')
			printf("Case #%d: %s\n",t,&num[1]);
		else
			printf("Case #%d: %s\n",t,num);
	}
}