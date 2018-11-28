//
//  main.cpp
//  cont
//
//  Created by v on 22/04/17.
//  Copyright © 2017 Vladimir Berezkin. All rights reserved.
//
#include <algorithm>
#include <bitset>
#include <iomanip>
#include <iostream>
#include <set>
#include <vector>
using namespace std;

void f() {
    int N, R, O, Y, G, B, V;
    cin >> N >> R >> O >> Y >> G >> B >> V;
    using NC = pair<int, char>;
    NC all[] = {NC(R, 'R'), NC(Y, 'Y'), NC(B, 'B')};
    sort(all, all+3);
    vector<char> res;
    for (int i = 0; i < N; ++i) {
        if (all[2].first >= all[1].first && all[2].first >= all[0].first &&
            (res.empty() || res.back() != all[2].second) && (res.size() < N - 1 || res.front() != all[2].second)) {
            res.push_back(all[2].second);
            --all[2].first;
        } else if (all[1].first >= all[0].first && all[1].first > 0 &&
                   (res.empty() || res.back() != all[1].second) && (res.size() < N - 1 || res.front() != all[1].second)) {
            res.push_back(all[1].second);
            --all[1].first;
        } else if (all[0].first > 0 && (res.empty() || res.back() != all[0].second)
                    && (res.size() < N - 1 || res.front() != all[0].second)) {
            res.push_back(all[0].second);
            --all[0].first;
        } else {
            break;
        }
    }
    if (res.size() < N) {
        cout << "IMPOSSIBLE";
    } else {
        res.push_back('\0');
        cout << &res[0];
    }
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
