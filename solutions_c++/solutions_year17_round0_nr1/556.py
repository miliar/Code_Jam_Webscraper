#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <map>
#include <cmath>
#include <string>

using namespace std;

#define ll long long
int K;
string S;

int main() {
    int T;
    cin>>T;
    for (int t = 1; t <= T; ++t) {
        cin>>S>>K;

        int ans = 0;
        for (int i = 0; i < S.size(); ++i) {
            if (S[i] == '-') {
                ++ans;
                for (int j = 0; j < K; ++j) {
                    if (i + j >= S.size()) {
                        ans += 1<<20;
                        break;
                    }
                    S[i + j] = S[i + j] == '-' ? '+' : '-';
                }
            }
        }
        
        if (ans < 1<<20) {
            printf("Case #%d: %d\n", t, ans);
        } else {
            printf("Case #%d: IMPOSSIBLE\n", t);
        }
    }
}

