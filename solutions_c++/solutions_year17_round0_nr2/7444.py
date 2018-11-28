 #include <bits/stdc++.h>
int main()
{
	int t,n,j,z=1;
	char a[20];
	scanf("%d",&t);
	while(t--)
	{
		int x=0,i=0,j=0;
		scanf("%s",a);
		int len = strlen(a);
		if(len == 1)
		{
			printf("Case #%d: %c\n",z++,a[0]);
			continue;
		}
		while(i<len-1)
		{
			if(a[i]>a[i+1])
			{
				a[i] = a[i] - 1;
				if(a[i]<='0')
				{
					a[i]='9';
					if(i-1>=0)
					{
						a[i-1] = a[i-1] - 1; 
						if(a[i-1]=='0')
						{
							j = i-1;
							while(j>0)
								a[j--]='9';
							a[j] = '0'	;
						}
					}
					a[0]='0';
				}
				else
				{
					j=i;
					if(j-1>=0)
					{
						while(a[j]<a[j-1])
						{
							a[j-1] = a[j-1]-1;
							j--;
							i=j;
						}
					}
				}
				i++;
				while(i<len)
					a[i++]='9';
			}
			i++;
		}
		i=0;
		while(a[i]=='0')
			i++;
		printf("Case #%d: ",z++);
		for(j=i;j<len;j++)
		{
			printf("%c",a[j]);
		}
		printf("\n");
	}
}