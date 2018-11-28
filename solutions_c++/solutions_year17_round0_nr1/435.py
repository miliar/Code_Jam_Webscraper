#include <iostream>
#include <string>

using namespace std;

void flipPancakes(string& row, int flipperSize, int position) {
    for (int i = 0; i < flipperSize; i++) {
        if (row[position + i] == '-') {
            row[position + i] = '+';
        }
        else {
            row[position + i] = '-';
        }
    }
}

int main () {
    int testCases;
    int flipperSize;
    int count;
    bool possible;
    string row;

    cin >> testCases;
    for (int curCase = 1; curCase <= testCases; curCase++) {
        cin >> row >> flipperSize;

        //cout << row << " " << flipperSize << endl;

        possible = true;
        count = 0;
        for (unsigned int i = 0; i < row.size(); i++) {
            if (row[i] == '-') {
                if (i + flipperSize > row.size()) {
                    possible = false;
                    break;
                }
                flipPancakes(row, flipperSize, i);
                count++;
            }
        }

        cout << "Case #" << curCase << ": ";
        if (possible) {
            cout << count << endl;
        }
        else {
            cout << "IMPOSSIBLE" << endl;
        }

        //cout << row << " " << flipperSize << endl;
    }

    return 0;
}