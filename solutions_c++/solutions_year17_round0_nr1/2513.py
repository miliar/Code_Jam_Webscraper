#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    long T, K;
    string S;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cin >> S >> K;
        long N = S.size();
        vector<long> a(N);
        for (long i = 0; i < N; i++) {
            a[i] = S[i] == '-';
        }

        long cnt = 0;
        long fail = 0;
        for (long i = 0; i < N; i++) {
            if (!a[i]) continue;
            if (i > N-K) {
                fail = 1;
                break;
            }
            cnt++;
            for (long j = i; j < i+K; j++) {
                a[j] ^= 1;
            }
        }

        cout << "Case #" << t << ": ";
        if (fail) cout << "IMPOSSIBLE" << endl;
        else cout << cnt << endl;;
    }
}
