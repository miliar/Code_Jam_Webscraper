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

struct RH {
    int64_t r;
    int64_t h;
    int64_t rs;
    int64_t hs;
};

int64_t area(vector<RH>::iterator b, vector<RH>::iterator e) {
    int64_t res = 0;
    int64_t m = 0;
    for (auto a = b; a != e; ++a) {
        res += a->hs;
        m = max(m, a->rs);
    }
    return res + m;
}

void f() {
    int N, K;
    cin >> N >> K;
    vector<RH> all(N);
    for (int i = 0; i < N; ++i) {
        cin >> all[i].r >> all[i].h;
        all[i].rs = all[i].r * all[i].r;
        all[i].hs = int64_t(2) * all[i].r * all[i].h;
    }
    sort(all.begin(), all.end(), ^(const RH& a, const RH& b){
        return a.hs > b.hs;
    });
    auto e = all.begin() + K;
    
    auto m = max_element(all.begin(), all.end(), ^(const RH& a, const RH& b){
        return a.hs + a.rs < b.hs + b.rs;
    });
    int64_t res = area(all.begin(), e);
    if (m < e) {
    } else {
        res = area(all.begin(), e);
        for (int i = 0; i < K; ++i) {
            vector<RH> tmp(all.begin(), e);
            tmp[i] = *m;
            auto ai = area(tmp.begin(), tmp.end());
            res = max(res, ai);
        }
    }
    double resd = double(res) * M_PI;
    cout << fixed << setprecision(6) << resd;
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
