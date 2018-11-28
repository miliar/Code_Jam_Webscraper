#include <iostream>
#include <string>
#include <stdio.h>
#include <string.h>

using namespace std;

int main() {
    int cases;
    cin >> cases;
    for (int i = 1; i <= cases; i++) {
        int numberOfFlips = 0;
        string flip;
        cin >> flip;
        int k = 0;
        cin >> k;
        char flip_array[flip.length()];
        strncpy(flip_array, flip.c_str(), sizeof(flip_array));
        for (int j = 0; j < flip.length() - k + 1; j++) {
            if (flip_array[j] == '-') {
                numberOfFlips++;
                for (int m = 0; m < k; m++) {
                    if (flip_array[j+m] == '-') {
                        flip_array[j+m] = '+';
                    }
                    else {
                        flip_array[j+m] = '-';
                    }
                }
            }
        }
        bool impossible = false;
        for (int j = 0; j < flip.length(); j++)
        {
            if(flip_array[j] == '-') {
                impossible = true;
                cout << "Case #" << i << ": IMPOSSIBLE" << endl;
                break;
            }
        }
        if (impossible == false) {
            cout << "Case #" << i << ": " << numberOfFlips << endl;
        }
    }
}