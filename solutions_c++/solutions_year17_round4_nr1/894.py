#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cassert>
#include <sstream>
#include <functional>
#include <algorithm>
#include <map>
#include <string>
#include <vector>
#include <set>
#include <queue>

using namespace std;

int nt;

int cnt[10];

int main()
{
	int nt;
	scanf("%d", &nt);
	for(int tt = 1; tt <= nt; tt++)
	{
		fprintf(stderr, "test = %d\n", tt);
		printf("Case #%d: ", tt);

		int N, P, a;
		scanf("%d %d", &N, &P);
        memset(cnt, 0, sizeof cnt);
        int res = 0;
        for(int i = 0; i < N; i++) { scanf("%d", &a); cnt[a % P]++; }

        res += cnt[0];
        if (P == 2)
        {
            res += (cnt[1] + 1) / 2;
        }
        else
        if (P == 3)
        {
            int k = min(cnt[1], cnt[2]);
            res += k;
            cnt[1] -= k;
            cnt[2] -= k;
            k = cnt[1] + cnt[2];
            res += (k + 2) / 3;
        }
        else // P == 4
        {
            res += cnt[2] / 2;
            cnt[2] %= 2;

            int k = min(cnt[1], cnt[3]);
            res += k;
            cnt[1] -= k;
            cnt[3] -= k;
            k = cnt[1] + cnt[3];
            if (cnt[2])
            {
                res++;
                k -= 2;
            }
            if (k > 0)
            {
                res += (k + 3) / 4;
            }
        }

        printf("%d\n", res);
	}
	return 0;
}
