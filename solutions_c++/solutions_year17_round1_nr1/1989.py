#include<iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    int t, r, c;
    char z;
    cin >> t;
    for (int i = 0; i < t; i++) {
        vector<vector<char>> V;
        cin >> r >> c;
        for (int j = 0; j < r; j++) {
            V.push_back(vector<char>());
            for (int x = 0; x < c; x++) {
                cin >> z;
                V[j].push_back(z);
            }
        }

        for (int j = 0; j < r; j++) {
            for (int x = 0; x < c; x++) {
                if (V[j][x] != '?') {
                    int ix = x;
                    while (--ix >= 0 && V[j][ix] == '?') {
                        V[j][ix] = V[j][x];
                    }
                    ix = x;
                    while (++ix < c && V[j][ix] == '?') {
                        V[j][ix] = V[j][x];
                    }
                }
            }
        }

        for (int j = 0; j < r; j++) {
            for (int x = 0; x < c; x++) {
                if (V[j][x] != '?') {
                    int ix = j;
                    while (--ix >= 0 && V[ix][x] == '?') {
                        V[ix][x] = V[j][x];
                    }
                    ix = j;
                    while (++ix < r && V[ix][x] == '?') {
                        V[ix][x] = V[j][x];
                    }
                }
            }
        }

        cout << "Case #" << i + 1 << ":\n";
        for (int j = 0; j < r; j++) {
            for (int x = 0; x < c; x++) {
                cout << V[j][x];
            }
            cout << endl;
        }

    }
}