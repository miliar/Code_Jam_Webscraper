#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>
using namespace std;
typedef long long LL;
LL b[200];
int main() {
    int T;
    cin >> T;
    for (int cas = 1; cas <= T; cas++) {
        LL n;
        cin >> n;
        int wei = 0;
        memset(b, 0, sizeof(b));
        while (n) {
            b[wei++] = n % 10;
            n /= 10;
        }
        for (int i = 0; i < wei; ++i) {
            if (b[i] >= b[i + 1])
                continue;
            b[i + 1]--;
            for (int j = 0; j <= i; ++j) {
                b[j] = 9;
            }
        }
        printf("Case #%d: ",cas);
        while (b[wei - 1] == 0)
            wei--;
        for (int i = wei - 1; i >= 0; --i) {
            printf("%lld", b[i]);
        }
        printf("\n");
    }
    return 0;
}
