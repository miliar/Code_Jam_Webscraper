#include <iostream>
#include <string>
#include <stdlib.h>
#include <algorithm>
#include <cstdio>
#include <fstream>


using namespace std;

int Len(long long x) {
    int i = 0;
    while (x) {
        x /= 10;
        i++;
    }
    return i;
}

int Raz(long long x, int y) {
    long long z = x;
    for (int i = 0; i < Len(x) - y; i++) {
        z /= 10;
    }
    return (int)(z % 10);
}

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int t;
    long long x[201];
    long long d[190];
    d[0] = 1;
    for (int i = 0; i < 19; i++) {
        d[i + 1] = 10 * d[i];
    }

    cin >> t;
    for (int i = 0; i < t; i++) {
        cin >> x[i];
        int len = Len(x[i]);
        for (int j = 1; j < len; j++) {
            for (int h = 1; h < len; h++) {
                if (Raz(x[i], h) > Raz(x[i], h + 1)) {
                    x[i] = (x[i] / d[Len(x[i]) - h] - 1) * d[Len(x[i]) - h] + (d[Len(x[i]) - h] - 1);
                }
            }
        }
        cout << "Case #" << i + 1 << ": " << x[i] << endl;
    }
    return 0;
}
