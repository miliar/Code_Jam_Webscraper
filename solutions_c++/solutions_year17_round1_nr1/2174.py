#include <iostream>
#include <string>
#include <fstream>
#include <vector>
using namespace std;

int main(){
    ifstream fin ("A-large.in");
    ofstream fout ("1AoutputA.txt");
    int r, c, T;
    string s;
    char** cake;
    fin >> T;
    for (int l = 0; l < T; ++l) {
        fin >> r >> c;
        cout << r << c << endl;
        cake = new char *[r];
        for (int i = 0; i < r; ++i)
            cake[i] = new char[c];
        for (int i = 0; i < r; ++i) {
            fin >> s;
            cout << s << endl;
            for (int j = 0; j < c; ++j) {
                cake[i][j] = s[j];
            }
        }
        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j) {
                for (int k = i - 1; k >= 0 && cake[k][j] == '?'; --k) {
                    cake[k][j] = cake[i][j];
                }
                for (int k = i + 1; k < r && cake[k][j] == '?'; ++k) {
                    cake[k][j] = cake[i][j];
                }
            }
        }
        for (int i = 0; i < c; ++i) {
            if(cake[0][i] == '?'){
                for (int j = i; j < c; ++j) {
                    if(j == c-1 && cake[0][j] == '?'){
                        cout << i << "right" << endl;
                        for (int m = 0; m < r; ++m) {
                            for (int k = i; k < c; ++k) {
                                cake[m][k] = cake[m][i-1];
                            }
                        }
                    }
                    else if(cake[0][j] != '?'){
                        for (int m = 0; m < r; ++m) {
                            for (int k = j - 1; k >= i; --k) {
                                cake[m][k] = cake[m][j];
                            }
                        }
                        break;
                    }
                }
            }
        }
        fout << "Case #" << l+1 << ":" << endl;
        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j) {
                fout << cake[i][j];
            }
            fout << endl;
        }
    }
}
