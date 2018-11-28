#include <iostream>
#include <string>

using namespace std;

int main() {
    int T;
    cin >> T;

    for (int i = 0; i < T; ++i) {
        string input;
        cin >> input;

        int tidyPos = input.size();
        char resetPrev = 0;
        for (int i = 1; i < input.size(); ++i) {
            if (input[i-1] > input[i]) {
                tidyPos = i;
                int prev = i - 1;
                input[prev] -= 1;
                while (prev-1 >= 0 && input[prev-1] > input[prev]) {
                    input[prev] = '9';
                    input[prev-1] -= 1;
                    prev--;
                }
                break;
            }
        }

        for (int i = tidyPos; i < input.size(); ++i) {
            input[i] = '9';
        }

        cout << "Case #" << i+1 << ": " << stoll(input) << endl;
    }

    return 0;
}
