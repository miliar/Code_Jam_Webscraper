#include <iostream>
#include <cstdio>
using namespace std;

int T;
int D, N;
double speed[1000], pos[1000];

void read() {
    cin >> T;
}

void solve() {
    for (int t = 1; t <= T; ++t) {
        cin >> D >> N;
        for (int n = 0; n < N; ++n) {
            cin >> pos[n] >> speed[n];
        }
        double time, currTime;
        time = (D - pos[N - 1]) / speed[N - 1];
        currTime = time;
        for (int n = N - 1; n >= 0; --n) {
            time = (D - pos[n]) / speed[n];
            if(currTime < time) {
                currTime = time;
            }
        }
        printf("Case #%d: %.6f\n", t, D / currTime);
    }
}

int main()
{
    freopen("in.in", "r", stdin);
    freopen("out.out", "w", stdout);
    read();
    solve();
    return 0;
}
