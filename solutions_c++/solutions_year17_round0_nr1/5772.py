#include <iostream>
#include <cstdio>
#include <vector>
#include <fstream>

using namespace std;

int64_t Solution(string s, int k);


int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    // freopen("in.txt", "r", stdin);
    // freopen("out.txt", "w", stdout);
    // ifstream cin("in.txt");
    // ofstream cout("out.txt");
    int cntTest;
    cin >> cntTest;
    for (int test = 0; test < cntTest; ++test) {
        string s;
        int k;
        cin >> s >> k;
        cout << "Case #" << test + 1 << ": ";
        int ans = Solution(s, k);
        if (ans == -1) {
            cout << "IMPOSSIBLE\n";
        } else {
            cout << ans << "\n";
        }
    }
    return 0;
}

int64_t Solution(string s, int k) {
    int cnt = 0;
    for(size_t idx = 0; idx < s.size() - k + 1; ++idx) {
        if (s[idx] == '-') {
            ++cnt;
            for (size_t j = idx; j < idx + k; ++j) {
                if (s[j] == '-') {
                    s[j] = '+';
                } else {
                    s[j] = '-';
                }
            }
        }
        // cerr << s << endl;
    }

    for (size_t idx = 0; idx < s.size(); ++idx) {
        if (s[idx] == '-') {
            return -1;
        }
    }
    return cnt;
}