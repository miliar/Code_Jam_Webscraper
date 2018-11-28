#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

vector<long long> v;

void gen(long long x, int len) {
    v.push_back(x);
    if (len < 18) {
        for (int d = x % 10; d < 10; d++) {
            gen(x * 10 + d, len + 1);
        }
    }
}

long long n;

int main() {
    for (int i = 1; i < 10; i++) {
        gen(i, 1);
    }
    sort(v.begin(),v.end());

    int T;
    cin >> T;
    for (int TC = 1; TC <= T; TC++) {
        cin >> n;
        cout << "Case #" << TC << ": ";
        cout << *(upper_bound(v.begin(), v.end(), n) - 1) << '\n';
    }
}
