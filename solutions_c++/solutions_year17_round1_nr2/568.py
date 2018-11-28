#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;
int T, N, P, ans, _max, _min;
int R[51];
int Q[51][51];
int lo[51], hi[51], cur[51], ind[51];
bool flag;
int main()
{
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cin >> N >> P;
        for (int i = 0; i < N; i++) cin >> R[i];
        for (int i = 0; i < N; i++)
            for (int j = 0; j < P; j++)
                cin >> Q[i][j];
        for (int i = 0; i < N; i++) {
            sort(Q[i], Q[i]+P);
            lo[i] = ceil(double(R[i])*0.9);
            hi[i] = floor(double(R[i])*1.1);
            cur[i] = 1;
            ind[i] = 0;
        }
        ans = 0;
        flag = true;
        while (flag) {
            for (int j = 0; j < N; j++) {
                if (!flag) break;
                while (!(lo[j] <= Q[j][ind[j]] && Q[j][ind[j]] <= hi[j])) {
                    while (ind[j] < P && lo[j] > Q[j][ind[j]]) ind[j]++;
                    if (ind[j] >= P) {
                        flag = false;
                        break;
                    }
                    while (hi[j] < Q[j][ind[j]]) {
                        cur[j]++;
                        lo[j] = ceil(double(R[j]*cur[j])*0.9);
                        hi[j] = floor(double(R[j]*cur[j])*1.1);
                    }
                }
            }
            if (!flag) break;
            _max = 0; _min = 10000000;
            for (int j = 0; j < N; j++) {
                if (cur[j] > _max) _max = cur[j];
                if (cur[j] < _min) _min = cur[j];
            }
            if (_max == _min) {
                ans++;
                for (int j = 0; j < N; j++) {
                    ind[j]++;
                    if (ind[j] >= P) flag = false;
                }
            }
            else {
                for (int j = 0; j < N; j++)
                    if (cur[j] <= _max) {
                        cur[j] = _max;
                        lo[j] = ceil(double(R[j]*cur[j])*0.9);
                        hi[j] = floor(double(R[j]*cur[j])*1.1);
                    }
            }
        }
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
