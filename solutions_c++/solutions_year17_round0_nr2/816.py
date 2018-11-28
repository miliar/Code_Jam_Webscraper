//#include <bits/stdc++.h>
#include <cstdio>
#include <ctime>
#include <cstdlib>
#include <cstring>
#include <string>
#include <queue>
#include <string>
#include <set>
#include <stack>
#include <map>
#include <cmath>
#include <vector>
#include <iostream>
#include <algorithm>
#include <bitset>
#include <fstream>
#include <sstream>

//INPUT
#define RI(n) scanf("%d", &n)
#define RII(n, m) scanf("%d%d", &n, &m)
#define RIII(n, m, k) scanf("%d%d%d", &n, &m, &k)
#define RIV(n, m, k, p) scanf("%d%d%d%d", &n, &m, &k, &p)
#define RV(n, m, k, p, q) scanf("%d%d%d%d%d", &n, &m, &k, &p, &q)
#define RS(s) scanf("%s", s)

//OUTPUT
#define WI(n) printf("%d\n", n)
#define WS(n) printf("%s\n", n)

//debug
//#define online_judge
#ifndef online_judge
#define dt(a)  << (#a) << "=" << a << " "
#define debugI(a) std::cout dt(a) << std::endl
#define debugII(a, b) std::cout dt(a) dt(b) << std::endl
#define debugIII(a, b, c) std::cout dt(a) dt(b) dt(c) << std::endl
#define debugIV(a, b, c, d) std::cout dt(a) dt(b) dt(c) dt(d) << std::endl
#define debugV(a, b, c, d, e) std::cout dt(a) dt(b) dt(c) dt(d) dt(e) << std::endl
#else
#define debugI(v)
#define debugII(a, b)
#define debugIII(a, b, c)
#define debugIV(a, b, c, d)
#define debugV(a, b, c, d, e)
#endif

const int INF = 2000000000;

using LL = long long;

std::vector<std::vector<int>> f;
std::vector<int> bits;
std::vector<int> ans;

int dfs(int pos, int pre, bool lmt, bool first)
{
    if (pos == -1) return 9;
    if (!lmt && !first && f[pos][pre] >= 0) return f[pos][pre];
    int u = lmt ? bits[pos] : 9;
    for (int i = u; i >= pre; i--) {
        if (dfs(pos - 1, i, lmt && i == u, first && !i) >= 0) {
            ans[pos] = i;
            return lmt || first ? i : f[pos][pre] = i;
        }
    }
    return lmt || first ? -1 : f[pos][pre] = -1;
}

int main()
{
    std::ifstream cin("B-large.in");
    std::ofstream cout("B-large.out");
    int n, k;
    std::string str;
    cin >> n;
    for (int kase = 1; kase <= n; kase++) {
        cin >> str;
        std::reverse(str.begin(), str.end());
        bits = std::vector<int>(str.length());
        ans = std::vector<int>(str.length());
        f = std::vector<std::vector<int>>(str.length() + 1, std::vector<int>(10, -1));
        for (int i = 0; i < str.length(); i++)
            bits[i] = str[i] - '0';
        LL ret = 0;
        dfs((int)str.length() - 1, 0, true, true);
        for (int i = (int)str.length() - 1; i >= 0; i--)
            ret = ret * 10 + ans[i];
        cout << "Case #" << kase << ": " << ret << std::endl;
    }
    return 0;
}
