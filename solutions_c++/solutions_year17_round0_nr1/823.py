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

int main()
{
    std::ifstream fin("A-large.in");
    std::ofstream fout("A-large.out");
    int n, k;
    std::string str;
    fin >> n;
    for (int kase = 1; kase <= n; kase++) {
        std::queue<int> q;
        fin >> str >> k;
        int ans = 0;
        for (int i = 0; i < str.length(); i++) {
            while (!q.empty() && q.front() < i)
                q.pop();
            if ((q.size() % 2 == 1 && str[i] == '+') || (q.size() % 2 == 0 && str[i] == '-')) {
                if (i + k - 1 >= (int)str.size()) {
                    ans = -1;
                    break;
                }
                ans++;
                q.push(i + k - 1);
            }
        }
        fout << "Case #" << kase << ": ";
        if (ans == -1)
            fout << "IMPOSSIBLE" << std::endl;
        else
            fout << ans << std::endl;
    }
    return 0;
}
