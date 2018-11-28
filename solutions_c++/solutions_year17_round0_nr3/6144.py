#include <bits/stdc++.h>
using namespace std;

ifstream fin("C:\\Users\\lkmak\\user\\alg\\codejam_clion\\C-small-2-attempt0.in");
ofstream fout("C:\\Users\\lkmak\\user\\alg\\codejam_clion\\output.txt");

void solve(int n, int k) {
    multiset<int> s;
    s.insert(-n);
    for (int i = 0; i < k - 1; i++) {
        auto p = *s.begin();
        s.erase(s.begin());
        s.insert(-(-p / 2));
        s.insert(-((-p - 1) / 2));
    }
    auto x = *s.begin();
    fout << -x / 2 << " " << (-x - 1) / 2  << endl;
    cout << "+" << endl;
}

int main() {
    int T;
    fin >> T;

    for (int t = 0; t < T; t++) {
        int n, k;
        fin >> n >> k;
        fout << "Case #" << t + 1 << ": ";
        solve(n, k);
    }

    return 0;
}