#include <bits/stdc++.h>
using namespace std;

ifstream fin("C:\\Users\\lkmak\\user\\alg\\codejam_clion\\B-small-attempt2.in");
ofstream fout("C:\\Users\\lkmak\\user\\alg\\codejam_clion\\output.txt");

bool is_good(int a) {
    vector<int> mas;
    while (a > 0) {
        mas.push_back(a % 10);
        a /= 10;
    }

    bool ans = true;
    for (int i = 0; i + 1 < mas.size(); i++) {
        ans = ans & (mas[i] >= mas[i + 1]);
    }

    return ans;
}

void solve(int n) {
    int ans = 0;
    for (int i = 1; i <= n; i++) {
        if (is_good(i))
            ans = i;
    }
    fout << ans << endl;
}

int main() {
    int T;
    fin >> T;

    for (int t = 0; t < T; t++) {
        int n;
        fin >> n;
        fout << "Case #" << t + 1 << ": ";
        solve(n);
    }

    return 0;
}