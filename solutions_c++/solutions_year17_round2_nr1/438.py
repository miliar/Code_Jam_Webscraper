#include <bits/stdc++.h>

using namespace std;

int main() {
    ifstream in("input.txt");
    ofstream out("output.txt");
    cin.rdbuf(in.rdbuf());
    cout.rdbuf(out.rdbuf());
    int T;
    cin >> T;
    cout << fixed << setprecision(8);
    for (int test = 1; test <= T; test++) {
        cout << "Case #" << test << ": ";
        int d, n;
        cin >> d >> n;
        double max_time = 0;
        for (int i = 0; i < n; ++i) {
            int k, s;
            cin >> k >> s;
            max_time = max(max_time, (double)(d - k) / s);
        }
        cout << d / max_time << endl;
    }
}