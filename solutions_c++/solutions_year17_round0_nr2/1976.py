#include<bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i=a;i<b;i++)



#define rrep(i,a,b) for(int i=a;i>=b;i--)
string S;
string sol() {
    int N = S.length();
    rrep(i, N - 2, 0) if (S[i] > S[i + 1]) {
        if (S[i] == '1' && i == 0) {
            rep(j, 0, N) S[j] = '9';
            return S.substr(1);
        }

        S[i]--;
        rep(j, i + 1, N) S[j] = '9';
    }
    return S;
}
//-----------------------------------------------------------------------------------
int main() {
    int T; cin >> T;
    rep(t, 1, T + 1) {
        cin >> S;
        printf("Case #%d: %s\n", t, sol().c_str());
    }
}