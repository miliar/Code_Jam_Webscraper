#include<bits/stdc++.h>
using namespace std;

int main() {
    string S = "";
    int tc = 0, K = 0, count = 0;
    bool notPossible = false;
    cin >> tc;
    for(int t = 1; t <= tc; ++t) {
        count = 0;
        notPossible = false;
        cin >> S >> K;
        for(int i = 0; i < S.size(); ++i) {
            if(S[i] == '-') {
                if((i + K - 1) >= S.size()) break;
                for(int j = i; j < (i + K) && j < S.size(); ++j)
                    S[j] = S[j] == '-' ? '+' : '-';
                ++count;
            }
        }
        for(int i = 0; i < S.size(); ++i) {
            if(S[i] == '-') {
                notPossible = true;
                break;
            }
        }
        if(notPossible) cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
        else cout << "Case #" << t << ": " << count << endl;
    }
    return 0;
}
