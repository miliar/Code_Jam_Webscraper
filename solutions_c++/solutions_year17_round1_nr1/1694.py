#include <iostream>
#include <string>
using namespace std;

void fillRow(char** cake, unsigned column, unsigned i) {
    unsigned firstCharIndex = 0;
    for (; firstCharIndex < column; ++firstCharIndex) {
        if (cake[i][firstCharIndex] != '?')
            break;
    }
    if (firstCharIndex == column)
        return;

    for (unsigned j = 0; j < firstCharIndex; ++j)
        cake[i][j] = cake[i][firstCharIndex];

    unsigned indexJ = firstCharIndex + 1;
    while (indexJ != column) {
        if (cake[i][indexJ] == '?') {
            cake[i][indexJ] = cake[i][firstCharIndex];
            ++indexJ;
        } else {
            firstCharIndex = indexJ;
            ++indexJ;
        }
    }
}

int main() {
	unsigned cases;
	cin >> cases;

	for (unsigned caseIndex = 1; caseIndex <= cases; ++caseIndex) {
        unsigned row, column;
        cin >> row >> column;

        char** cake = new char*[row];
        for (unsigned i = 0; i < row; ++i) {
            cake[i] = new char[column];
            for (unsigned j = 0; j < column; ++j) {
                cin >> cake[i][j];
            }
        }

        unsigned firstNErow = 0;
        for (;firstNErow < row; ++firstNErow) {
            bool find = false;
            for (unsigned j = 0; j < column; ++j) {
                if (cake[firstNErow][j] != '?') {
                    find = true;
                    break;
                }
            }
            if (find)
                break;
        }

        fillRow(cake, column, firstNErow);
        
        for (unsigned i = 0; i < firstNErow; ++i)
            for (unsigned j = 0; j < column; ++j)
                cake[i][j] = cake[firstNErow][j];

        unsigned indexI = firstNErow + 1;
        
        while (indexI != row) {
            bool empty = true;
            for (unsigned j = 0; j < column; ++j) {
                if (cake[indexI][j] != '?') {
                    empty = false;
                    break;
                }
            }

            if (empty) {
                for (unsigned j = 0; j < column; ++j)
                    cake[indexI][j] = cake[firstNErow][j];
            } else {
                fillRow(cake, column, indexI);
                firstNErow = indexI;
            }
            
            ++indexI;

        }



        cout << "Case #" << caseIndex << ":\n";
        for (unsigned i = 0; i < row; ++i) {
            for (unsigned j = 0; j < column; ++j) {
                cout << cake[i][j];
            }
            cout << '\n';
        }
	}
}
