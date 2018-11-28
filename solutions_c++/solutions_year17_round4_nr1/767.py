#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <ctime>
#include <map>
#include <set>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

int cnt[10];

void solve()
{
	int n, p;
	cin >> n >> p;
	memset(cnt, 0, sizeof(cnt));
	for (int i = 0; i < n; ++i)
	{
		int tmp;
		cin >> tmp;
		++cnt[tmp%p];
	}
	int ans = 1+cnt[0];
	if (p != 2)
	{
		for (int i = 1; i < p; ++i)
			while (cnt[i]>0 && cnt[p-i]>0)
			{
				++ans;
				--cnt[i];
				--cnt[p-i];
			}
		if (p == 3)
		{
		 	ans += cnt[1]/3 + cnt[2]/3;
		 	cnt[1]%=3;cnt[2]%=3;
		}
		if (p == 4)
		{
			while (cnt[1]>1 && cnt[2]>0)
			{
				++ans;
				cnt[1]-=2;
				cnt[2]--;
			}
			while (cnt[3]>1 && cnt[2]>0)
			{
				++ans;
				cnt[3]-=2;
				cnt[2]--;
			}
			ans += cnt[1]/4+cnt[2]/2+cnt[3]/4;
			cnt[1]%=4;cnt[3]%=4;cnt[2]%=2;
		}
	}
	else
	{
		ans += cnt[1]/2;
		cnt[1]%=2;
	}
	if (cnt[1]==0 && cnt[2]==0 && cnt[3]==0)
		--ans;
	cout << ans << endl;
}

int main()
{
	int times;
	freopen("a.in","r",stdin);
	freopen("a.txt","w",stdout);
	scanf("%d", &times);
	for (int i = 1; i <= times; ++i)
	{
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}