#include <set>
#include <map>
#include <cmath>
#include <ctime>
#include <queue>
#include <string>
#include <cstdio>
#include <vector>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <algorithm>
using namespace std;
int Test;
long long N, M;
int hd, tl;
pair<long long, long long> Q[100000];

void insert(long long x, long long y)
{
    if (tl == 0 || x < Q[tl-1].first) {
        Q[tl ++] = make_pair(x, y);
    } else {
        for (int i = tl-1; i >= 0; i --)
        if (Q[i].first == x) {
            Q[i].second += y;
            return;
        }
    }
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	scanf("%d", &Test);
	for (int Case = 1; Case <= Test; Case ++) {
        scanf("%lld%lld", &N, &M);
        memset(Q, 0, sizeof(Q));
        hd = tl = 0;
        insert(N, 1);
        long long ret_x = -1, ret_y = -1;
        while (M > 0) {
            long long n = Q[hd].first;
            long long c = Q[hd].second;
            hd ++;
            M -= c;
            ret_x = n/2;
            ret_y = n-1-ret_x;
            insert(ret_x, c);
            insert(ret_y, c);
        }
        printf("Case #%d: %lld %lld\n", Case, ret_x, ret_y);
	}
	return 0;
}
