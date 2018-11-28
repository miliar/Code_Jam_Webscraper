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

char str[] = "RYB";
int counts[3];

char res[10001];

int get_high(char prev) {
    int hi = -1;
    int pos = -1;
    for(int i = 0; i < 3; ++i) {
        // printf("pos = %d, char = %c, count = %d\n", i, str[i], counts[i]);
        if(prev != str[i] && hi < counts[i]) {
            // printf("pos = %d, value = %d\n", i, counts[i]);
            pos = i;
            hi = counts[i];
        }
    }
    return pos;
}

void solve() {
    int N, R, O, Y, G, B, V;
    scanf("%d %d %d %d %d %d %d", &N, &R, &O, &Y, &G, &B, &V);

    if(R > Y + B || Y > R + B || B > Y + R) {
        printf("IMPOSSIBLE\n");
        return;
    }

    if(R >= Y && R >= B) {
        str[0] = 'R';
        counts[0] = R;
        if(Y >= B) {
            str[1] = 'Y';
            counts[1] = Y;
            str[2] = 'B';
            counts[2] = B;
        } else {
            str[2] = 'Y';
            counts[2] = Y;
            str[1] = 'B';
            counts[1] = B;
        }
    } else if(Y >= R && Y >= B) {
        str[0] = 'Y';
        counts[0] = Y;
        if(R >= B) {
            str[1] = 'R';
            counts[1] = R;
            str[2] = 'B';
            counts[2] = B;
        } else {
            str[2] = 'R';
            counts[2] = R;
            str[1] = 'B';
            counts[1] = B;
        }
    } else if(B >= Y && B >= R) {
        str[0] = 'B';
        counts[0] = B;
        if(R >= Y) {
            str[1] = 'R';
            counts[1] = R;
            str[2] = 'Y';
            counts[2] = Y;
        } else {
            str[2] = 'R';
            counts[2] = R;
            str[1] = 'Y';
            counts[1] = Y;
        }
    }

    char prev = ' ';
    for(int i = 0; i < N; ++i) {
        int best = get_high(prev);
        // printf("best = %d\n", best);
        prev = str[best];
        printf("%c", prev);
        --counts[best];
    }
    printf("\n");
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
