#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void tidy(string &xs) {
    const long long N = xs.size();
    // find first strict decrease and first strict decrease
    long long inc = N; long long dec = N;
    for (long long i = 0; i < N; i++) {
        if (xs[i] < xs[i + 1]) inc = min(inc, i + 1);
        if (xs[i] > xs[i + 1]) { dec = min(dec, i + 1); break; }
    }
    if (dec == N) return;
    if (inc == N) inc = 0;

    for (long long i = dec; i < N; i++) { xs[i] = '9'; }
    xs[inc] = xs[inc] - 1;

    for (long long i = inc + 1; i < dec + 1; i++) { xs[i] = '9'; }

    if (xs[0] == '0') {
        rotate(xs.begin(), xs.begin() + 1, xs.end());
        xs.resize(N - 1);
    }
}

int main(int argc, char *argv[]) {
    int T; cin >> T; int case_no = 1;
    string N;
    while (T--) {
        cin >> N;
        cout << "Case #" << case_no++ << ": ";
        tidy(N);
        cout << N << endl;
    }
}

