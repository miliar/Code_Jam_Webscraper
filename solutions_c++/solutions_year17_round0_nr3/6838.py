#include<stdio.h>
#include<string.h>
#include<math.h>
#include <algorithm>

bool stalls[1002];
void resolv(int n, int k, int &MAX_LR, int &MIN_LR) {
    memset(stalls, 0x00, sizeof(stalls));
    stalls[0] = stalls[n+1] = true;
    int last_min = 0;
    int last_max = n;
    int index = 0;
    for (int i = 0; i < k; ++i) {
        bool first_case = true;
        for (int j = 1; j < n+1; ++j) {
            bool ready_l = false, ready_r = false;
            int ls = 0, rs = 0;
            if (stalls[j])
                continue;
            for(int fields = 1; !ready_l || !ready_r; ++fields) {
                if (!ready_l && stalls[j - fields]) {
                    ls = fields - 1;
                    ready_l = true;
                }
                if (!ready_r && stalls[j + fields]) {
                    rs = fields - 1;
                    ready_r = true;
                }
            }
            int new_min = std::min(ls, rs);
            int new_max = std::max(ls, rs);
            if (first_case || new_min > last_min || new_min == last_min && new_max > last_max) {
                index = j;
                last_min = new_min;
                last_max = new_max;
                first_case = false;
            }
        }
        stalls[index] = true;
    }
    MAX_LR = last_max;
    MIN_LR = last_min;
}

int main() {
    int N, K, RMIN, RMAX;
    int T;
    freopen("output.txt", "w", stdout);
    freopen("input.txt", "r", stdin);
    scanf("%d", &T);
    for(int i = 0; i < T;++i) {
        scanf("%d %d", &N, &K);
        resolv(N, K, RMAX, RMIN);
        printf("Case #%d: %d %d\n", i+1, RMAX, RMIN);
    }

    return 0;
}