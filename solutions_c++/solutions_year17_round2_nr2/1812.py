#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;
int n;
int c[6];
char ch[] = { 'R', 'O', 'Y', 'G', 'B', 'V' };
int ch2i[256];
char ans[1005];
bool check()
{
    for (int i = 0; i < n - 1; i++) {
        if (ans[i] == ans[i + 1]) {
            return false;
        }
    }
    if (ans[n - 1] == ans[0]) {
        return false;
    }
    return true;
}
struct node {
    char c;
    int n;
    bool operator<(const node& rhs)
    {
        return n > rhs.n;
    }
} t[3];
int main()
{
    for (int i = 0; i < 6; i++) {
        ch2i[(int)ch[i]] = i;
    }
    int T;
    scanf("%d", &T);
    for (int cases = 1; cases <= T; cases++) {
        scanf("%d", &n);
        for (int i = 0; i < 6; i++) {
            scanf("%d", &c[i]);
        }
        printf("Case #%d: ", cases);
        if (c[0] > n / 2 || c[2] > n / 2 || c[4] > n / 2) {
            puts("IMPOSSIBLE");
        } else {
            fill(ans, ans + 1005, '0');
            for (int i = 0; i < 3; i++) {
                t[i].c = ch[i * 2], t[i].n = c[i * 2];
            }
            sort(t, t + 3);
            for (int i = 0; i < t[0].n; i++) {
                ans[i * 2] = t[0].c;
            }
            int j = n - 1;
            if (n & 1)
                j--;
            for (int i = 0; i < t[1].n; i++, j -= 2) {
                ans[j] = t[1].c;
            }
            int cnt = 0;
            for (int i = 0; i < n; i++) {
                if (ans[i] == '0') {
                    ans[i] = t[2].c;
                    cnt++;
                }
            }
            assert(cnt == t[2].n);
            ans[n] = '\0';
            assert(check());
            printf("%s\n", ans);
        }
    }
    return 0;
}
