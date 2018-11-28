#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> pi;
const int MAXN = 30;
int TC, N, M;
char s[MAXN][MAXN];
int main() {
    scanf("%d", &TC);
    for (int Txn = 1; Txn <= TC; ++Txn) {
        scanf("%d%d", &N, &M);
        for (int i = 0; i < N; ++i) {
            scanf("%s", s[i]);
            for (int j = 1; j < M; ++j) {
                if (s[i][j] != '?') continue;
                s[i][j] = s[i][j-1];
            }
            for (int j = M-2; j >= 0; --j) {
                if (s[i][j] != '?') continue;
                s[i][j] = s[i][j+1];
            }
        }
        for (int j = 0; j < M; ++j) {
            for (int i = 1; i < N; ++i) {
                if (s[i][j] != '?') continue;
                s[i][j] = s[i-1][j];
            }
            for (int i = N-2; i >= 0; --i) {
                if (s[i][j] != '?') continue;
                s[i][j] = s[i+1][j];
            }
        }
    
        printf("Case #%d:\n", Txn);
        for (int i = 0; i < N; ++i) printf("%s\n", s[i]);
    }
}