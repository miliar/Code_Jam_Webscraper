#include <iostream>
#include <algorithm>
#include <cstdio>
#include <utility>
using namespace std;

const int N_MAX = 1e3;
const double PI = 3.14159265358979;
int T, N, K;
long long r[N_MAX], h[N_MAX];
int id[N_MAX];

bool hr_comp(int i, int j) {
    return h[i]*r[i] > h[j]*r[j];
}

bool mycomp(const pair<long, long> & p1, const pair<long, long> & p2) {
    return p1.first > p2.first;
}

int main() {
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cin >> N >> K;
        for (int i = 0; i < N; i++) {
            cin >> r[i] >> h[i];
            id[i] = i;
        }
        sort(id, id+N, hr_comp);
        long long ans = 0;
        for (int i = 0; i < N; i++) {
            long long a = r[i]*r[i] + 2*r[i]*h[i];
            int selected = 0;
            for (int j = 0; j < N && selected < K-1; j++) {
                if (id[j] != i && r[id[j]] <= r[i]) {
                    selected++;
                    a += 2*h[id[j]]*r[id[j]];
                }
            }
            ans = max(a, ans);
        }
        printf("Case #%d: %.9f\n", t, ans*PI);
    }
    return 0;
}
