#include <bits/stdc++.h>
using namespace std;

#define REP(i,n) for (int i = 0; i < n; i++)
#define RESET(c,v) memset(c, v, sizeof c)

typedef long long ll;

int T;
ll N, K;

int main() {
    cin >> T;
    REP(tc, T) {
        cin >> N >> K;

        map<ll, ll> stalls;
        stalls[-N] = 1;

        ll y, z;
        while (K > 0) {
            ll len, cnt;
            tie(len, cnt) = *stalls.begin();
            len *= -1;

            y = len/2;
            z = len-1-y;

            stalls[-y] += cnt;
            stalls[-z] += cnt;

            K -= cnt;
            stalls.erase(-len);
        }

        cout << "Case #" << (tc+1) << ": " << y << " " << z << endl;
    }
}
