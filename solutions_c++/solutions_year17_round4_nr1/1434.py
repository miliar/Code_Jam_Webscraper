#include <iostream>
#include <vector>
#include <map>
using namespace std;

int main() {
    long T, N, P;
    cin >> T;
    for (long t = 1; t <= T; t++) {
        cin >> N >> P;
        vector<long> G(N);
        for (long i = 0; i < N; i++) cin >> G[i];

        map<long, long> cnts;
        for (long i = 0; i < N; i++) cnts[G[i] % P]++;

        long ans = 999999999;
        if (P == 2) {
            ans = 1 + cnts[0];
            while (cnts[1] >= 2) cnts[1] -= 2, ans++;
            ans -= (cnts[1] == 0);
        } else if (P == 3) {
            ans = 1 + cnts[0];
            while (cnts[1] && cnts[2]) cnts[1]--, cnts[2]--, ans++;
            while (cnts[1] >= 3) cnts[1] -= 3, ans++;
            while (cnts[2] >= 3) cnts[2] -= 3, ans++;
            ans -= (cnts[1] + cnts[2] == 0);
        } else if (P == 4) {
            ans = 1 + cnts[0];
            while (cnts[2] >= 2) cnts[2] -= 2, ans++;
            while (cnts[1] && cnts[3]) cnts[1]--, cnts[3]--, ans++;

            while (cnts[1] >= 2 && cnts[2]) cnts[1] -= 2, cnts[2]--, ans++;
            while (cnts[3] >= 2 && cnts[2]) cnts[3] -= 2, cnts[2]--, ans++;

            while (cnts[1] >= 4) cnts[1] -= 4, ans++;
            while (cnts[3] >= 4) cnts[3] -= 4, ans++;

            ans -= (cnts[1] + cnts[2] + cnts[3] == 0);
        }

        cout << "Case #" << t << ": " << ans << endl;
    }
}
