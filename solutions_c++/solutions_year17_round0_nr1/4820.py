#include <iostream>
#include <string>
using namespace std;

void flip(string &pancakes, int start_index, int spat_width) {
    pancakes[start_index] = '+';
    for (int i = 1; i < spat_width; ++i) {
        if (pancakes[start_index + i] == '-')
            pancakes[start_index + i] = '+';
        else pancakes[start_index + i] = '-';
    }
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        bool impos = false;
        int num_flips = 0, spat_width;
        string pancakes;
        cin >> pancakes >> spat_width;

        for (int j = 0; j <= pancakes.size() - spat_width; ++j) {
            if (pancakes[j] == '-') {
                flip(pancakes, j, spat_width);
                ++num_flips;
            }
        }

        for (int j = pancakes.size() - spat_width + 1; j < pancakes.size(); ++j)
            if (pancakes[j] == '-') {
                impos = true;
                break;
            }

        cout << "Case #" << i + 1 << ": ";
        if (impos)
            cout << "IMPOSSIBLE" << endl;
        else cout << num_flips << endl;
    }
}
