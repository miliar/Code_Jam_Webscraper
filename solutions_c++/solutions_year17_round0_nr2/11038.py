#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>

using namespace std;

const int maxn = 1000 + 10;

bool ok(int x)
{
    int k = 10;
    while (x > 0) {
        int xx = x % 10;
        if (xx > k) return 0;
        k = xx;
        x = x / 10;
    }
    return 1;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T, n;
    scanf("%d",&T);
    for (int t = 1; t <= T; t++) {
        scanf("%d",&n);
        int ret = 0;
        for (int i = 1; i <= n; i++) {
            if (ok(i)) ret = i;
        }
        printf("Case #%d: %d\n", t, ret);
    }
    return 0;
}
