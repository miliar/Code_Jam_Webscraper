#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <stdlib.h>
using namespace std;
int a[105];
int main() {
    int t, cas = 0;
    int n, m;
    scanf("%d", &t);
    while (t--) {
        cas++;
        scanf("%d%d",&n, &m);
        for (int i = 0; i < n; ++i) {
            scanf("%d", &a[i]);   
        }
        int ans = 0;
        if (m == 2) {
            int one = 0;
            int two = 0;
            for (int i = 0; i < n; ++i) {
                if (a[i] % 2 == 0) {
                    two++;
                } else {
                    one++;
                }
            }
            ans += two;
            ans += (one + 1) / 2;
        } else if (m == 3) {
            int one = 0;
            int two = 0;
            for (int i = 0; i < n; ++i) {
                if (a[i] % 3 == 0) {
                    ans++;
                } else if (a[i] %3 == 1) {
                    one++;
                } else {
                    two++;
                }
            }
            if (one < two) {
                int tmp = one;
                one = two;
                two = tmp;
            }
            ans += two;
            one -= two;
            ans += (one + 2) / 3;
        } else if (m == 4) {
            int one = 0;
            int two = 0;
            int th = 0;
            for (int i = 0; i < n; ++i) {
                if (a[i] % 4 == 0) {
                    ans++;
                } else if (a[i] % 4 == 1) {
                    one++;
                } else if (a[i] % 4 == 2) {
                    two++;
                } else if (a[i] % 4 == 3) {
                    th++;
                }
            }
            if (one < th) {
                int tmp = one;
                one = th;
                th = tmp;
            }
            ans += th;
            one -= th;
            two += one / 2;
            one %= 2;
            ans += two / 2;
            two %= 2;
            if (two != 0 || one != 0) {
                ans++;
            }
        }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
