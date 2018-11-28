#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("inp.txt","r",stdin);
	freopen("res.txt","w",stdout);
	long long int t,len,i,j,flag,count;
	scanf("%lld",&t);
	for(j=1;j<=t;j++)
	{
		char str[10000];
		count=0;
		scanf("%s",str);
		len=strlen(str);
		printf("Case #%lld: ",j);
		if(len>1)
		{
			flag=0;
			for(i=0;i<len-1;i++)
			{
				if(str[i] < str[i+1])
				{
					printf("%c",str[i]);
					while (count!=0)
					{
						printf("%c",str[i]);
						count--;
					}
				}
				else if(str[i]==str[i+1])
				{
					count++;
				}
				else
				{
					str[i]--;
					if(str[i]!='0')
					{
						printf("%c",str[i]);
					}
					while(count!=0)
					{
						printf("9");
						count--;
					}
					i++;
					flag=1;
					break;
				}
			}
			if(count!=0)
			{
				count++;
				while(count!=0)
				{
					printf("%c",str[i]);
					count--;
				}
			}
			else
			{
				if(flag==0)
				{
					printf("%c",str[i]);
				}
				else
				{
					while(i<len)
					{
						printf("9");
						i++;
					}
				}
			}
			printf("\n");
		}
		else
		{
			printf("%c\n",str[0]);
		}
	}
	return 0;
}
