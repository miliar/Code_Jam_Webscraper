#include <bits/stdc++.h>

using namespace std;

#define SZ(x) ((int)(x).size())
#define PB(x) push_back(x)
#define MEMSET(x,v) memset(x,v,sizeof(x))
#define REP(i,n) for(int (i)=0;(i)<(n);++(i))
#define x first
#define y second
#define INF (0x3f3f3f3f)

typedef long long LL;
typedef pair<int, int> P2;
template<class A, class B> inline bool mina(A &x, B y) {return (x > y)?(x=y,1):0;}
template<class A, class B> inline bool maxa(A &x, B y) {return (x < y)?(x=y,1):0;}

int in[4];
int N, P;
void solve() {
    MEMSET(in, 0);
    cin >> N >> P;
    int a;
    REP(i, N) {
        cin >> a;

        in[a % P]++;
    }
    int ans = in[0];
    if (P == 2) {
        int k = in[1] / 2;
        ans += k;
        in[1] -= 2 * k;
        ans += in[1];
    } else if (P == 3) {
        int k = min(in[1], in[2]);
        ans += k;
        in[1] -= k;
        in[2] -= k;
        if (in[1]) {
            int k = in[1] / 3;
            ans += k;
            in[1] -= 3 * k;
            if (in[1]) ans++;
        }
        if (in[2]) {
            int k = in[2] / 3;
            ans += k;
            in[2] -= 3 * k;
            if (in[2]) ans++;
        }
    } else {
        int k = min(in[1], in[3]);
        ans += k;
        in[1] -= k;
        in[3] -= k;
        k = in[2] / 2;
        ans += k;
        in[2] -= 2 * k;
        if (in[2] == 0) {
            if (in[1]) {
                int k = in[1] / 4;
                ans += k;
                in[1] -= 4 * k;
                if (in[1]) ans++;
            }
            if (in[3]) {
                int k = in[3] / 4;
                ans += k;
                in[3] -= 4 * k;
                if (in[3]) ans++;
            }
        } else {
            if (in[1]) {
                if (in[1] >= 2) {
                    ans += 1 + (in[1] - 2 + 3) / 4;
                } else {
                    ans++;
                }
            } else if (in[3]) {
                if (in[3] >= 2) {
                    ans += 1 + (in[3] - 2 + 3) / 4;
                } else {
                    ans++;
                }
            } else {
                ans++;
            }
        }
    }
    printf("%d\n", ans);
}

int main() {
    int test;
    cin >> test;
    REP(tt, test) {
        printf("Case #%d: ", tt + 1);
        solve();
    }

    return 0;
}
