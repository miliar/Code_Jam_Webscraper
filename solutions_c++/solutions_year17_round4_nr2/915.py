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

int mas[2][1010];

void Solve()
{
    int i, j, k, n, m, tests;

    in_int1(tests);
    for (int test = 1; test <= tests; test++)
    {
        int c;
        in_int3(n, c, m);
        int ans = 0;
        mset(mas, 0);
        for (i = 0; i < m; i++)
        {
            int p, b;
            in_int2(p, b);
            p--;
            b--;
            mas[b][p]++;
        }

        for (i = 0; i < n; i++)
        {
            while (mas[0][i])
            {
                int best_candidate = 0;
                int best_count = -1;
                for (j = 0; j < n; j++)
                {
                    if (i == j || !mas[1][j]) continue;
                    if (best_count < mas[0][j] + mas[1][j])
                    {
                        best_count = mas[0][j] + mas[1][j];
                        best_candidate = j;
                    }
                }

                if (best_count == -1) break;
                mas[1][best_candidate]--;
                mas[0][i]--;
                ans++;
            }
        }

        int coll = 0;
        for (i = 0; i < n; i++)
        {
            if (!mas[0][i] && !mas[1][i]) continue;
                if (i == 0)
                {
                    ans += mas[0][i] + mas[1][i];
                }
                else
                {
                    ans += max(mas[0][i], mas[1][i]);
                    coll += min(mas[0][i], mas[1][i]);
                }
        }
/*
        // 2 customers case
        set<pii> s;
        for (auto it : mas[1])
        {
            s.insert({ it.second,it.first });
        }

        for (auto it : mas[0])
        {
            q.push({ it.second,it.first });
        }

        priority_queue<pii, vector<pii>, greater<pii>> q;
        for (auto it : mas[0])
        {
            q.push({ it.second,it.first });
        }

        int coll = 0;
        while (!q.empty() && mas[1].size() > 0)
        {
            int cnt = q.top().first;
            int pos = q.top().second;
            q.pop();
            int p = -1;
            for (auto it : mas[1])
            {
                if (it.first != pos)
                {
                    p = it.first;
                    break;
                }
            }

            if (p == -1) p = pos;
            bool skip = false;
            if (p == pos)
            {
                if (p > 0) coll++;
                else
                {
                    ans++;
                    skip = true;
                }
            }

            if (!skip && cnt > 1)
            {
                cnt--;
                q.push({ cnt, pos });
            }

            mas[1][p]--;
            if (mas[1][p] == 0) mas[1].erase(p);
        }
*/
        printf("Case #%d: %d %d", test, ans, coll);
		printf("\n");
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