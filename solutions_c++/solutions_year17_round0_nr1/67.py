#include <bits/stdc++.h>
using namespace std;

int A[1000];

int main() {
    ios_base::sync_with_stdio(0);
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    int T, tI, N, K, i, j, k;
    cin >> T;
    bool b;
    for (tI = 0; tI < T; tI++) {
        string s;
        cin >> s >> K;
        N = s.size();
        k = 0;
        b = 1;
        for (i = 0; i < N; i++) A[i] = (s[i] == '+');
        for (i = 0; i < N - K + 1; i++) if (!A[i]) {for (j = 0; j < K; j++) A[i + j] = !A[i + j]; k++;}
        for (i = N - K + 1; i < N && b; i++) b = A[i];
        if (b) cout << "Case #" << tI + 1 << ": " << k << endl;
        else cout << "Case #" << tI + 1 << ": " << "IMPOSSIBLE" << endl;
    }
    return 0;
}
