#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <ctime>
#include <string>
#include <cstring>
#include <complex>
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
#define mp make_pair

const int N = 1010;
int n, m, k;
int a[N], b[N];

void solve()
{
    for (int i = 0; i < N; i++)
        a[i] = b[i] = 0;
    scanf("%d%d%d", &n, &m, &k);
    for (int i = 0; i < k; i++)
    {
        int x, y;
        scanf("%d%d", &x, &y);
        a[y - 1]++;
        b[x]++;
    }
    k = 0;
    for (int i = 0; i < m; i++)
        k = max(k, a[i]);
    int sum = 0;
    for (int i = 1; i <= n; i++)
    {
        sum += b[i];
        k = max(k, (sum + i - 1) / i);
    }
    m = 0;
    int cur = 0;
    for (int i = n; i > 0; i--)
    {
        int cnt = b[i];
        cnt -= k;
        if (cnt > 0) m += cnt;
        cur += cnt;
        cur = max(cur, 0);
    }
    printf("%d %d\n", k, m);
    return;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++)
    {
        printf("Case #%d: ", i);
        solve();
    }


    return 0;
}
