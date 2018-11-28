#include "stdafx.h"
#include "Qual_A.h"


void Qual_A::Solve() {
    int k;
    string s;
    cin >> s >> k;
    queue<int> invertion_positions;
    bool isInvert = false;
    int ans = 0;
    for (int i = 0; i < s.size(); ++i) {
        if (!invertion_positions.empty() && invertion_positions.front() == i) {
            isInvert = !isInvert;
            invertion_positions.pop();
        }
        if (s[i] == '+' ^ isInvert)
            continue;
        if (i + k > s.size()) {
            cout << "IMPOSSIBLE" << endl;
            return;
        }
        ans++;
        isInvert = !isInvert;
        invertion_positions.push(i + k);
    }
    cout << ans << endl;
}

Qual_A::Qual_A() {
}


Qual_A::~Qual_A() {
}
