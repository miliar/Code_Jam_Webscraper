#include <iostream>
#include <string.h>
#include <vector>
#include <map>
#include <algorithm>
#include <set>

using namespace std;
void print(int testNum) {
    cout << "Case #" << testNum << ":\n";
}
const int maxN = 40;
char a[maxN][maxN];

int main(void) {
    int t;
    cin >> t;
    for (int test = 1; test <= t; test++) {
        int r, c;
        cin >> r >> c;
        set <char> cc;
        for (int i = 'A'; i <= 'Z'; i++) {
            cc.insert(i);
        }
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                cin >> a[i][j];
                if (cc.count(a[i][j])) {
                    cc.erase(a[i][j]);
                }
            }
        }
        int wasWas = 0;
        for (int i = 0; i < r; i++) {
            int was = 0;
            for (int j = 0; j < c; j++) {
                if (a[i][j] != '?') {
                    was = 1;
                    int curJ = j - 1;
                    while (curJ >= 0 && a[i][curJ] == '?') {
                        a[i][curJ] = a[i][j];
                        curJ--;
                    }
                    curJ = j + 1;

                    while (curJ < c && a[i][curJ] == '?') {
                        a[i][curJ] = a[i][j];
                        curJ++;
                    }
                }
            }
            if (!was && i != 0) {
                for (int j = 0; j < c; j++) {
                    a[i][j] = a[i - 1][j];
                }
            }
        }

        for (int i = r - 1; i >= 0; i--) {
            int was = 0;
            for (int j = 0; j < c; j++) {
                if (a[i][j] != '?') {
                    was = 1;
                    int curJ = j - 1;
                    while (curJ >= 0 && a[i][curJ] == '?') {
                        a[i][curJ] = a[i][j];
                        curJ--;
                    }
                    curJ = j + 1;

                    while (curJ < c && a[i][curJ] == '?') {
                        a[i][curJ] = a[i][j];
                        curJ++;
                    }
                }
            }
            if (!was && i != r - 1) {
                for (int j = 0; j < c; j++) {
                    a[i][j] = a[i + 1][j];
                }
            }
        }
        print(test);
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                cout << a[i][j];
            }
            cout << endl;
        }

    }


}