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
#include <ctime>
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

char cake[25][25];
bool rowHas[25];

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

        memset(cake, 0, sizeof(cake));
        memset(rowHas, 0, sizeof(rowHas));

        RI(R); RI(C); RNL();

        for (int i = 0; i < R; i++)
        {
            bool seen = false;
            for (int j = 0; j < C; j++)
            {
                RC(v);
                if (v != '?') rowHas[i] = true;
                cake[i][j] = v;
            }
            RNL();
        }

        for (int i = 0; i < R; i++)
        {
            // skip empty rows for now
            if (!rowHas[i]) continue;

            int start = 0;
            int end = 0;
            char v = 0;
            while (end < C)
            {
                if (cake[i][end] == '?')
                {
                    end++;
                    continue;
                }

                v = cake[i][end];
                for (int j = start; j < end; j++)
                {
                    cake[i][j] = v;
                }
                end++;
                start = end;
            }
            if (start != end)
            {
                _ASSERT(v);
                for (int j = start; j < C; j++)
                {
                    cake[i][j] = v;
                }
            }
        }

        // search for empty rows now.  top to bottom
        for (int i = 0; i < R - 1; i++)
        {
            if (rowHas[i] && !rowHas[i + 1])
            {
                for (int j = 0; j < C; j++)
                {
                    cake[i + 1][j] = cake[i][j];
                }
                rowHas[i + 1] = true;
            }
        }

        // bottom to top
        for (int i = R - 1; i > 0; i--)
        {
            if (rowHas[i] && !rowHas[i - 1])
            {
                for (int j = 0; j < C; j++)
                {
                    cake[i - 1][j] = cake[i][j];
                }
                rowHas[i - 1] = true;
            }
        }

        DPF("\n");
        for (int i = 0; i < R; i++)
        {
            for (int j = 0; j < C; j++)
            {
                DPF("%c", cake[i][j]);
            }
            DPF("\n");
        }

    }
    fclose(inf);
    fclose(outf);
    return 0;
}