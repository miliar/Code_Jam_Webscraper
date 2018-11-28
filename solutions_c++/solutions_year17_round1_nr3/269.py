#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cctype>
#include <cstdio>
#include <vector>
#include <cassert>
#include <complex>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
#define int long long

const int inf = 1e3;

int go(int H_d, int A_d, int H_k, int A_k, int B, int D)
{
    int ret = inf;
    for (int numD = 0; numD <= 100; numD++)
        for (int numB = 0; numB <= 100; numB++)
        {
            int cur = 0;
            int hd = H_d, ad = A_d, hk = H_k, ak = A_k;
            for (int i = 0; i < numD; i++)
            {
                if (hd - (ak - D) <= 0)
                {
                    hd = H_d - ak;
                    if (hd <= 0)
                    {
                        cur = inf;
                        break;
                    }
                    cur++;
                }
                ak -= D;
                if (ak < 0) ak = 0;
                hd -= ak;
                cur++;
                if (hd <= 0)
                {
                    cur = inf;
                    break;
                }
            }
            if (cur == inf)
                continue;
            for (int i = 0; i < numB; i++)
            {
                if (hd - ak <= 0)
                {
                    hd = H_d - ak;
                    if (hd <= 0)
                    {
                        cur = inf;
                        break;
                    }
                    cur++;
                }
                ad += B;
                hd -= ak;
                cur++;
                if (hd <= 0)
                {
                    cur = inf;
                    break;
                }
            }
            if (cur == inf)
                break;
            while (hk > 0)
            {
                if (cur >= inf)
                {
                    cur = inf;
                    break;
                }
                hk -= ad;
                if (hk <= 0)
                {
                    cur++;
                    break;
                }
                if (hd - ak <= 0)
                {
                    hd = H_d - ak;
                    if (hd <= 0)
                    {
                        cur = inf;
                        break;
                    }
                    cur++;
                }
                hd -= ak;
                cur++;
                if (hd <= 0)
                {
                    cur = inf;
                    break;
                }
            }
            if (cur == inf)
                continue;
            ret = min(ret, cur);
        }
    return ret;
}

#undef int
int main()
{
#define int long long
    int t; cin >> t;
    for (int tt = 1; tt <= t; tt++)
    {
        cerr << "Executing Case #" << tt << "\n";
        int H_d, A_d, H_k, A_k, B, D;
        cin >> H_d >> A_d >> H_k >> A_k >> B >> D;
        int opt = go(H_d, A_d, H_k, A_k, B, D);
        cout << "Case #" << tt << ": ";
        if (opt == inf) cout << "IMPOSSIBLE\n";
        else cout << opt << "\n";
    }
    return 0;
}
