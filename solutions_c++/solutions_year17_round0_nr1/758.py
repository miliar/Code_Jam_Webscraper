#include <bits/stdc++.h>

using namespace std;

char str[1010];
bitset<1010>bit;

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	
	int T;
	scanf("%d",&T);

	for(int tt=1;tt<=T;tt++)
	{
		scanf("%s",str);

		int len=strlen(str);
		bit.reset();

		for(int i=1;i<=len;i++)
			if(str[i-1]=='-')
				bit.set(i);

		int K,ans=0;
		scanf("%d",&K);

		for(int i=1;i<=len-K+1;i++)
			if(bit.test(i))
			{
				ans++;
				for(int j=0;j<K;j++)
					bit.flip(i+j);
			}

		printf("Case #%d: ",tt);
		if(bit.count())
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n",ans);
	}
	return 0;
}