/*************************************************************************
	> File Name: Round1B_B.cpp
	> Author: BMan
	> Mail: luo-kai-jia@163.com
	> Created Time: Sun 23 Apr 2017 01:01:26 AM CST
 ************************************************************************/

#include <bits/stdc++.h>
using namespace std;

enum {
    R = 0x1,
    Y = 0x2,
    B = 0x4,
    O = R | Y,
    G = Y | B,
    V = R | B
};

char GetName(int value) {
    if (value == R) return 'R';
    if (value == Y) return 'Y';
    if (value == B) return 'B';
    if (value == O) return 'O';
    if (value == G) return 'G';
    if (value == V) return 'V';
    return 'X';
}

int GetValue(char name) {
    if (name == 'R') return R;
    if (name == 'Y') return Y;
    if (name == 'B') return B;
    if (name == 'O') return O;
    if (name == 'G') return G;
    if (name == 'V') return V;
    return 0;
}

int n;
int cnt[7];

int main() {
    int _T;
    scanf("%d", &_T);
    for (int _t = 1; _t <= _T; _t++) {
        scanf("%d", &n);
        scanf("%d %d %d %d %d %d",
                &cnt[1], &cnt[3], &cnt[2], &cnt[6], &cnt[4], &cnt[5]);
        if (cnt[1] > cnt[2] +  cnt[4] ||
                cnt[2] > cnt[1] + cnt[4] ||
                cnt[4] > cnt[1] + cnt[2]) {
            printf("Case #%d: IMPOSSIBLE\n", _t);
        } else {
            printf("Case #%d: ", _t);
            int first = 0;
            int last = 0;
            for (int i = 0; i < n; i++) {
                int cur, cur_max = 0;
                for (int i = 1; i <= 6; i++) {
                    if (i != last) {
                        if (cnt[i] > cur_max || (cnt[i] == cur_max && i == first)) {
                            cur = i;
                            cur_max = cnt[i];
                        }
                    }
                }
                if (i == 0) first = cur;
                printf("%c", GetName(cur));
                last = cur;
                cnt[cur]--;
            }

            printf("\n");
        }
        
    }
    return 0;
    
}
