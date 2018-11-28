#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    long long T; cin >> T;
    for (long long t = 1; t <= T; t++) {
        long long D, N; cin >> D >> N;

        double max_time_to_finish = 0;

        for (long long i = 0; i < N; i++) {
            long long k, s;
            cin >> k >> s;
            max_time_to_finish = max(max_time_to_finish, (D - k + 0.0) / (s + 0.0));
        }

        cout << "Case #" << t << ": ";
        printf("%.6f", D / max_time_to_finish);
        cout << endl;
    }
    return 0;
}
