#include <cstdint>
#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>

using namespace std;

void solve() {
    string N;
    cin >> N;
    int p = 0;
    for (int i = 0; i < N.size() - 1; i++) {
        if (N[i + 1] > N[i]) {
            p = i + 1;
            continue;
        }
        if (N[i + 1] < N[i]) {
            N[p]--;
            for (int j = p + 1; j < N.size(); j++) N[j] = '9';
            break;
        }
        // i+1 == i
    }
    if (N[0] == '0' && N.size() > 1) {
        N = N.substr(1);
    }
    cout << N << endl;
}

int main() {
    int T;
    cin >> T;
    for (int testcase = 1; testcase <= T; testcase++) {
        cout << "Case #" << testcase << ": ";
        solve();
    }
    return 0;
}
