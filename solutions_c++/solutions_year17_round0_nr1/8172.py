
#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>
#include <map>
#include <queue>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int solve(string &, int);

int main() {

    int cases;
    int case_num =0;

    cin >> cases;

    while (cases--) {
        ++case_num;

        int K;
        string S;
        cin >> S >> K;

        auto solution = solve(S, K);
        cout << "Case #" << case_num << ": ";
        if(solution < 0)
            cout << "IMPOSSIBLE" << endl;
        else
            cout << solution << endl;
    }
    return 0;
}

bool flip(string& S, size_t s, size_t e) {
    if (e > S.size())
        return false;
    for (auto i = s; i < e; ++i)
        if(S[i] == '+')
            S[i] = '-';
        else
            S[i] = '+';
    return true;
}


int solve(string& S, int K){
    int counter = 0;
    for (auto i = 0u; i < S.size(); ++i)
        if (S[i] == '-') {
            bool flipped = flip(S, i, i + K);
            if (!flipped)
                return -1;
            ++counter;
        }
    return counter;
}
