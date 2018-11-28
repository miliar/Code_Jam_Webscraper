#include <bits/stdc++.h>
using namespace std;

int K, ans = 0;
string s;

void flip(int pos) {
    for (int i = pos; i < pos + K; i++) {
        s[i] = ((s[i] == '+') ? '-' : '+');
    }
    ans++;
}


int main() {
    int T; cin >> T;
    for (int test = 1; test <= T; test++) {
        ans = 0;
        cin >> s >> K;
        
        int N = s.size();
        for (int i = 0; i < N - K + 1; i++) {
            if (s[i] == '-') flip(i);
        }
        for (int i = N - K + 1; i < N; i++) {
            if (s[i] == '-') ans = -1;
        }

        cout << "Case #" << test << ": " << ((ans == -1) ? "IMPOSSIBLE" : to_string(ans)) << endl;
    }
}
