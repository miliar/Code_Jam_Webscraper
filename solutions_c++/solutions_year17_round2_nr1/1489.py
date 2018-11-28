#include<iostream>
#include <set>
#include <vector>
#include <queue>
#include <map>
#include <climits>
#include <iomanip>

using namespace std;

int main(int argc, const char *argv[]) {
    size_t T, N;
    double D, K, S;

    cin >> T;

    for(size_t t = 1; t <= T; t++) {
        cin >> D >> N;
        double lateTime = 0;

        for(size_t n = 0; n < N; n++) {
            cin >> K >> S;

            double time = (D-K) / S;
            if(time > lateTime) {
                lateTime = time;
            }
        }

        cout << "Case #" << t << ": " << fixed << setprecision(8) << D / lateTime << endl;
    }

    return 0;
}
