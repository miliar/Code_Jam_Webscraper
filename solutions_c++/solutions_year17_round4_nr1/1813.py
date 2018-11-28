#include <iostream>
using namespace std;
int main()
{
    int T, N, P;
    int a[100], ans;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cin >> N >> P;
        for (int i = 0; i < N; i++) {
            cin >> a[i];
            a[i] %= P;
        }
        int c[4] = {0};
        for (int i = 0; i < N; i++)
            c[a[i]]++;
        ans = c[0];
        if (P == 2) ans += (c[1]+1)/2;
        if (P == 3) {
            if (c[1] > c[2]) ans += c[2] + (c[1]-c[2]+2)/3;
            else ans += c[1] + (c[2]-c[1]+2)/3;
        }
        if (P == 4) {
            if (c[1] > c[3]) {ans += c[3]; c[1] -= c[3]; c[3] = 0;}
            else {ans += c[1]; c[3] -= c[1]; c[1] = 0;}
            ans += (c[2]+1)/2;
            c[2] %= 2;
            if (c[2] == 1) {
                ans++;
                int tmp = c[1] > 0 ? c[1] : c[3];
                if (tmp > 2) ans += (tmp+1)/4;
            }
            else {
                int tmp = c[1] > 0 ? c[1] : c[3];
                ans += (tmp+3)/4;
            }
        }
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
