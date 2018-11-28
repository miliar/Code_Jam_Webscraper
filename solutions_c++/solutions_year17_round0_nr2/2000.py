#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int T;
string S;

bool valid(string STR) {
    for (int a = 0; a < (int)STR.size() - 1; ++a)
        if (STR[a] > STR[a + 1]) return false;
    return true;
}

long long SET(int POS) {
    string STR = S;
    --STR[POS];
    for (int a = POS + 1; a < (int)STR.size(); ++a)
        STR[a] = '9';
    if (valid(STR)) return stoll(STR);
    return 0;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> T;
    for (int TT = 1; TT <= T; ++TT) {
        cin >> S;
        long long ANS = 0;
        if (valid(S)) ANS = stoll(S);
        for (int a = 0; a < (int)S.size() - 1; ++a) {
            if (S[a] == '0') continue;
            ANS = max(ANS, SET(a));
        }
        cout << "Case #" << TT << ": " << ANS << "\n";
    }
    return 0;
}
