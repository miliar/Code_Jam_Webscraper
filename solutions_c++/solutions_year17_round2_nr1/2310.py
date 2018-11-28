#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>
using namespace std;

int main() {
    int T, D, N, K, S;
    double time;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cin >> D >> N;
        time = 0;
        for (int j = 0; j < N; j++) {
            cin >> K >> S;
            double temp = (double)(D - K) / (double)S;
            time = time < temp ? temp : time;
        }
        cout << "Case #" << i << ": ";
        printf("%.6f\n", (double)D / time);
    }
    return 0;
}