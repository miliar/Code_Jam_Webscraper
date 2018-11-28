#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <limits>

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;
typedef vector<LL> VLL;
typedef vector<VLL> VVLL;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

int divide[5];
int a[220];

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int tt;
    int n, p;
    scanf("%d", &tt);
    for (int t=0 ; t<tt; t++) {
        for (int i=0 ; i<5 ; i++) {
            divide[i] = 0;
        }

        scanf("%d%d", &n, &p);
        for (int i=0 ; i<n ; i++) {
            scanf("%d", &a[i]);
            a[i] %= p;
            divide[a[i]]++;
        }

        int ans = 0;
        if (p==2) {
            ans = divide[0] + divide[1]/2 + (divide[1]%2);
        }
        else if (p==3) {
            int tmp = min(divide[1], divide[2]);
            divide[1] -= tmp;
            divide[2] -= tmp;
            ans = divide[0] + tmp + divide[1]/3 + divide[2]/3;
            if (divide[1] % 3 > 0) {
                ans += 1;
            }
            if (divide[2] % 3 > 0) {
                ans += 1;
            }
        }
        else if (p==4) {
            ans = divide[0] + divide[2]/2;
            divide[2] = divide[2] % 2;

            int tmp = min(divide[1], divide[3]);
            divide[1] -= tmp;
            divide[3] -= tmp;
            ans += tmp;

            if (divide[1] > 0) {    // 1
                if (divide[1] >= 2 && divide[2] > 0) {
                    divide[1] -= 2;
                    divide[2]--;
                    ans += 1;
                }
                ans += divide[1] / 4;
                divide[1] %= 4;
            }
            else if (divide[3] > 0) {      // 3
                if (divide[3] >= 2 && divide[2] > 0) {
                    divide[3] -= 2;
                    divide[2]--;
                    ans += 1;
                }
                ans += divide[3] / 4;
                divide[3] %= 4;
            }

            if (divide[1] > 0 || divide[2] > 0 || divide[3] > 0) {
                ans += 1;
            }
        }

        printf("Case #%d: %d\n", t+1, ans);
    }
}
