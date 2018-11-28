#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
using namespace std;
#define MAXN 1003
int n, k;
struct Tcake {
    long long r, h;
    bool operator< (const Tcake &a)const
    {
        return r * h > a.r * a.h;
    }
} a[MAXN], b[MAXN];
long long f(int num)
{
    memcpy(b, a, sizeof(a));
    long long ans = a[num].r * a[num].r;
    long long t = a[num].r;
    swap(a[0], a[num]);
    sort(a + 1, a + n);
    int cnt = 0;
    for (int i = 0; i < n; ++i)
        if (t >= a[i].r) {
            ans += 2 * a[i].r * a[i].h;
            ++cnt;
            if (cnt == k)
                break;
        }
    memcpy(a, b, sizeof(a));
    return ans;
}
int main()
{
    int T;
    scanf("%d", &T);
    for (int Ti = 1; Ti <= T; ++Ti) {
        scanf("%d%d", &n, &k);
        for (int i = 0; i < n; ++i)
            cin >> a[i].r >> a[i].h;
        long long ans = 0;
        for (int i = 0; i < n; ++i)
            ans = max(ans, f(i));
        printf("Case #%d: %.10lf\n", Ti, M_PI * ans);
    }
    return 0;
}
