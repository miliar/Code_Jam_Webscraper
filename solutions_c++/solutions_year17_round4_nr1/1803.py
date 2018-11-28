#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <utility>
#include <vector>
#include <queue>
#include <map>
#include <set>

using namespace std;

const int MAXN = 102;
int n, p;
int a[MAXN];
int freq[MAXN];

int solve() {
    memset(freq, 0, sizeof(freq));
    scanf("%d %d", &n, &p);
    for (int i = 0; i < n; ++i) {
        scanf("%d", a + i);
        ++freq[a[i] % p];
    }

    if (p == 2) {
        int odds = freq[1];
        return freq[0] + ((odds + 1) / 2);
    } else {
        int ans = freq[0];

        int small = min(freq[1], freq[2]);
        ans += small;
        // pair the 1s and 2s
        freq[1] -= small;
        freq[2] -= small;

        // handle the remainders
        for (int i = 1; i < 3; ++i) {
            ans += (freq[i] + 2) / 3;
        }

        return ans;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    int T;
    scanf("%d", &T);
    for (int case_num = 1; case_num <= T; ++case_num) {
        printf("Case #%d: %d\n", case_num, solve());
    }

    return 0;
}
