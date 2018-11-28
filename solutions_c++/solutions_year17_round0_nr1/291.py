#include <iostream>
#include <string>

using namespace std;

void doit() {
    string pancakes;
    int K;
    cin >> pancakes >> K;
    int panlen = pancakes.size();

    int numflips = 0;
    for (int i = 0; i < panlen; ++i) {
        if (pancakes[i] == '-') {
            if (i + K > panlen) {
                numflips = -1;
                break;
            }
            else {
                numflips += 1;
                for (int j = i; j < i+K; ++j) {
                    if (pancakes[j] == '-') pancakes[j] = '+';
                    else pancakes[j] = '-';
                }
            }
        }
    }
    if (numflips >= 0) {
        cout << numflips << endl;
    }
    else {
        cout << "IMPOSSIBLE" << endl;
    }
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        doit();
    }
    return 0;
}
