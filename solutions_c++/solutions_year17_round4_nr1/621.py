#include <bits/stdc++.h>
using namespace std;
using namespace chrono;

int a[105];
int b[4];
int n, p;

int solve()
{
	int ans = 0;
	b[0] = b[1] = b[2] = b[3] = 0;
	scanf("%d%d", &n, &p);
	for (int i = 0;i < n;i++) scanf("%d", a+i), b[a[i]%p]++;
	if (p == 2)
	{
		ans = b[0]+(b[1]+1)/2;
	} else if (p == 3)
	{
		ans = b[0]; b[0] = 0;
		int cur = 0;
		if (b[2] > b[1])
		{
			cur = 2; b[2]--; ans++;
		}
		while (b[1] && b[2])
		{
			if (cur == 0) ans++;
			cur = (cur+1)%3; b[1]--;
			if (cur == 0) ans++;
			cur = (cur+2)%3; b[2]--;
		}
		while (b[1])
		{
			if (cur == 0) ans++;
			cur = (cur+1)%3; b[1]--;
		}
		while (b[2])
		{
			if (cur == 0) ans++;
			cur = (cur+2)%3; b[2]--;
		}
	} else if (p == 4)
	{
		ans = b[0];
		while (b[1] && b[3])
		{
			b[1]--; b[3]--;
			ans++;
		}
		while (b[1] >= 2 && b[2])
		{
			b[1] -= 2; b[2]--;
			ans++;
		}
		while (b[3] >= 2 && b[2])
		{
			b[3] -= 2; b[2]--;
			ans++;
		}
		while (b[2] >= 2)
		{
			b[2] -= 2;
			ans++;
		}
		while (b[1] >= 4)
		{
			b[1] -= 4;
			ans++;
		}
		while (b[3] >= 4)
		{
			b[3] -= 4;
			ans++;
		}
		fprintf(stderr, "%d %d %d ", b[1], b[2], b[3]);
		int cur = 0;
		while (b[1])
		{
			if (cur == 0) ans++;
			cur = (cur+1)%4;
			b[1]--;
		}
		while (b[2])
		{
			if (cur == 0) ans++;
			cur = (cur+2)%4;
			b[2]--;
		}
		while (b[3])
		{
			if (cur == 0) ans++;
			cur = (cur+3)%4;
			b[3]--;
		}
	}
	return ans;
}

int main()
{
	int t; scanf("%d", &t);
	for (int _ = 1;_ <= t;_++)
	{
		fprintf(stderr, "\tCase #% 3d...", _); fflush(stdout);
		milliseconds start_ti = duration_cast<milliseconds>(system_clock::now().time_since_epoch());

		printf("Case #%d: %d\n", _, solve());

		milliseconds end_ti = duration_cast<milliseconds>(system_clock::now().time_since_epoch());
		long long time_used = end_ti.count() - start_ti.count();
		fprintf(stderr, " done\t% 6lldms\n", time_used); fflush(stdout);
	}
	fprintf(stderr, "\n\n\n");
	return 0;
}
