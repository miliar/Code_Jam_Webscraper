#include <iostream>
#include <string>
using namespace std;

void flip(string& s, int idx, int count) {
    for (int i = idx; i < idx + count; i++) {
        char& c = s[i];
        c = c == '+' ? '-' : '+';
    }
}

void Run(int i) {
    string pancakes;
    int K;

    cin >> pancakes >> K;
    int flip_count = 0;
    for (int idx = 0; idx < pancakes.size(); idx++) {
        // cout << pancakes << endl;
        if (pancakes[idx] == '-') {
            if (idx + K > pancakes.size()) {
                // no way to flip
                cout << "Case #" << i << ": IMPOSSIBLE" << endl;
                return;
            } else {
                flip(pancakes, idx, K);
                flip_count++;
            }
        }
    }
    cout << "Case #" << i << ": " << flip_count << endl;
}

int main() {
    long T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        Run(i + 1);
    }
}
