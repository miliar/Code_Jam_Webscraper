#include <cstdio>
#include <cstring>
#include <algorithm>
#include "io.h"

using std::max;
using std::min;


char s[20];
int m[20];
int ans[20];
int len;

bool find(int pos, bool maxed, int last) {
    if (pos >= len) {
        return true;
    }

    if (maxed) {
        if (m[pos] >= last) {
            if (find(pos+1, true, m[pos])) {
                ans[pos] = m[pos];
                return true;
            } else {
                for (int i = m[pos]-1; i >= last; --i) {
                    if (find(pos+1, false, i)) {
                        ans[pos] = i;
                        return true;
                    }
                }
                return false;
            }
        } else {
            return false;
        }
    } else {
        for (int i = 9; i >= last; --i) {
            if (find(pos+1, false, i)) {
                ans[pos] = i;
                return true;
            }
        }
        return false;
    }
}

int main() {
//    init_io("B-eg.in", "B-eg.out");
//    init_io("B-small-attempt0.in", "B-small-attempt0.out");
    init_io("B-large.in", "B-large.out");
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        memset(ans, 0, sizeof(ans));
        scanf("%s", s);
        len = (int)strlen(s);
        for (int i = 0; i < len; ++i) {
            m[i] = s[i]-'0';
        }
        find(0, true, 0);
        printf("Case #%d: ", t);
        int j;
        for (j = 0; j < len; j++) {
            if (ans[j] != 0) {
                break;
            }
        }
        for (; j < len; j++) {
            printf("%d", ans[j]);
        }
        puts("");
    }

    return 0;
}