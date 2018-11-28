#include <bits/stdc++.h>

using namespace::std;

int indexOf(const string& str, const string& substr) {
    auto loc = str.find(substr, 0);
    if (loc != string::npos) {
        return loc;
    }
    return -1;
}

void pancakes(string S, const int K, const int caseno) {
    int i = -1, j = 0, size_of_s = S.size();
    int soln = 0;
    while (((j = indexOf(S, "-")) > i) && (j <= size_of_s - K)) {
        //start flipping
        for (int k = 0; k < K; k++) {
            S[k+j] = (S[k+j] == '+' ? '-' : '+');
        }
        //cout << S << endl;
        soln++;
        i = j;
    }

    j = indexOf(S, "-");
    if (j > -1)
        cout << "Case #" << caseno << ": " << "IMPOSSIBLE" << endl;
    else 
        cout << "Case #" << caseno << ": " << soln << endl;
}

int main() {
    int T, K, caseno = 1;
    string S;

    freopen("pancakes_large.in", "r", stdin);

    cin >> T;
    while (cin >> S >> K) {
        //cout << "test: " << S << ", " << K << endl;
        pancakes(S, K, caseno);
        caseno++;
    }
    return 0;
}