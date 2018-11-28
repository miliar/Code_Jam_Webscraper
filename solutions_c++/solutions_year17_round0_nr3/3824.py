#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        long solMax = 0, solMin = 0;
        long N, K;
        cin >> N >> K;
        long bit = 1;
        while (true) {
            long numPersonas = (1 << bit) - 1;
            if (K <= numPersonas) {
                numPersonas = (1 << (bit - 1)) - 1;
                long div = (N - numPersonas) / (numPersonas + 1);
                long mod = (N - numPersonas) % (numPersonas + 1);
                long length = div - 1;
                if (K - numPersonas <= mod) {
                    length++;
                }
                solMax = (long) ceil(length / 2.0);
                solMin = (long) floor(length / 2.0);
                break;
            }
            bit++;
        }
        cout << "Case #" << t << ": " << solMax << " " << solMin << endl;
    }
    return 0;
}