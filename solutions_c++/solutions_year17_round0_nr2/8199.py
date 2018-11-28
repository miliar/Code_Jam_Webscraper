
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

string solve(string & S);

int main() {

    int cases;
    int case_num = 0;

    cin >> cases;

    while (cases--) {
        ++case_num;
        long long N = 0;
        cin >> N;
        auto S = to_string(N);
        auto solution = solve(S);
        cout << "Case #" << case_num << ": ";
        cout << solution << endl;
    }
    return 0;
}

bool correct(string & S) {
    for (auto i = 0u; i < S.size() - 1; ++i)
        if (S[i] > S[i + 1]) {
            S[i] = S[i] - 1;
            for (auto j = i + 1; j < S.size(); ++j)
                S[j] = '9';
            return false;
        }
    return true;
}

string solve(string & S) {
    while (!correct(S))
        ;
    size_t p = 0;
    while(S[p] == '0' && p < S.size())
        ++p;
    return S.substr(p);
}
