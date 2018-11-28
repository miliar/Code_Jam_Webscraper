#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <cmath>

using namespace std;

const int maxL = 20 + 5;

int T, l;
int a[maxL];

char s[maxL];

int main() {
    //freopen("2.in", "r", stdin);
    //freopen("2.txt", "w", stdout);
    scanf("%d", &T);
    for (int testCase = 1; testCase <= T; ++testCase) {
        scanf("%s", s);
        l = strlen(s);
        for (int i = 1; i <= l; ++i)
            a[i] = s[i - 1] - '0';
        bool flag = true;
        while (flag) {
            flag = false;
            for (int i = 1; i < l; ++i) {
                if (a[i] <= a[i + 1]) continue;
                --a[i];
                flag = true;
                for (int j = i + 1; j <= l; ++j)
                    a[j] = 9;
                break;
            }
        }
        printf("Case #%d: ", testCase);
        for (int i = 1; i <= l; ++i) {
            if (a[i] == 0) continue;
            printf("%d", a[i]);
        }
        printf("\n");
    }
    return 0;
}
