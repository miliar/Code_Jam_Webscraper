#include <bits/stdc++.h>
using namespace std;
using i64 = int64_t;

bool solve(int c1, int c2, int c3, int c12, int c23, int c13, string& result) {
    if (c12 > 0) {
        if (c3 < c12) {
            return false;
        }
        if (c3 == c12) {
            if (c1 > 0 || c2 > 0 || c23 > 0 || c13 > 0) {
                return false;
            }
            result.clear();
            for (int i = 0; i < c3; ++i) {
                result.push_back('B');
                result.push_back('O');
            }
            return true;
        }

        if (!solve(c1, c2, c3 - c12, 0, c23, c13, result)) {
            return false;
        }

        string sub;
        for (int i = 0; i < c12; ++i) {
            sub.push_back('O');
            sub.push_back('B');
        }

        for (size_t i = 0; i < result.size(); ++i) {
            if (result[i] == 'B') {
                result.insert(result.begin() + i + 1, sub.begin(), sub.end());
                return true;
            }
        }

        assert(false);
    }
    if (c23 > 0) {
        if (c1 < c23) {
            return false;
        }
        if (c1 == c23) {
            if (c3 > 0 || c2 > 0 || c13 > 0 || c12 > 0) {
                return false;
            }
            result.clear();
            for (int i = 0; i < c1; ++i) {
                result.push_back('R');
                result.push_back('G');
            }
            return true;
        }
        if (!solve(c1 - c23, c2, c3, c12, 0, c13, result)) {
            return false;
        }

        string sub;
        for (int i = 0; i < c23; ++i) {
            sub.push_back('G');
            sub.push_back('R');
        }

        for (size_t i = 0; i < result.size(); ++i) {
            if (result[i] == 'R') {
                result.insert(result.begin() + i + 1, sub.begin(), sub.end());    
                return true;
            }
        }

        assert(false);
    }
    if (c13 > 0) {
        if (c2 < c13) {
            return false;
        }
        if (c2 == c13) {
            if (c3 > 0 || c1 > 0 || c23 > 0 || c12 > 0) {
                return false;
            }
            result.clear();
            for (int i = 0; i < c2; ++i) {
                result.push_back('Y');
                result.push_back('V');
            }
            return true;
        }

        if (!solve(c1, c2 - c13, c3, c12, c23, 0, result)) {
            return false;
        }

        string sub;
        for (int i = 0; i < c13; ++i) {
            sub.push_back('V');
            sub.push_back('Y');
        }

        for (size_t i = 0; i < result.size(); ++i) {
            if (result[i] == 'Y') {
                result.insert(result.begin() + i + 1, sub.begin(), sub.end());    
                return true;
            }
        }

        assert(false);
    }

    result.clear();

    int last = -1;
    int firstput = -1;
    int C[3] = {c1, c2, c3};
    while (C[0] + C[1] + C[2] > 0) {
        int best = -1;
        for (int i = 0; i < 3; ++i) {            
            if (C[i] == 0) continue;
            if (i == last) continue;
            if (best == -1 || C[i] > C[best] || (C[i] == C[best] && i == firstput)) {
                best = i;
            }
        }
        if (best == -1) {
            return false;
        }

        --C[best];
        if (best == 0) {
            result.push_back('R');
        }else
        if (best == 1) {
            result.push_back('Y');
        }else
        if (best == 2) {
            result.push_back('B');
        }

        if (firstput == -1) {
            firstput = best;
        }
        last = best;
    }

    if (result.size() > 1 && result.back() == result.front()) {
        return false;
    }
    return true;
}
                                    
int main() {
    freopen(".in", "r", stdin);
    freopen(".out", "w", stdout);
    ios::sync_with_stdio(false);

    int T;
    cin >> T;
    for (int __ =1; __ <= T; ++__) {
        int N, R, O, Y, G, B, V;
        cin >> N >> R >> O >> Y >> G >> B >> V;

        string output;
        if (!solve(R, Y, B, O, G, V, output)) {
            output = "IMPOSSIBLE";
        }
        cout << "Case #" << __ << ": " << output << '\n';
    }

    return 0;
}
