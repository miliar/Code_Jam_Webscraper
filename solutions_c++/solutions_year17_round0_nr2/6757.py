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
        string number;
        cin >> number;
        int size = number.length();
        int newSize = size;
        for (int i = size - 1; i > 0; i--) {
            int current = number[i] - '0';
            int previous = number[i-1] - '0';
            if (current < previous) {
                // Tidy it!
                newSize = i;
                number[i-1] = (previous - 1) + '0';
            }
        }
        string result;
        if (number[0] == '0') {
            result = number.substr(1, newSize - 1);
        } else {
            result = number.substr(0, newSize);
        }
        cout << result;
        for (int i = newSize; i < size; i++) {
            cout << 9;
        }
        cout << endl;
    }

    return 0;
}
