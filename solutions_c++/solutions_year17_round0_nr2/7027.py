#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
char num[30];
int main()
{
	// freopen("test.in","r",stdin);
	// freopen("test.out","w",stdout);
	int i,j,n,q,k,len;
	scanf("%d",&q);
	for(k=1;k<=q;k++)
	{
		printf("Case #%d: ",k);
		scanf(" %s",num);
		len = strlen(num);
		if(len==1)
		{
			printf("%s\n",num);
			continue;
		}
		for(i=0;i<len-1;i++)
		{
			if(num[i]>num[i+1])
			{
				break;
			}
		}
		if(i==len-1)
		{
			printf("%s\n",num);
			continue;
		}
		for(i=i;i>0;i--)
		{
			if(num[i-1]!=num[i])
			{
				break;
			}
		}
		num[i]--;
		for(i=i+1;i<len;i++)
		{
			num[i] = '9';
		}
		if(num[0]=='0')
			printf("%s\n",&num[1]);
		else
			printf("%s\n",num);
	}
	return 0;
}