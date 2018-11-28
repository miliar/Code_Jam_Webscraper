#include <string>
#include <cstdio>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <iostream>
#include <fstream>
#include <cmath>


using namespace std;
void problem() {
//    cout << endl;
    int  r, c;
    cin >> r >> c;
    vector<string> v(r);

    for (int i  = 0; i < r; ++i) {
        cin >> v[i];
    }

    for (int i  = 0; i < r; ++i) {
        /**
         *  fill from left to right
         * */
        int p = 0;
        while (v[i][p] == '?') {
            p++;
        }
        if (p == c)
            continue;
        char ch = v[i][p];
        int bp = p;
        while (bp >= 0) { // fill to up
            v[i][bp--] = ch;
        }
        while (p < c) {
            if (v[i][p] != '?') {
                ch = v[i][p];
            } else {
                v[i][p] = ch;
            }
            p++;
        }
    }

    /**
     * fill from top to bottom
     */
    for (int i  = 0; i < c; ++i) {
        /**
         *  fill from left to right
         * */
        int p = 0;
        while (v[p][i] == '?') {
            p++;
        }
        char ch = v[p][i];
        int bp = p;
        while (bp >= 0) { // fill to up
            v[bp--][i] = ch;
        }
        while (p < r) {
            if (v[p][i] != '?') {
                ch = v[p][i];
            } else {
                v[p][i] = ch;
            }
            p++;
        }
    }


    for (int i = 0; i < r; ++i) {
        cout << endl<< v[i];
    }

}

int main() {
    ifstream in("../../in");
    cin.rdbuf(in.rdbuf()); //redirect std::cin to in!


    int T;
    cin >> T;
    long long r, t;
    long long result;
    for (int i = 0; i < T; ++i) {
        cout << "Case #" << (i + 1) << ": ";
        problem();
        cout << endl;
    }


    return 0;
}
