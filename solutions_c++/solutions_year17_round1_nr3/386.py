#include <stdio.h>
#include <algorithm>
#include <string.h>
using namespace std;

const int INF = 0x3f3f3f3f;
const int MAX_VAL = 105;

int solve(int debuf, int buf, int hd, int ad, int hk, int ak, int b, int d) {
    int max_health = hd;
    int res = 0;
    int cured = 0;
    while(debuf > 0 && ak > 0) {
        res++;
        if (hd <= 0) {
            return INF;
        }
        if (hd - max(0, ak - d) <= 0 && !cured) {
            cured = 1;
            hd = max_health - ak;
        } else {
            cured = 0;
            debuf--;
            ak = max(0, ak - d);
            hd -= ak;
        }
    }
    while(buf > 0) {
        res++;
        if (hd <= 0) {
            return INF;
        }
        if (hd - ak <= 0 && !cured) {
            cured = 1;
            hd = max_health - ak;
        } else {
            cured = 0;
            buf--;
            ad += b;
            hd -= ak;
        }
    }
    while(hk > 0) {
        res++;
        if (hd <= 0) {
            return INF;
        }
        //printf("res = %d, hd = %d, hk = %d\n", res, hd, hk);
        if (hk - ad <= 0) {
            hk -= ad;
            break;
        }
        if (hd - ak <= 0 && !cured) {
            cured = 1;
            hd = max_health - ak;
        } else {
            cured = 0;
            hk -= ad;
            hd -= ak;
        }
    }
    //printf("here res = %d, hk = %d\n\n", res, hk);
    if (hk <= 0) {
        return res;
    }
    return INF;
}

int main(void) {
    int t;
    int hd, ad, hk, ak, b, d;

    scanf(" %d", &t);
    for (int caso = 1; caso <= t; caso++) {
        scanf(" %d %d %d %d %d %d", &hd, &ad, &hk, &ak, &b, &d);

        int res = INF;
        for (int i = 0; i <= 100; i++) {
            for (int j = 0; j <= 100; j++) {
                res = min(res, solve(i, j, hd, ad, hk, ak, b, d));
            }
        }

        printf("Case #%d: ", caso);
        if (res < INF) {
            printf("%d\n", res);
        } else {
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}
