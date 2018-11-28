#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <set>
#include <deque>
#include <map>
#include <algorithm>
#include <functional>
#include <ctime>
#include <queue>
using namespace std;
typedef unsigned long long ULL;
typedef long long LL;
#ifdef _DEBUG
#define DPF(fmt,...) { printf(fmt,##__VA_ARGS__); fprintf(outf, fmt,##__VA_ARGS__); }
#else
#define DPF(fmt,...) { fprintf(outf, fmt,##__VA_ARGS__); }
#endif
const int MAX_STR = 100000;
#define RI(val) int val = 0; scanf("%d", &val);
#define RIS(val, nn) vector<int> val; { for (int ii = 0; ii < (nn); ii++) { int vval; scanf("%d", &vval); val.push_back(vval); } }
#define RLL(val) LL val = 0; scanf("%lld", &val);
#define RLLS(val, nn) vector<LL> val; { for (int ii = 0; ii < (nn); ii++) { LL vval; scanf("%lld", &vval); val.push_back(vval); } }
#define RD(val) double val = 0.0f; scanf("%lf", &val);
#define RDS(val, nn) vector<double> val; { for (int ii = 0; ii < (nn); ii++) { double vval; scanf("%lf", &vval); val.push_back(vval); } }
#define RC(val) char val = 0; scanf("%c", &val);
#define RS(val) string val; {char str[MAX_STR]; scanf("%s", str); val = str;}
#define RL(val) string val; {char str[MAX_STR]; fgets(str, MAX_STR - 1, stdin); int len = strlen(str); if (str[len - 1] == '\n'){str[len - 1] = '\0';}else{str[len] = '\0';} val = str;}
#define RNL() {char str[MAX_STR]; fgets(str, MAX_STR, stdin);}
#define REP(ii, nn) for (int ii = 0; ii < (nn); ii++)
#define REPS(ii, mm, nn) for (int ii = (mm); ii < (nn); ii++)
#define swap(a, b) {auto t = a; a = b; b = t;}

map<LL, LL, greater<LL>> valmap;

int main()
{
    FILE* inf = freopen("in.txt", "r", stdin); FILE* outf = fopen("out.txt", "w");
    RI(np); RNL();
    for (int pp = 1; pp <= np; pp++)
    {
#ifndef _DEBUG
        printf("Case #%d\n", pp);
#endif
        DPF("Case #%d: ", pp);
        RLL(N); RLL(K);

        /*
        int val[2000] = {0};
        val[0] = 1;
        val[N + 1] = 1;
        LL val1, val2;

        for (int i = 0; i < K; i++)
        {
            int minLR = -1;
            int maxLR = -1;
            int stall;
            for (int j = 0; j < N + 2; j++)
            {
                // walk left to find Ls
                int Ls = 0;
                for (int k = j; k >= 0; k--)
                {
                    if (val[k]) break;
                    Ls++;
                }

                // walk right to find Rs
                int Rs = 0;
                for (int k = j; k < N + 2; k++)
                {
                    if (val[k]) break;
                    Rs++;
                }

                if (min(Ls, Rs) == minLR)
                {
                    if (max(Ls, Rs) > maxLR)
                    {
                        maxLR = max(Ls, Rs);
                        stall = j;
                    }
                }
                else if (min(Ls, Rs) > minLR)
                {
                    minLR = min(Ls, Rs);
                    maxLR = max(Ls, Rs);
                    stall = j;
                }
            }
            val[stall] = 1;
            if (i == K - 1)
            {
                val1 = maxLR - 1;
                val2 = minLR - 1;
            }
        }
        */
        
        valmap.clear();

        LL i = 0;

        LL val1, val2;

        i = 1;
        valmap[N] = 1;

        while (true)
        {
            LL val = valmap.begin()->first;
            LL count = valmap.begin()->second;
            if (val % 2 == 1)
            {
                val1 = val2 = val / 2;
            }
            else if (val == 0)
            {
                val1 = val2 = 0;
            }
            else
            {
                val1 = val / 2;
                val2 = val1 - 1;
            }
            if (i + count > K)
            {
                break;
            }

            i += count;
            if (valmap.find(val1) != valmap.end())
            {
                valmap[val1] += count;
            }
            else
            {
                valmap[val1] = count;
            }
            if (valmap.find(val2) != valmap.end())
            {
                valmap[val2] += count;
            }
            else
            {
                valmap[val2] = count;
            }
                
            valmap.erase(valmap.begin());
        }
        

        DPF("%lld %lld\n", val1, val2);

    }
    fclose(inf);
    fclose(outf);
    return 0;
}