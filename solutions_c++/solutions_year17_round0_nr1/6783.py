/*
 * File:   PancakeFlipper.cpp
 * Author: baplar
 *
 * Created on 8 avril 2017, 15:49
 */

#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char** argv) {
    int t;
    cin >> t;

    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        string pancakes;
        cin >> pancakes;
        int k;
        cin >> k;

        int nbPancakes = pancakes.length();
        vector<int> flips = {};
        bool flipping = false;
        int flipIndex = 0;
        for (int n = 0; n < nbPancakes; n++ ) {
            if (flips.size() > flipIndex && n >= flips[flipIndex] + k) {
                // End of a flip
                flipping = !flipping;
                flipIndex++;
            }
            char pancake = pancakes[n];
            if ((pancake == '-') != flipping) {
                // Need to flip again
                flips.push_back(n);
                flipping = !flipping;
            }
        }
        if (flips.size() > 0 && flips.back() > nbPancakes - k) {
            // We got past the last pancake : it is impossible !
            cout << "IMPOSSIBLE" << endl;
        } else {
            cout << flips.size() << endl;
        }

    }

    return 0;
}
