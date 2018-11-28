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

#define online
#ifdef online
#define in fin
#define out fout
#else
#define in std::cin
#define out std::cout
#endif

int main()
{
    std::ifstream fin("C-large.in");
    std::ofstream fout("C-large.out");
    int T;
    in >> T;
    for (int kase = 1; kase <= T; kase++) {
        LL n, k;
        in >> n >> k;
        while (k != 1) {
            n--; k--;
            n = n / 2 + n % 2 * k % 2;
            k = k / 2 + k % 2;
        }
        out << "Case #" << kase << ": " << n - 1 - (n - 1) / 2 << ' ' << (n - 1) / 2 << std::endl;
    }
    return 0;
}
