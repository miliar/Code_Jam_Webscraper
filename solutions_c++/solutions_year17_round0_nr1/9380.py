#include <iostream>
#include <algorithm>

using namespace std;

bool isHappy(char c) { return c == '+'; }
bool isSad(char c)   { return c == '-'; }

// assumption: can solve in a greedy fashion moving left-to-right
// if flipping k pancakes make a k-subtring of all happy, flip and advance one
// otherwise if flipping k pancakes makes a k-substring of a happy followed by a jumble, flip and advance one
// othwerwise just advance one
// return either the number of flips or -1 for impossible
int min_flips(string& pancakes, int k) {
    int num_flips = 0;
    int i = 0;

    while (i <= pancakes.size() - k) {
        if (all_of(pancakes.begin() + i, pancakes.begin() + i + k, isSad)) {
            // flip and advance one
            ++num_flips;
            for (int j = 0; j < k; ++j) { pancakes[i + j] = '+'; };
            i += 1;
        } else {
            bool isFirstSad = isSad(pancakes[i]);
            int isAtLeastOneSad = count_if(pancakes.begin() + i, pancakes.begin() + i + k, isSad);
            bool isPartitioned = is_partitioned(pancakes.begin() + i, pancakes.begin() + i + k, isSad);
            if (isFirstSad) {
                // flip and advance one
                ++num_flips;
                for (int j = 0; j < k; ++j) { pancakes[i + j] = pancakes[i + j] == '-' ? '+' : '-'; };
                i += 1;
            } else {
                // just advance one
                i += 1;
            }
        }
    }

    return all_of(pancakes.begin(), pancakes.end(), isHappy) ? num_flips : -1;
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        string pancake_configuration;
        int flipper_size;
        cin >> pancake_configuration >> flipper_size;
        int answer = min_flips(pancake_configuration, flipper_size);
        cout << "Case #" << i << ": " << (answer == -1 ? "IMPOSSIBLE" : to_string(answer)) << '\n';
    }
}
