//
//  main.cpp
//  cont
//
//  Created by v on 30/04/17.
//  Copyright © 2017 Vladimir Berezkin. All rights reserved.
//
#include <algorithm>
#include <bitset>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <set>
#include <vector>
#include <math.h>
using namespace std;
//  !!!SMALL
void f() {
    int AC, AJ;
    cin >> AC >> AJ;
    using BE = pair<int, int>;
    vector<BE> beC(AC);
    vector<BE> beJ(AJ);
    for (int i = 0; i < AC; ++i) {
        cin >> beC[i].first >> beC[i].second;
    }
    for (int i = 0; i < AJ; ++i) {
        cin >> beJ[i].first >> beJ[i].second;
    }
    int res;
    if (AC == 2 || AJ == 2) {
        auto be = AC ? beC : beJ;
        sort(be.begin(), be.end());
        auto len1 = be[1].second - be[0].first;
        auto len2 = 24*60 + be[0].second - be[1].first;
        auto len = min(len1, len2);
        res = len <= 12*60 ? 2 : 4;
        
    } else {
        res = 2;
    }
    cout << res;
    cout << endl;
}

int main() {
    int cases;
    cin >> cases;
    for (int cas = 1; cas <= cases; ++cas) {
        cout << "Case #" << cas << ": ";
        f();
    }
    return 0;
}
