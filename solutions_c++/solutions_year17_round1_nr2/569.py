#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <list>
#include <queue>
using namespace std;

int main() {
    long T, N, P;
    cin >> T;
    for (long t = 1; t <= T; t++) {
        cin >> N >> P;
        vector<long> R(N);
        for (long i = 0; i < N; i++) cin >> R[i];
        vector<vector<long>> Q(N, vector<long>(P));
        vector<list<long>> q(N);
        for (long i = 0; i < N; i++) {
            for (long j = 0; j < P; j++) cin >> Q[i][j];
            sort(Q[i].begin(), Q[i].end());
            q[i] = list<long>(Q[i].begin(), Q[i].end());
        }

        long cnt = 0;
        {
            long i = 0;
            while (i <= 1100000) {
                vector<long> r = vector<long>(R.begin(), R.end());
                for (long j = 0; j < N; j++) r[j] *= i;
                long stop = 0, cont = 0;
                for (long j = 0; j < N; j++) {
                    while (r[j] * 9 > 10 * q[j].front()) {
                        q[j].pop_front();
                        if (q[j].empty()) {
                            stop = 1;
                            break;
                        }
                    }
                    if (stop) break;
                    if (r[j] * 11 < 10 * q[j].front()) {
                        cont = 1;
                        break;
                    }
                }
                if (stop) break;
                else if (cont) {
                    i++;
                    continue;
                }
                cnt++;
                for (long j = 0; j < N; j++) {
                    q[j].pop_front();
                    if (q[j].empty()) stop = 1;
                }
                if (stop) break;
            }
        }

        cout << "Case #" << t << ": " << cnt << endl;
    }
}
