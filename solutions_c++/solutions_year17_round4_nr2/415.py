#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <stdlib.h>
using namespace std;

int person[1005];
int pos[1005];
int main() {
    int t, cas = 0;
    int n, m, c;
    scanf("%d", &t);
    while (t--) {
        cas++;
        scanf("%d %d %d", &n, &c, &m);
        memset(person, 0, sizeof(person));
        memset(pos, 0, sizeof(pos));
        while (m--) {
            int x, y;
            scanf("%d%d", &x, &y);
            person[y]++;
            pos[x]++;
        }
        int ans = 0;
        int sum = 0;
        for (int i = 1; i <= n; ++i) {
            sum += pos[i];
            if (ans < (sum + i - 1) / i) {
                ans = (sum + i - 1) / i;
            }
        }
        for (int i = 1; i <= c; ++i) {
            if (ans < person[i]) {
                ans = person[i];
            }
        }
        int ansb = 0;
        for (int i = 1; i <= n; ++i) {
            if (pos[i] > ans) {
                ansb += pos[i] - ans;
            }
        }
        printf("Case #%d: %d %d\n", cas, ans, ansb);
    }
    return 0;
}
