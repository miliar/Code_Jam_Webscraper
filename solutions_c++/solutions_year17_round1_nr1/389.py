#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <queue>
#include <stack>

using namespace std;

const int maxn = 26;

char s[maxn][maxn];
bool f[maxn];
int R, C;

int main(int argc, char const *argv[]) {
    freopen("A-large.in", "r", stdin);
    freopen("b.txt", "w", stdout);
    int T; cin>>T;
    int kase = 1;
    while (T --) {
        cin>>R>>C;
        memset(f, false, sizeof(f));
        for (int i = 0; i < R; i ++) {
            scanf("%s", s[i]);
            int tmp = 0;
            for (int j = 0; j < C; j ++)
                tmp += (s[i][j] == '?');
            if (tmp == 0) f[i] = true;
            if (tmp != C) {
                for (int j = 1; j < C; j ++) if (s[i][j] == '?' && s[i][j - 1] != '?')
                    s[i][j] = s[i][j - 1];
                for (int j = C - 1; j >= 0; j --) if (s[i][j] == '?' && s[i][j + 1] != '?')
                    s[i][j] = s[i][j + 1];
                f[i] = true;
            }
            if (tmp == C) {
                if (i > 0 && f[i - 1]) {
                    for (int j = 0; j < C; j ++)
                        s[i][j] = s[i - 1][j];
                    f[i] = true;
                }
            }
        }
        for (int i = R - 1; i >= 0; i --) {
            if (!f[i] && f[i + 1]) {
                for (int j = 0; j < C; j ++)
                    s[i][j] = s[i + 1][j];
                f[i] = true;
            }
        }
        printf("Case #%d:\n", kase ++);
        for (int i = 0; i < R; i ++) {
            for (int j = 0; j < C; j ++)
                cout<<s[i][j];
            cout<<endl;
        }
    }
    return 0;
}