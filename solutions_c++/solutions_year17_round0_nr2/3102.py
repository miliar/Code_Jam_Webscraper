#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <map>
#include <set>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

char str[32];

void solve() {
    long long N;
    scanf("%lld", &N);
    sprintf(str, "%lld", N);
    int l = strlen(str);

    if(N < 10) {
        printf("%lld\n", N);
        return;
    }

    int pos = -1;
    int prev = str[0];
    int i = 0;
    for(i = 0; i < l; ++i) {
        if(prev < str[i]) {
            pos = i;
            prev = str[i];
        }
        if(prev > str[i]) break;
    }
    if(i == l) {
        printf("%lld\n", N);
        return;
    }

    if(pos != -1) {
        str[pos] = str[pos] - 1;
        for(i = pos + 1; i < l; ++i)
            str[i] = '9';
        printf("%s\n", str);
        return;
    }

    if(str[0] == '1') {
        for(int i = 0; i < l - 1; ++i) str[i] = '9';
        str[l - 1] = '\0';
        printf("%s\n", str);
        return;
    }

    str[0] = str[0] - 1;
    for(i = 1; i < l; ++i)
        str[i] = '9';
    printf("%s\n", str);
}

int main() {
    int T;
    scanf("%d", &T);
    for(int test = 1; test <= T; ++test) {
        printf("Case #%d: ", test);
        solve();
    }

    return 0;
}
