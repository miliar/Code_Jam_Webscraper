#include <functional>
#include <iostream>
#include <deque>
#include <set>
#include <cstring>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <map>
#include <cmath>
#include <string>

using namespace std;

#define ll long long

#if 1
#define pl(x...) printf(x)
#else
#define pl(x...)
#endif

ll N, P;
ll G[100];


int mem[101][101][101][4];

int solve(int m1, int m2, int m3, int cur) {
    int &ans = mem[m1][m2][m3][cur];
    if (ans != -1) return ans;

    if (m1 == 0 && m2 == 0 && m3 == 0) return ans = 0;

    ans = 0;
    if (m1 > 0) {
        ans = max(ans, solve(m1-1, m2, m3, (cur+P-1)%P));
    }
    if (m2 > 0) {
        ans = max(ans, solve(m1, m2-1, m3, (cur+P-2)%P));
    }
    if (m3 > 0) {
        ans = max(ans, solve(m1, m2, m3-1, (cur+P-3)%P));
    }


    if (cur == 0) ans++;
    return ans;
}

int main() {
    int T;
    cin>>T;
    for (int t = 1; t <= T; ++t) {
        memset(mem,-1,sizeof(mem));
        cin>>N>>P;
        for (int i=0;i<N;++i) {
            cin>>G[i];
        }

        ll ans = 0;

        if (P == 2) {
            int even = 0;
            for (int i=0;i<N;++i) {
                if (G[i] % 2 == 0) even++;
            }
            int m1 = N - even;

            ans = even + solve(m1, 0, 0, 0);
        } else if (P == 3) {
            int m0 = 0, m1=0, m2=0;
            for (int i=0;i<N;++i) {
                if (G[i] % 3 == 0) m0++;
                if (G[i] % 3 == 1) m1++;
                if (G[i] % 3 == 2) m2++;
            }

            ans = m0 + solve(m1, m2, 0, 0);

        } else if (P == 4) {
            int m0 = 0, m1=0, m2=0, m3=0;
            for (int i=0;i<N;++i) {
                if (G[i] % 4 == 0) m0++;
                if (G[i] % 4 == 1) m1++;
                if (G[i] % 4 == 2) m2++;
                if (G[i] % 4 == 3) m3++;
            }

            ans = m0 + solve(m1, m2, m3, 0);
        }


        printf("Case #%d: %lld\n", t, ans);
    }
}

