#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<algorithm>
#include<cstdlib>
#include<cmath>
using namespace std;

typedef long long ll;

int main()
{
	int T;	
	int c = 0;
	cin >> T;
	while(T--)
	{
		int n,p;
		cin >> n >> p;
		int i;
		int num[4];
		memset(num,0,sizeof(num));
		for(i=0;i<n;i++)
		{
			int tmp;
			cin >> tmp;
			num[tmp%p]++;
		}
		
		int ans = num[0];
		if(p==2)
			ans+=ceil((double)num[1]/2);
		else if(p==3)
		{
			int tmp = min(num[1],num[2]);
			ans+=tmp;
			num[1]-=tmp;
			num[2]-=tmp;
			ans+=ceil((double)num[1]/3);
			ans+=ceil((double)num[2]/3);
		}
		else
		{
			int tmp = min(num[1],num[3]);
			ans+=tmp;
			num[1]-=tmp;
			num[3]-=tmp;
			ans+=num[3]/4;
			num[3] -= num[3]/4 * 4;

			int big = 0;
			int i;
			for(i=0;i<=num[1];i++)
				if(num[2] >= i * 2)
				{
					int bigtmp = i;
					int tmpnum2 = num[2];
					int tmpnum1 = num[1];
					tmpnum2 -= i * 2;
					tmpnum1 -= i;
					bigtmp += tmpnum2/2;
					bigtmp += tmpnum1/4;
					tmpnum2 -= tmpnum2/2 * 2;
					tmpnum1 -= tmpnum1/4 * 4;
					if(num[3]!=0 && tmpnum2 == 1 && tmpnum1 == 2) bigtmp++;
					if(num[3]!=0 && tmpnum2 == 0 && tmpnum1 == 0) bigtmp++;
					if(tmpnum2 != 0)
					{
						bigtmp++;
						tmpnum1 -= 2;
					}
					if(tmpnum1 > 0) bigtmp++;
					big = max(big, bigtmp);
				}
			ans+=big;
		}
		printf("Case #%d: %d\n",++c, ans);
	}
	return 0;
}
