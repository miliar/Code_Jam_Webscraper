 #include <bits/stdc++.h>
int main()
{
	int t,x=1,n;
	scanf("%d",&t);
	char a[1000];
	while(t--)
	{
		int i,j,flag=0,k=0;
		scanf("%s",a);
		scanf("%d",&n);
		for(j=0;j<strlen(a);j++)
		{
			if(a[j]=='-')
			{
				if(j+n>strlen(a))
				{
					flag=1;
					break;
				}
				else
				{
					k++;
					for(i=j;i<j+n;i++)
					{
						if(a[i]=='+')
							a[i]='-';
						else
							a[i]='+';
					}
				}
			}
		}
		if(flag==0)
		{
			printf("Case #%d: %d\n",x++,k);
		}
		else
		{
			printf("Case #%d: IMPOSSIBLE\n",x++);
		}
	}
	return 0;
}