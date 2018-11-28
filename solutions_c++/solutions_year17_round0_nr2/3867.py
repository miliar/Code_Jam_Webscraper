#include <iostream>
#include <algorithm>

using namespace std;

int main(int argc, char* argv[]) {
    int T; long long N, R, P10;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cin >> N; R = 0; P10 = 1;

        int digit = N % 10; N = N / 10; R = digit;
        while (N > 0) {
            int curr = N % 10; N = N / 10; P10 *= 10;

            if (digit < curr) {
                R = curr * P10 - 1;
                curr = curr - 1;
            }
            else {
                R = curr * P10 + R;
            }

            digit = curr;
        }

        cout << "Case #" << i << ": " << R << endl;
    }
}