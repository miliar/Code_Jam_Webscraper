#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <list>

using namespace std;

#define N 1005
char ss[N];
int k;

int opt(char ch) {
    return ch == '+' ? '-' : '+';
}

int main() {
    int test;
    scanf("%d", &test);
    for (int cas = 1; cas <= test; cas++) {
        scanf("%s%d", ss, &k);
        int res = 0;
        int n = strlen(ss);
        for (int i = 0; i <= n - k; i++) {
            if (ss[i] == '+') {
                continue;
            }
            else {
                for (int j = 0; j < k; j++) {
                    ss[i + j] = opt(ss[i + j]);
                }
                res++;
            }
        }

        bool ok = 1;
        for (int i = n - 1; i >= 0; i--) {
            if (ss[i] != '+') {
                ok = 0;
                break;
            }
        }

        printf("Case #%d: ", cas);
        if (ok)
            printf("%d\n", res);
        else
            puts("IMPOSSIBLE");
    }
    return 0;
}
