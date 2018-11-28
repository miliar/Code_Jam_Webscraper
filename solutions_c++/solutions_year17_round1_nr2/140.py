#include <iostream>
#include <cassert>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>
#include <cstdio>

using namespace std;

typedef long long ll;

int main() {
    int T;
    cin >> T;
    for (int caseno = 1; caseno <= T; ++caseno) {
        int N, P;
        cin >> N >> P;
        vector<ll> R(N);
        for (int i =0 ; i < N; ++i) cin >> R[i];
        multimap<pair<int, bool>, int> packages;
        for (int i = 0; i < N; ++i) {
            for (int j =0 ; j < P; ++j) {
                int Q;
                cin >> Q;
                int lo = ceil(double(Q) * 10 / 11 / R[i]);
                int hi = floor(double(Q) * 10 / 9 / R[i]);
                //cerr << lo << ".." << hi << ' ' << Q << endl;
                if (lo <= hi) {
                    packages.emplace(make_pair(lo, false), i);
                    packages.emplace(make_pair(hi, true), i);
                }
            }
        }
        int r = 0;
        vector<int> available(N);
        vector<int> used(N);
        for (auto&& p : packages) {
            //cerr << p.first.first << ' ';
            int i = p.second;
            if (p.first.second) {
                // ending
                if (used[i]) {
                    --used[i];
                } else {
                    assert(available[i]);
                    --available[i];
                }
            } else {
                available[i] += 1;
                //cerr << i << ":" << available[i] << "  ";
                int m = *min_element(available.begin(), available.end());
                if (m) {
                    for (auto& x : available) x -= m;
                    for (auto& x : used) x += m;
                    r += m;
                }
            }
        }
        cout << "Case #" << caseno << ": " << r << endl;
    }
}
