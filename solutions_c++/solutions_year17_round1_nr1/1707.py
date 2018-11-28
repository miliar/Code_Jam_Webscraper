#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

int main() {
    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t) {
        cout << "Case #" << t << ":" << endl;
        int R, C;
        cin >> R >> C;
        vector<string> cake(R);
        map<char, int> width;
        for(int r = 0; r < R; ++r) {
            cin >> cake[r];
        }
        // left
        char l;
        for(int r = 0; r < R; ++r) {
            l = '?';
            for(int c = 0; c < C; ++c) {
                if(cake[r][c] == '?') {
                    cake[r][c] = l;
                } else {
                    l = cake[r][c];
                }
            }
        }
        // right
        l = '?';
        for(int r = R - 1; r >= 0; --r) {
            l = '?';
            for(int c = C - 1; c >= 0; --c) {
                if(cake[r][c] == '?') {
                    cake[r][c] = l;
                } else {
                    l = cake[r][c];
                }
                if(l != '?') {
                    width[l]++;
                }
            }
        }
        // down
        for(int r = 0; r < R - 1; ++r) {
            l = '?';
            for(int c = 0; c < C; ++c) {
                if(cake[r][c] != '?') {
                    l = cake[r][c];
                    int i;
                    for(i = 0; i < width[l]; ++i) {
                        if(cake[r + 1][c + i] != '?') {
                            break;
                        }
                    }
                    if(i == width[l]) {
                        for(i = 0; i < width[l]; ++i) {
                            cake[r + 1][c + i] = l;
                        }
                    }
                }
            }
        }
        // up
        for(int r = R - 1; r > 0; --r) {
            l = '?';
            for(int c = 0; c <= C; ++c) {
                if(cake[r][c] != '?') {
                    l = cake[r][c];
                    int i;
                    for(i = 0; i < width[l]; ++i) {
                        if(cake[r - 1][c + i] != '?') {
                            break;
                        }
                    }
                    if(i == width[l]) {
                        for(i = 0; i < width[l]; ++i) {
                            cake[r - 1][c + i] = l;
                        }
                    }
                }
            }
        }
        for(auto row : cake) {
            cout << row << endl;
        }
    }
}
