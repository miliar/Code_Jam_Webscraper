#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
const int maxn = 10010;

int n;
char ss[maxn];


int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-smallout","w", stdout);
	int t;
	int ca = 0;
	scanf("%d",&t);
	while(t--)
	{
		int ans = 0, x;
		bool flag = 0;
		scanf("%s %d",ss,&x);
		int len = strlen(ss);
		int cnt;
		for(int i = 0; i <= len - x; ++i)
		{
			if(ss[i] == '-')
			{
				ans++;
				cnt = 0;
				for(int j = i; j < len; ++j)
				{
					//cout << j << endl;
					if(cnt >= x) break;
					cnt++;
					if(ss[j] == '-') ss[j] = '+';
					else ss[j] = '-';
				}
				//cout << cnt << endl;
				//cout << ss << endl;
			}

		}
		for(int i = 0; i < len; ++i)
		{
			if(ss[i] == '-')
			{
				flag = 1;
				break;
			}
		}

		if(flag) printf("Case #%d: IMPOSSIBLE\n",++ca);
		else printf("Case #%d: %d\n",++ca,ans);
	}



	return 0;
}
/*
100
---------- 5
*/
