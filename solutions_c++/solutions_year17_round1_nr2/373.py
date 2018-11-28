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

int ingr[100];
int tmp[100];
int le[100], ri[100];

void Solve()
{
    int i, j, k, n, m, tests;

    in_int1(tests);
    for (int test = 1; test <= tests; test++)
    {
        int p;
        in_int2(n, p);

        vector<pii> mas[55];
        for (i = 0; i < n; i++) in_int1(ingr[i]);
        for (i = 0; i < n; i++)
        {
            int mx = 0;
            for (j = 0; j < p; j++)
            {
                in_int1(tmp[j]);
                le[j] = 2000000000;
                ri[j] = 0;
                mx = max(mx, tmp[j]);
            }

            for (k = 1; k <= 1200000; k++)
            {
                ll price = 1ll * k * ingr[i];
                ll price90 = price * 9 / 10;
                if (price90 * 10 < price * 9) price90++;
                if (price90 > mx) break;

                ll price110 = price * 11 / 10;

                for (j = 0; j < p; j++)
                {
                    if (tmp[j] >= price90 && tmp[j] <= price110)
                    {
                        le[j] = min(le[j], k);
                        ri[j] = max(ri[j], k);
                    }
                }
            }

            for (j = 0; j < p; j++)
            {
                if (le[j] > 0) mas[i].push_back({ le[j], ri[j] });
            }

            sort(mas[i].begin(), mas[i].end());
        }

        vector<int> ind(n, 0);
        int ans = 0;
        while (true)
        {
            bool ok = true;
            int mx = 0;
            int mn = 2000000000;
            for (i = 0; i < n; i++)
            {
                if (ind[i] >= mas[i].size())
                {
                    ok = false;
                    break;
                }

                mx = max(mx, mas[i][ind[i]].first);
                mn = min(mn, mas[i][ind[i]].second);
            }

            if (!ok) break;

            if (mx <= mn)
            {
                ans++;
                for (i = 0; i < n; i++) ind[i]++;
            }
            else
            {
                for (i = 0; i < n; i++)
                {
                    if (mas[i][ind[i]].second < mx) ind[i]++;
                }
            }
        }

        fprintf(stderr, "Case #%d: %d\n", test, ans);
        printf("Case #%d: %d\n", test, ans);
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