#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <utility>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

using namespace std;

int main(int argc, char const *argv[])
{
    int t, T;

    cin >> T;

    for (t = 1; t <= T; ++t) {
        int r, c;

        cin >> r >> c;

        char cake[r * c];

        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j) {
                cin >> cake[i * c + j];
            }
        }

        while (find(cake, cake + r * c, '?') != (cake + r * c)) {
            for (int i = 0; i < r; ++i) {
                if (all_of(cake + i * c, cake + i * c + c, [](char x){return x == '?';})) {
                    if (i == 0) {
                        memcpy(cake, cake + c, c);
                    } else {
                        if (all_of(cake + i * c - c, cake + i * c, [](char x){return x == '?';})) {
                            memcpy(cake + i * c, cake + i * c + c, c);
                        } else {
                            memcpy(cake + i * c, cake + i * c - c, c);
                        }
                    }
                }

                for (int j = 0; j < c; ++j) {
                    if (cake[i * c + j] != '?') {
                        if (j > 0 && cake[i * c + j - 1] == '?') {
                            cake[i * c + j - 1] = cake[i * c + j];
                        }

                        if (j < c - 1 && cake[i * c + j + 1] == '?') {
                            cake[i * c + j + 1] = cake[i * c + j];
                        }
                    }
                }
            }
        }

        printf("Case #%d:\n", t);
        for (int i = 0; i < r; ++i) {
            for (int j = 0; j < c; ++j) {
                putchar(cake[i * c + j]);
            }
            putchar('\n');
        }
    }

    return 0;
}
