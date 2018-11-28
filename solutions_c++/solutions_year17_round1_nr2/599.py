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

#define pii pair<int, int>

bool cmpp(pii& a, pii& b)
{
    if (a.first == b.first) return a.second < b.second;
    return a.first < b.first;
}

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

        RI(N); RI(P);
        
        vector<int> ingredients;
        vector<deque<pii>> amounts;

        for (int i = 0; i < N; i++)
        {
            RI(val);
            ingredients.push_back(val);
        }

        for (int i = 0; i < N; i++)
        {
            deque<pii> vec;
            int ival = ingredients[i];
            for (int j = 0; j < P; j++)
            {
                RI(val);
                
                int servings = val / ival;
                int low = (int)(0.8f * servings);
                low = max(1, low);
                int high = (int(2.0f * servings) + 1);

                // test servings;
                int start = -1;
                int end = -1;
                for (int s = low; s <= high; s++)
                {
                    int serv = s * ival;
                    int servmin = serv * 0.9f;
                    int servmax = serv * 1.1f;
                    if (val >= servmin && val <= servmax)
                    {
                        if (start == -1)
                        {
                            start = s;
                        }
                    }
                    else
                    {
                        if (start != -1)
                        {
                            end = s - 1;
                            break;
                        }
                    }
                }
                if (start != -1 && end == -1)
                {
                    end = high;
                }
                if (end != -1)
                {
                    pii v = {start, end};
                    vec.push_back(v);
                }
            }
            amounts.push_back(vec);
        }
        
        int count = 0;

        for (int i = 0; i < N; i++)
        {
            sort(amounts[i].begin(), amounts[i].end(), cmpp);
        }

        while (true)
        {
            bool potential = true;
            int minn = 10000000;
            int smallindex = -1;
            for (int i = 0; i < N; i++)
            {
                if (!amounts[i].size())
                {
                    potential = false;
                    break;
                }
                if (amounts[i][0].first < minn)
                {
                    minn = amounts[i][0].first;
                    smallindex = i;
                }
            }
            if (!potential) break;

            bool found = true;
            pii small = amounts[smallindex][0];
            for (int i = small.first; i <= small.second; i++)
            {
                found = true;
                for (int j = 0; j < N; j++)
                {
                    if (j == smallindex) continue;
                    // break out if we had a bad one.
                    if (i < amounts[j][0].first ||
                        i > amounts[j][0].second)
                    {
                        found = false;
                        break;
                    }
                }
                if (found) break;
            }
            if (found)
            {
                for (int i = 0; i < N; i++)
                {
                    amounts[i].pop_front();
                }
                count++;
            }
            else
            {
                amounts[smallindex].pop_front();
            }
        }

        DPF("%d\n", count);

    }
    fclose(inf);
    fclose(outf);
    return 0;
}