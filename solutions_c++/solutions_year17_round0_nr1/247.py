#include <iostream>
#include <string>

using namespace std;

int main() {
    int num_cases;
    cin >> num_cases;
    string input;
    int K;
    for (int case_index = 1; case_index <= num_cases; ++case_index) {
        cin >> input >> K;
        int ans = 0;
        size_t pos = 0;
        const size_t N = input.length();
        for (;pos + K <= N; ++pos) {
            if (input[pos] == '-') {
                // Flip everything now.
                ++ans;
                for (size_t i = 0; i < K; ++i) {
                    input[pos + i] ^= 6;
                }
            }
        }
        // Check the last K - 1 slots.
        bool dead = false;
        for (; pos < N; ++pos) {
            if (input[pos] == '-') dead = true;
        }
        cout << "Case #" << case_index << ": ";
        if (dead) {
            cout << "IMPOSSIBLE";
        } else {
            cout << ans;
        }
        cout << endl;
    }
    return 0;
}
