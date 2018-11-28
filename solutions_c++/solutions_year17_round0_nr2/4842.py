#include <iostream>
#include <map>
#include <vector>

using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int tc;
    cin >> tc;

    for (int tc_i = 0; tc_i < tc; tc_i++) {
        long long n;
        cin >> n;

        int digit[20];
        int length = 0;

        while (n) {
            digit[length++] = (int)(n % 10);

            n /= 10;
        }

        for (int i = 0; i < length/2; i++) {
            swap(digit[i], digit[length - 1 - i]);
        }

        bool done = false;
        int originalLength = length;

        while (!done) {
            done = true;

            for (int i = 0; i < length - 1; i++) {
                if (digit[i] > digit[i + 1]) {
                    digit[i]--;

                    for (int j = i + 1; j < length; j++) {
                        digit[j] = 9;
                    }

                    length = i + 1;

                    done = false;
                    break;
                }
            }
        }

        cout << "Case #" << (tc_i + 1) << ": ";

        bool wasNonZero = false;

        for (int i = 0; i < originalLength; i++) {
            if (digit[i] == 0 && !wasNonZero) {
                continue;
            }

            cout << digit[i];

            wasNonZero = digit[i] > 0;
        }

        cout << endl;
    }

    return 0;
}