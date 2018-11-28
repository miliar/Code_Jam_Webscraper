#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

const int MAXC = 1000, MAXN = 10000;
// int ar[MAXN][MAXC],
int cnt[MAXC], sum[MAXN];

void ans(int tn, int a, int b)
{
    cout << "Case #" << tn << ": " << a << ' ' << b << endl;
}

int prom;
bool can(int b)
{
    prom = 0;
    int lost = 0;
    for (int q = 0; q < MAXN; ++q)
    {
        if (sum[q] > b)
        {
            if (lost >= sum[q] - b)
            {
                lost -= sum[q] - b;
                prom += sum[q] - b;
            }
            else
                return false;
        }
        else
        {
            lost += b - sum[q];
        }
    }
    
    return true;
}

void solve(int test_number)
{
    int n, c, m;
    cin >> n >> c >> m;
    
    memset(cnt, 0, sizeof(cnt));
    memset(sum, 0, sizeof(sum));
    for (int q = 0; q < m; ++q)
    {
        int a, b;
        cin >> a >> b;
        --a; --b;
//        ++ar[a][b];
        ++cnt[b];
        ++sum[a];
    }
    
    int mm = 0;
    for (int q = 0; q < MAXC; ++q)
        mm = max(mm, cnt[q]);
    int ss = 0;
    for (int q = 0; q < MAXN; ++q)
        ss = max(ss, sum[q]);
    
    if (ss < mm)
    {
        ans(test_number, mm, 0);
        return;
    }
    int L = mm - 1, R = ss;
    while (R - L > 1)
    {
        int middle = (L + R) / 2;
        if (can(middle))
            R = middle;
        else
            L = middle;
    }
    can(R);
    ans(test_number, R, prom);
}

int main()
{
  /*
    freopen("tmp", "r", stdin);
//  */ freopen("btest.in", "r", stdin); freopen("btest.out", "w", stdout);
    
    int cnt_tests;
    cin >> cnt_tests;
    for (int q = 0; q < cnt_tests; ++q)
    {
        solve(q + 1);
    }
    
    return 0;
}
