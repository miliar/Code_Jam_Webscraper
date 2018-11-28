#include <algorithm>
#include <cstdio>
using namespace std;

char str[32];

int go(int i, int flag) {
    if (!str[i]) return flag;
    if (str[i] < str[i-1]) flag = 1;
    if (flag) str[i] = '9';
    int f = go(i+1, flag);
    if (flag) return flag;
    if (f) str[i]--;
    if (str[i] < str[i-1]) {
        str[i] = '9';
        return 1;
    }
    return flag;
}

int main() {
    int t, k;
    scanf("%d", &t);
    for (int tt = 1; tt <= t; tt++) {
        scanf("%s", str+1);
        go(1, 0);
        int i = 1;
        while (str[i] == '0') i++;
        printf("Case #%d: %s\n", tt, str+i);
    }
    return 0;
}
