#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define in_str(b) scanf("%s",(b))
#define in_int1(a) scanf("%d",&(a))
#define in_int2(a,b) scanf("%d%d",&(a),&(b))
#define in_int3(a,b,c) scanf("%d%d%d",&(a),&(b),&(c))
#define in_int4(a,b,c,d) scanf("%d%d%d%d",&(a),&(b),&(c),&(d))
#define so(a) sort((a).begin(), (a).end())
#define rso(a) sort((a).rbegin(), (a).rend())
#define mp(a,b) make_pair(a,b)
#define mset(a,n) memset(a,n,sizeof(a))
#define readints(mas,n) for (int _i=0;_i<(n);_i++) in_int1((mas)[_i])
#define readdoubles(mas,n) for (int _i=0;_i<(n);_i++) scanf("%lf", &(mas)[_i])
#define unq(src) src.erase(unique((src).begin(), (src).end()), (src).end())
#define MOD 1000000007
typedef pair<int, int> pii;
typedef long long ll;
typedef pair<ll, ll> pll;

int mas[110];
int P;
char dp[4][101][101][101][101];

char go(int r, int p0, int p1, int p2, int p3)
{
    if (p0 + p1 + p2 + p3 == 0) return 0;
    char& res = dp[r][p0][p1][p2][p3];
    if (res == -1)
    {
        int add = r == 0 ? 1 : 0;
        res = 0;
        char ret;
        if (p0)
        {
            ret = go(r, p0 - 1, p1, p2, p3);
            res = max(res, ret);
        }

        if (p1)
        {
            ret = go((r - 1 + P)%P, p0, p1-1, p2, p3);
            res = max(res, ret);
        }

        if (p2)
        {
            ret = go((r - 2 + P) % P, p0, p1, p2 - 1, p3);
            res = max(res, ret);
        }

        if (p3)
        {
            ret = go((r - 3 + P) % P, p0, p1, p2, p3-1);
            res = max(res, ret);
        }

        res += add;
    }

    return res;
}

void Solve()
{
    int i, j, k, n, m, tests;

    in_int1(tests);
    for (int test = 1;test<=tests;test++)
    {
        in_int2(n, P);
        int r[4] = { 0 };
        for (i = 0; i < n; i++)
        {
            int a;
            in_int1(a);
            r[a%P]++;
        }
        mset(dp, -1);
        printf("Case #%d: %d\n", test, (int)go(0,r[0],r[1],r[2],r[3]));
	}
}

int main()
{
#ifdef __LOCAL_RUN__
#define _MAX_BUF_SIZE 32
    int _i = 0;
    char *_buf = new char[_MAX_BUF_SIZE];

    FILE *res_output = freopen("output.txt", "wt", stdout);
    while (true)
    {
        string _suffix = string(itoa(_i, _buf, 10)) + string(".txt");
        FILE *res_input = freopen((string("input-") + _suffix).c_str(), "rt", stdin);
        if (!res_input)
        {
            // the end
            break;
        }
        if (_i) printf("\n\n");
        printf("==== Case #%d =====\n", _i);
        Solve();
        _i++;
    }
#else
    Solve();
#endif
    return 0;
}