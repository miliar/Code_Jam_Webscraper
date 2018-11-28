#include <algorithm>
#include <fstream>
#include <cmath>
#include <iostream>

using namespace std;

int main()
{
    ifstream cin("A-large.in");
    ofstream cout("output.txt");
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        int r, c;
        char fields[26][26];
        cin >> r >> c;
        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j) {
                cin >> fields[i][j];
            }
        }
        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j) {
                if (fields[i][j] != '?') {
                    int k = i - 1;
                    while (k >= 0 && fields[k][j] == '?') {
                        fields[k][j] = fields[i][j];
                        --k;
                    }
                    k = i + 1;
                    while (k < r && fields[k][j] == '?') {
                        fields[k][j] = fields[i][j];
                        ++k;
                    }
                }
            }
        }
        for (int j = 0; j < c; ++j) {
            for (int i = 0; i < r; ++i) {
                if (fields[i][j] != '?') {
                    int k = j - 1;
                    while (k >= 0 && fields[i][k] == '?') {
                        fields[i][k] = fields[i][j];
                        --k;
                    }
                    k = j + 1;
                    while (k < c && fields[i][k] == '?') {
                        fields[i][k] = fields[i][j];
                        ++k;
                    }
                }
            }
        }
        cout << "Case #" << test << ":" << endl;
        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j) {
                cout << fields[i][j] ;
            }
            cout << endl;
        }
    }
    return 0;
}