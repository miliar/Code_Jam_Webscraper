#include <bits/stdc++.h>

using namespace std;

int T;
long long N, K;

int main() {
    ifstream fin("C.in");
    ofstream fout("C.out");

    fin >> T;
    for (int t = 1; t <= T; t++) {
        fin >> N >> K;
        fout << "Case #" << t << ": ";

        long long so_far = 0, r = N;
        for (int i = 0; ; i++) {
            if (so_far + (1LL << i) >= K) break;
            so_far += (1LL << i);
            r = ((r - 1) >> 1);
        }

        int a = N - r - (r + 1LL) * so_far;
        if (so_far + a < K)
            fout << (r >> 1) << " " << ((r - 1) >> 1) << "\n";
        else fout << ((r + 1) >> 1) << " " << (r >> 1) << "\n";
    }

    fin.close();
    fout.close();

    return 0;
}
