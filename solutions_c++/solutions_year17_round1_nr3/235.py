#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <cstring>
#include <cmath>
#include <iomanip>
#include <string>
#include <cstdio>

using namespace std;

short u[101][101][101][101];

int TIMER;

int sz;
int ans;

struct State {
    int hd, ad, hk, ak;

    State() {

    }

    State(int _hd, int _ad, int _hk, int _ak) : hd(_hd), ad(_ad), hk(_hk), ak(_ak) {
        u[hd][ad][hk][ak] = TIMER;
    }
};

State q[1000000];

void add(int hd, int ad, int hk, int ak) {
    if (hk <= 0) {
        ans = min(ans, TIMER);
        return;
    }
    if (hd >= 100) {
        hd = 100;
    }
    if (hd <= 0) {
        return;
    }    
    if (ad >= 100) {
        ad = 100;
    }
    if (ak < 0) {
        ak = 0;
    }
    if (u[hd][ad][hk][ak] == 0) {
        q[sz++] = State(hd, ad, hk, ak);
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int Tests;
    cin >> Tests;
    for (int Test = 1; Test <= Tests; Test++) {
        cout << "Case #" << Test << ": ";
        int hd, ad, hk, ak, b, d;
        cin >> hd >> ad >> hk >> ak >> b >> d;
        int HD = hd;
        memset(u, 0, sizeof(u));
        TIMER = 1;
        q[0] = State(hd, ad, hk, ak);
        int i = 0;
        sz = 1;
        ans = 1000000000;
        while (i < sz) {
            if (ans < 1000000000) {
                break;
            }            
            int hd = q[i].hd;
            int ad = q[i].ad;
            int hk = q[i].hk;
            int ak = q[i].ak;
            ///cout << HD << " " << hd << " " << ad << " " << hk << " " << ak << " " << u[hd][ad][hk][ak] << " " << endl;
            TIMER = u[hd][ad][hk][ak] + 1;

            add(HD - ak, ad, hk, ak);
            add(hd - ak, ad + b, hk, ak);
            add(hd - ak, ad, hk - ad, ak);
            add(hd - (ak - d), ad, hk, ak - d);

            i++;
        }
        if (ans == 1000000000) {
            cout << "IMPOSSIBLE" << endl;
        }
        else {
            cout << ans - 1 << endl;
        }
    }
    return 0;
}