#include <iostream>
#include <cstdlib>
#include <cmath>
#include <string.h>
#include <cstring>
#include <cstdio>

using namespace std;

bool mass [1010];

int main( ) {

    freopen("B-small-attempt0.in", "r", stdin);
    freopen("output_file.txt", "w", stdout);

    for (int i = 1; i < 1000; i++) {
        char string [4] = "";

        itoa(i, string, 10);

        for (int j = 1; j <= 9; j++)
            mass[j] = true;

        if (i >= 10 && i < 100) {
            if (string[0] <= string[1])
                mass[i] = true;
        }

        if (i >= 100 && i < 1000) {
            if (string[0] <= string[1] && string[1] <= string[2])
                mass[i] = true;
        }
    }

    int T;

    cin >> T;

    for (int i = 1; i <= T; i++) {
        int bufer;
        cin >> bufer;

        for (int j = bufer; bufer >= 1; j--) {
            if (mass[j] == true) {
                cout <<"Case #"<< i <<": "<< j << endl;
                break;
            }
        }
    }

    fclose (stdin);

    return 0;
}
