#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <string>
#include <queue>
#include <sstream>
#include <cmath>
#include <random>
#include <cstring>
using namespace std;

#define CLR(a,b) memset(a,b,sizeof(a))
const int N = 1000+5;
char face[N];
int fliped[N];
int n;
int k;

int solve()
{
    CLR(fliped, 0);
    int cur_fliped = 0;
    int ans = 0;
    for (int i = 0; i < n; ++i) {
        int status = (face[i] == '+') ? 1 : 0;
        status ^= cur_fliped;
        if (status == 0) {
            cur_fliped ^= 1;
            int flip_end = i + k - 1;
            if (flip_end >= n) return -1;
            fliped[flip_end] ^= 1;
            ans ++;
        }
        cur_fliped ^= fliped[i];
    }
    return ans;
}

int main() {
    int cas = 0;
    freopen("/Users/lizhen/Documents/Project/Cpp/cpp/cpp/input.txt", "r", stdin);
    freopen("/Users/lizhen/Documents/Project/Cpp/cpp/cpp/output.txt", "w", stdout);
    int T;
    cin >> T;
    while (T--) {
        cas ++;
        printf("Case #%d: ", cas);
        cin >> face;
        cin >> k;
        n = strlen(face);
        int ans = solve();
        if (ans == -1) {
            puts("IMPOSSIBLE");
        } else {
            printf("%d\n", ans);
        }
    }
    return 0;
}
