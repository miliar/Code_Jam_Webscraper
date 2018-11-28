#include <bits/stdc++.h>
using namespace std;
double P[51];
bool beyond[51];
int main() {
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        int N, K;
        cin >> N >> K;
        if(N == K) {
            double U;
            cin >> U;
            for(int i = 1; i <= N; i++) {
                cin >> P[i];
                beyond[i] = false;
            }
            bool has_beyond = true;
            double avg = U;
            while(has_beyond) {
                has_beyond = false;
                avg = U;
                int n = 0;
                for(int i = 1; i <= N; i++) {
                    if(!beyond[i]) {
                        avg += P[i];
                        n++;
                    }
                }
                avg /= n;
                for(int i = 1; i <= N; i++) {
                    if(!beyond[i] && P[i] > avg) {
                        beyond[i] = true;
                        has_beyond = true;
                    }
                }
            }
            double ans = 1;
            for(int i = 1; i <= N; i++) {
                if(beyond[i]) {
                    ans *= P[i];
                } else {
                    ans *= avg;
                }
            }
            cout << "Case #" << t << ": " << fixed << setprecision(7) << ans << endl;
        } else {

        }
    }
    return 0;
}
