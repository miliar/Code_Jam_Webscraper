#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <set>
#define LL long long
#define N 100005
#define INF 0x7fffffff
using namespace std;
char a[20];
char b[20];
int T;
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt00.out","w",stdout);
	scanf("%d",&T);
	for(int case1=1;case1<=T;case1++)
	{
		memset(a,0,sizeof(a));
		memset(b,'9',sizeof(b));
		scanf("%s",a);
		int flag=1;
		int p=0;
		int len=strlen(a);
		//for(int i=0;i<len;i++)
        //    printf("%c",b[i]);
        //printf("\n");
        b[0]=a[0];
		for(int i=0;i<len-1;i++)
		{
			if(a[i]<a[i+1])
			{
				b[i+1]=a[i+1];
				p=i+1;
			}
			if(a[i]>a[i+1])
			{
				b[p]=b[p]-1;
				//printf("%d %c\n",p,b[p]);
				printf("Case #%d: ",case1);
				for(int j=0;j<len;j++)
				{
					if(b[j]=='0')continue;
					else printf("%c",b[j]);
				}
				printf("\n");
				flag=0;
				break;
			}
		}
		if(flag)printf("Case #%d: %s\n",case1,a);
	}
	return 0;
}
