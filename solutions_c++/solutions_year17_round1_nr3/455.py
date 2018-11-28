#include <algorithm>
#include <fstream>
#include <iostream>
#include <cmath>
#include <set>

using namespace std;

int justDoIt(int numberOfDebuff, int numberOfBuff, int hd, int ad, int hk, int ak, int b, int d) {
    int hCur = hd;
    int cnt = 0;
    while (numberOfDebuff > 0) {
        if (ak - d >= hCur && ak >= hd) {
            return 100 * 100;
        }
        if (ak - d >= hCur) {
            hCur = hd - ak;
        } else {
            ak -= d;
            hCur -= ak;
            numberOfDebuff--;
        }
        cnt++;
        if (cnt >= 10000) {
            return 10000;
        }
    }
    while (numberOfBuff > 0) {
        if (ak >= hCur) {
            hCur = hd - ak;
        } else {
            ad += b;
            hCur -= ak;
            numberOfBuff--;
        }
        cnt++;
        if (cnt >= 10000) {
            return 10000;
        }
    }
    while (hk > 0) {
        if (ad >= hk) {
            return cnt + 1;
        }
        if (ak >= hCur) {
            hCur = hd - ak;
        } else {
            hk -= ad;
            hCur -= ak;
        }
        cnt++;
        if (cnt >= 10000) {
            return 10000;
        }
    }
}

int main()
{
    ifstream cin("C-small-attempt0.in");
    ofstream out("output.txt");
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        int hd, ad, hk, ak, b, d;
        cin >> hd >> ad >> hk >> ak >> b >> d;
        // будем ли его дебафать
        int ans = 100 * 100;
        for (int i = 0; i <= 100; ++i) {
            for (int j = 0; j <= 100; ++j) {
                ans = min(ans, justDoIt(i, j, hd, ad, hk, ak, b, d));
            }
        }
        if (ans < 10000) {
            out << "Case #" << test << ": " << ans << endl;
        } else {
            out << "Case #" << test << ": " << "IMPOSSIBLE" << endl;
        }
    }
    return 0;
}