#include <iostream>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
#include <queue>
#include <vector>
#include <climits>
using namespace std;
typedef int64_t ll;

int t, k;
char s[1005];

int main() {
    scanf("%d", &t);
    for (int m = 1; m <= t; m++) {
        scanf("%s%d", s, &k);
        int l = (int) strlen(s);
        int cnt = 0;
        for (int i = 0; i <= l - k; i++)
            if (s[i] == '-') {
                cnt++;
                for (int j = 0; j < k; j++)
                    s[i + j] == '-' ? s[i + j] = '+' : s[i + j] = '-';
            }
        bool res = true;
        for (int i = l - k + 1; i < l; i++)
            if (s[i] == '-') {
                res = false;
                break;
            }
        printf("Case #%d: ", m);
        res ? printf("%d\n", cnt) : printf("IMPOSSIBLE\n");
    }
    return 0;
}