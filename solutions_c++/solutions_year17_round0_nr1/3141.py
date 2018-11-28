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

char str[1010];

void solve() {
    scanf("%s", str);
    int l = strlen(str);
    int K;
    scanf("%d", &K);
    int moves = 0;
    for(int i = 0; i + K <= l; ++i) {
        if(str[i] == '-') {
            ++moves;
            for(int j = i; j < i + K; ++j) {
                if(str[j] == '-')
                    str[j] = '+';
                else
                    str[j] = '-';
            }
        }
    }

    int good = 1;
    for(int i = 0; i < l; ++i) {
        if(str[i] == '-')
            good = 0;
    }
    if(good == 0) {
        printf("IMPOSSIBLE\n");
    } else {
        printf("%d\n", moves);
    }
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
