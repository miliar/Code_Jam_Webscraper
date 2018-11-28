#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;
char a[1010];
int main()
{
	// freopen("test.in","r",stdin);
	// freopen("test.out","w",stdout);
	int i,j,k,q,l,r,K,len,COUNT;
	scanf("%d",&q);
	for(K=1;K<=q;K++)
	{
		printf("Case #%d: ",K);
		COUNT = 0;;
		scanf(" %s %d",a,&k);
		len = strlen(a);
		l = 0;
		r = k-1;
		while(r<len)
		{
			if(a[l]=='-')
			{
				COUNT++;
				for(i=l;i<=r;i++)
				{
					if(a[i]=='+')
						a[i] = '-';
					else
						a[i] = '+';
				}
			}
			l++;
			r++;
		}
		for(i=0;i<len;i++)
		{
			if(a[i]=='-')
				break;
		}
		if(i==len)
		{
			printf("%d\n",COUNT);
		}
		else
		{
			printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}