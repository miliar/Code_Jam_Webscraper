#include <bits/stdc++.h>

template<typename T> T gcd(T a, T b) {
    if(!b) return a;
    return gcd(b, a % b);
}
template<typename T> T lcm(T a, T b) {
    return a * b / gcd(a, b);
}

template<typename T> void chmin(T& a, T b) { a = (a > b) ? b : a; }
template<typename T> void chmax(T& a, T b) { a = (a < b) ? b : a; }
int in() { int x; scanf("%d", &x); return x; }

using namespace std;

typedef long long Int;
typedef unsigned long long uInt;
typedef unsigned uint;

const int INF = 0x3f3f3f3f;

int dp[20][(1 << 10) + 10];

int T, K, N, allones, aux;
string S;

int f(int pos, int mask) {
    if(pos == N) {
        if(mask != allones) return INF;
        return 0;
    }

    int& ans = dp[pos][mask];
    if(ans == -1) {
        int flip = mask;
        flip ^= (aux << (N - pos - 1));
        ans = min(f(pos + 1, flip) + 1, f(pos + 1, mask));
    }

    return ans;
}

int main(void) {

    cin >> T;
    for(int t=1; t<=T; t++) {
        cin >> S >> K;
        N = S.size();

        aux = 0;
        int aux2 = 1;
        for(int i=0; i<K; i++) {
            aux |= aux2;
            aux2 <<= 1;
        }

        allones = (1 << N) - 1;
        int mask = 0;
        for(int i=0; i<N; i++) {
            mask |= (1 << i)*(S[i] == '+');
        }

        memset(dp, -1, sizeof dp);
        int ans = f(K - 1, mask);
        cout << "Case #" << t << ": ";
        if(ans != INF)
            cout << ans << "\n";
        else
            cout << "IMPOSSIBLE\n";
    }

    return 0;
}
