#include <bits/stdc++.h>
using namespace std;

int main(int argc, char** argv) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        string N;
        cin >> N;
        int l = N.length();
        for (int i = l - 2; i >= 0; --i) {
            if (N[i] > N[i + 1]) {
                N[i] = N[i] - 1;
                for (int j = i + 1; j < l; ++j) N[j] = '9';
            }
        }
        cout << "Case #" << t << ": " << stoull(N) << "\n";
    }
    return 0;
}
