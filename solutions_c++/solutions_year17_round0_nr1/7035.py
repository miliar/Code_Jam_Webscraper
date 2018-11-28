#include <bits/stdc++.h>
using namespace std;

ifstream fin("C:\\Users\\lkmak\\user\\alg\\codejam_clion\\A-large.in");
ofstream fout("C:\\Users\\lkmak\\user\\alg\\codejam_clion\\output.txt");

void solve(string &s, int k) {
    int n = s.size();
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        a[i] = (s[i] == '+' ? 1 : 0);
    }

    int cnt = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] == 0) {
            if (i + k - 1 >= n) {
                fout << "IMPOSSIBLE" << endl;
                return;
            }
            else {
                cnt++;
                for (int j = i; j < i + k; j++) {
                    a[j] = 1 - a[j];
                }
            }
        }
    }

    fout << cnt << endl;
}

int main() {
    int T;
    fin >> T;

    for (int t = 0; t < T; t++) {
        string s;
        int k;
        fin >> s >> k;
        fout << "Case #" << t + 1 << ": ";
        solve(s, k);
    }

    return 0;
}