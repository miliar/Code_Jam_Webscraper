#include<bits/stdc++.h>

#define ll long long

int main()
{
	ll t,j;
	scanf("%lld",&t);
	for(j=0;j<t;j++)
	{
		printf("Case #%lld: ",j+1);
		ll k,t1;
		char a[10009],b;
		scanf("%s",a);
		scanf("%lld",&k);
		ll i=0,l=strlen(a),fp=0,ind,c=0;
		while(a[i]=='+')
			i++;
		if(i==l)
		{
			printf("0\n");
			continue;
		}
		if(i+k>l)
		{
			printf("IMPOSSIBLE\n");
			continue;
		}
		for(;i+k<=l;i++)
		{
			if(a[i]=='+')
				continue;
			c++;
			fp=0;
			for(t1=0;t1<k;t1++)
			{
				if(a[i+t1]=='+')
				{
					a[i+t1]='-';
					fp++;
					if(fp==1)
					{
						ind=i+t1;
					}
				}
				else
				{
					a[i+t1]='+';
				}
			}
			//printf("%s\n",a);
			if(fp>0)
				i=ind-1;
			else
				i+=k-1;			
		}
		i--;
		while(i<l)
		{
			if(a[i]=='-')
				fp++;
			i++;
		}
		if(fp>0)
		{
			printf("IMPOSSIBLE\n");
		}
		else
		{
			printf("%lld\n",c);
		}		
	}
	return 0;
}
