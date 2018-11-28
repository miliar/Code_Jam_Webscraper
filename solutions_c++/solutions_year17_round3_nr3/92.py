#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int N, K;
        cin >> N >> K;
        double U;
        cin >> U;
        vector<double> v(N);
        for (int i = 0; i < N; i++) {
            cin >> v[i];
        }
        
        sort(v.begin(), v.end());
        
        double result = 0;
        double eps = 1e-8;
        for (int i = 0; i < N - 1; i++) {
            if (v[i] + eps < v[i+1]) {
                double cur = v[i+1] - v[i];
                cur *= i + 1;
                cur = min(U, cur);
                U -= cur;
                for (int j = 0; j <= i; j++) {
                    v[j] += cur / (i + 1);
                }
            }
        }

        for (int i = 0; i < N; i++) 
            v[i] += U / N;

        result = 1;
        for (auto p : v)
            result *= p;

        cout.precision(10);
        cout << fixed;
        
        cout << "Case #" << t << ": " << result;
        cout << '\n';
    }
    
}
