#include<bits/stdc++.h>
#define ll long long

int main()
{
	ll t,k;
	scanf("%lld",&t);
	for(k=0;k<t;k++)
	{
		printf("Case #%lld: ",k+1);
		char a[30];
		scanf("%s",a);
		ll i,j,len=strlen(a),temp;
		for(i=0;i<len;i++)
		{
			if(a[i]>=a[i-1]&&a[i]>a[i+1])
			{
				break;
			}
		}
		if(i==len-1)
		{
			printf("%s\n",a);
		}
		else if(a[i]=='1')
		{
			for(i=1;i<len;i++)
				printf("9");
			printf("\n");
		}
		else
		{
			temp=a[i];
			j=i;
			while(a[j]==a[j-1])
			{
				a[j]='9';
				j--;
			}
			a[j]--;
			for(i++;i<len;i++)
				a[i]='9';
			printf("%s\n",a);
		}
	}
	return 0;
}
