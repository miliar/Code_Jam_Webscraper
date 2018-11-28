#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void flip(char * values, int size) {
//    cout << "FL: " << values << endl;
    for (int i = 0; i < size; ++i) {
        if (values[i] == '-') {
            values[i] = '+';
        } else {
            values[i] = '-';
        }
    }
}

int tryFlipping(const std::string& pancakes, int flipper) {
//    cout << "IN: " << pancakes << " FL: " << flipper << endl;
    std::string p = pancakes;
    auto size = p.size();
    int counter = 1;
    int coherent = -1;
    int flipCount = 0;
    for (int i = 0; i < size; ++i) {
        if (p[i] == '-') {
//            cout << "CH: " << p[i] << " C: " << counter << endl;
            if (coherent < 0) {
                coherent = 1;
            }
        } else {
            if (coherent < 0) {
                // Still +
                continue;
            }
        }

        if (counter == flipper) {
            flip(&p[i - (flipper - 1)], flipper);
            coherent = -1;
            counter = 1;
            i -= flipper;
            ++flipCount;
        } else {
            ++counter;
        }
    }

//    cout << "F: " << p << endl;

    for (auto ch : p) {
        if (ch == '-') {
            return -1;
        }
    }

    return flipCount;
}

int main(int argc, char ** argv) {
    int t, k;
    std::string s;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cin >> s >> k;

        int count = tryFlipping(s, k);
        if (count >= 0) {
            cout << "Case #" << i << ": " << count << " " << endl;
        } else {
            cout << "Case #" << i << ": " << "IMPOSSIBLE" << " " << endl;
        }
    }

    return 0;
}
