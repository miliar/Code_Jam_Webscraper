//#pragma warning (disable: 4786)
//#pragma comment (linker, "/STACK:16777216")
//HEAD
//include <bits/stdc++.h>
#include <cstdio>
#include <ctime>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <string>
#include <set>
#include <stack>
#include <map>
#include <cmath>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

typedef long long LL;

const int maxn = 10010;
LL t[2][80];
LL t_val[2][80];
LL get_pow(int cnt)
{
    if (cnt < 0) return 0;
    LL rt = 1;
    for (int i = 0; i < cnt; i++)
        rt *= 2;
    return rt;
}
LL get_min_val(LL x)
{
    if (!x) return 0;
    else return (x-1)/2;
}
LL get_val(LL n, int level)
{
    for (int i = 0; i < level; i++)
    {
        n = get_min_val(n);
    }
    return n;
}
void get_ans(LL final_n, LL &L, LL &R)
{
    LL x = final_n/2;
    if (final_n&1) x++;
    L = max(0LL, x-1);
    R = max(0LL, final_n - x);
}
int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int T;
    int ncase = 1;
    scanf("%d", &T);
    while (T--) {
        LL n, k;
        cin >> n >> k;
        memset(t, 0, sizeof(t));
        memset(t_val, 0, sizeof(t_val));
        t[n&1][0] = 1;
        t_val[n&1][0] = n;
        for (int i = 0; i < 70; i++) {
            for (int j = 0; j < 2; j++)
            if (t[j][i] > 0) {
                LL val = t_val[j][i];

                LL val_son = get_min_val(val);
                t[val_son&1][i+1] += t[j][i];
                t_val[val_son&1][i+1] = val_son;

                if (val%2==0) val_son++;
                t[val_son&1][i+1] += t[j][i];
                t_val[val_son&1][i+1] = val_son;
            }
        }
//        for (int i = 0; i < 10; i++) {
//            cout << t[0][i] << ' ' << t_val[0][i] << " * "<< t[1][i] << ' ' << t_val[1][i] <<endl;
//        }
        int k_level = 0;
        LL sum = 1;
        while (k > sum && sum >= 0) {
            k_level++;
            sum += get_pow(k_level);
        }
        sum -= get_pow(k_level);
        LL final_k, final_n1, final_n2;
        final_k = k - sum;
//        cout << k << ' ' << sum << endl;
        final_n1 = get_val(n, k_level);
        final_n2 = final_n1+1;
//        cout << k_level << ' ' << final_k << ' ' << final_n1<< ' ' << final_n2 << endl;

        LL final_n=final_n2;
        int x = final_n2%2;
        LL tmp_sum = t[x][k_level];
//        cout << tmp_sum << endl;
        if (tmp_sum < final_k) {
            final_n = final_n1;
        }
        LL L, R;
        get_ans(final_n, L, R);

//        cout << final_n << ' ' << L << ' ' << R << endl;
        printf("Case #%d: ", ncase++);
        cout << max(L, R) << ' ' << min(L, R) << endl;
    }
}

