#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>

#include <map>

using namespace std;

const int maxLen = 10101;

string S;
int K;
int P[maxLen];
int ans;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T;
    cin >> T;
    for (int Cas = 1; Cas <= T; ++Cas) {
        cin >> S >> K;

        int N = S.size();
        for (int i = 0; i < N; ++i) {
            if (S[i] == '-') {
                P[i] = 0;
            } else {
                P[i] = 1;
            }
        }

        ans = 0;
        for (int i = 0; i < N - K + 1; ++i) {
            if (!P[i]) {
                for (int j = 0; j < K; ++j) {
                    P[i + j] = 1 - P[i + j];
                }
                ans ++;
            }
        }

        printf("Case #%d: ", Cas);
        int flag = false;
        for (int i = N - K + 1; i < N; ++i) {
            if (!P[i]) {
                printf("IMPOSSIBLE\n");
                flag = true;
                break;
            }
        }
        if (flag) {
            continue;
        }
        printf("%d\n", ans);
    }
    return 0;
}
