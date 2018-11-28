#include <bits/stdc++.h>
using namespace std;

int main()
{
	int tst;
	scanf("%d",&tst);
	for(int t=1;t<=tst;t++)
	{
		int n,k;
		scanf("%d %d",&n,&k);
		int res1,res2,tmp = n;
		while(k)
		{
			if(tmp==0)
			{
				res1=res2=0;
				break;
			}
			tmp--;
			res1 = ceil((double)tmp/2);
			res2 = floor((double)tmp/2);
			if(!(k&1))
				tmp = res1;
			else
				tmp = res2;
			k>>=1;
		}
		printf("Case #%d: %d %d\n",t,res1,res2);
	}
}
