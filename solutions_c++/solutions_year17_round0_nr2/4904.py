#include <bits/stdc++.h>
using namespace std;

ifstream f("a.in");
ofstream g("a.out");

int N, T, sol;

int tidy(int val) {
    vector < int > tmp;

    while (val != 0) {
        tmp.push_back(val % 10);
        val /= 10;
    }

    reverse(tmp.begin(), tmp.end());

    return is_sorted(tmp.begin(), tmp.end());
}

int main() {
    f >> T;
    for (int q = 1; q <= T; ++q) {
        f >> N;

        for (int i = 1; i <= N; ++i) {
            if (tidy(i)) {
                sol = i;
            }
        }

        g << "Case #" << q << ": " << sol << '\n';
    }
    return 0;
}
