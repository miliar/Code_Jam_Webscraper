#include<stdio.h>
#include<string.h>
#include<math.h>
#include<list>
#include<map>
#include<stack>
#include<queue>

int main()
{
	int T;
	__int64 N;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&T);
	for(int i=0;i<T;i++)
	{
		scanf("%I64d",&N);
		__int64 R=0,x=N,num,base=1;
		while(x>0)
		{
			num=x%10;
			x/=10;
			if(num<x%10)
			{
				R=10*base-1;
				x--;
			}
			else
				R+=num*base;
			base*=10;
		}
		printf("Case #%d: %I64d\n",i+1,R);
	}
	return 0;
}