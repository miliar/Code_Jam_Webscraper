//
// Created by XelaPi.
//
#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>

using namespace std;

int main() {

    int num;

    cin >> num;

    for (int i = 0; i < num; i++) {
        cout << "Case #" << (i + 1) << ":\n";

        int row, column;

        cin >> row >> column;

        char * array = new char[row * column];

        unordered_map<char, bool> used;

        for (int j = 0; j < row; ++j) {
            for (int k = 0; k < column; ++k) {
                cin >> array[j * column + k];
                if (array[j * column + k] != '?') {
                    used.insert(make_pair(array[j * column + k], false));
                }
            }
        }

        for (int xSize = column; xSize > 0; --xSize) {
            for (int ySize = row; ySize > 0; --ySize) {
                for (int xStart = 0; xStart <= column - xSize; xStart++) {
                    for (int yStart = 0; yStart <= row - ySize; yStart++) {
                        bool allButOneBlank = true;
                        char one = ' ';

                        for (int x = xStart; x < xStart + xSize; x++) {
                            for (int y = yStart; y < yStart + ySize; y++) {
                                char test = array[y * column + x];

                                if (test != '?') {
                                    if (one != ' ') {
                                        allButOneBlank = false;
                                    } else {
                                        one = test;
                                    }
                                }
                            }
                        }

                        if (!allButOneBlank || one == ' ' || used[one]) {
                            continue;
                        }

                        used[one] = true;

                        for (int x = xStart; x < xStart + xSize; x++) {
                            for (int y = yStart; y < yStart + ySize; y++) {
                                array[y * column + x] = one;
                            }
                        }
                    }
                }
            }
        }


        for (int j = 0; j < row; ++j) {
            for (int k = 0; k < column; ++k) {
                cout << array[j * column + k];
            }
            cout << endl;
        }
    }

    return 0;
}