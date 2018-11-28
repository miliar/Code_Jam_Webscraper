#include <bits/stdc++.h>

#define pii pair<int, int>
#define pll pair<LL, LL>
#define F first
#define S second
#define B begin()
#define E end()
#define MOD 1000000007
#define itt iterator
#define ritt reverse_iterator
#define LL long long

#define PI (4 * atan(1))

using namespace std;

int t, n, p, r[55], q[55][55], ok, cnt, id[55], idf[55], ids[55], m, mxx;
LL mn, mx;

void bsearch(int f, int b, int row, LL x, int mode)	// 1 find f | 2 find s
{
	if(f > b)
		return;

	m = (f + b) / 2;
	if((mode == 1 && q[row][m] >= x) || (mode == 2 && q[row][m] >= x))
	{
		if(mode == 1)
			idf[row] = m;
		bsearch(f, m - 1, row, x, mode);
	}
	else
	{
		if(mode == 2)
			ids[row] = m;
		bsearch(m + 1, b, row, x, mode);
	}
}

int main()
{
	// freopen("D:\\Computer\\TestingArea\\test.in", "r", stdin);
	// freopen("D:\\Computer\\TestingArea\\test.out", "w", stdout);

	// freopen("B-large.in", "r", stdin);
	// freopen("B-large.out", "w", stdout);

    scanf("%d", &t);
    for(int z = 1; z <= t; ++z)
    {
    	cnt = 0;

    	scanf("%d%d", &n, &p);
    	for(int i = 0; i < n; ++i)
    		scanf("%d", &r[i]);
    	for(int i = 0; i < n; ++i)
		{
			id[i] = 0;
			for(int j = 0; j < p; ++j)
    		{
    			scanf("%d", &q[i][j]);
    			mxx = max(mxx, q[i][j] / r[i]);
    		}
    		sort(q[i], q[i] + p);
    	}

    	mxx = (mxx + 1) * 11 / 10;

    	for(int i = 1; i <= 1000000; ++i)
    	{
    		ok = 2e9;
    		for(int j = 0; j < n; ++j)
    		{
				mn = (LL)r[j] * i * 9 / 10;
				mx = (LL)r[j] * i * 11 / 10 + 1;

				idf[j] = p;
				ids[j] = -1;

				bsearch(0, p - 1, j, mn, 1);
				bsearch(0, p - 1, j, mx, 2);

				idf[j] = max(idf[j], id[j]);

    			ok = min(ok, ids[j] - idf[j] + 1);
    		}

    		if(ok > 0)
			{
				for(int j = 0; j < n; ++j)
    				id[j] = idf[j] + ok;

    			cnt += ok;
    		}
    	}
    	printf("Case #%d: %d\n", z, cnt);
    }
    return 0;
}