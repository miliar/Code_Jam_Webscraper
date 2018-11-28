#include <bits/stdc++.h>

using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, x) for(auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
#define scanf nope
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

void flip(char& c) {
        if (c == '-') c = '+';
        else if (c == '+') c = '-';
        else assert(false);
}

void solve() {
        string S;
        int K;
        cin >> S >> K;
        int res = 0;
        for (int i = 0; i <= sz(S) - K; ++i) {
                if (S[i] == '-') {
                        for (int j = 0; j < K; ++j) {
                                flip(S[i + j]);
                        }
                        res++;
                }
        }
        if (count(all(S), '-')) cout << "IMPOSSIBLE" << endl;
        else cout << res << endl;
}

int main() {
        int N;
        cin >> N;
        rep(i,1,N+1) {
                cout << "Case #" << i << ": ";
                solve();
        }
}
