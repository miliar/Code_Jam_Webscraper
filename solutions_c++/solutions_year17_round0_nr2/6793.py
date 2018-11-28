#include <cstdio>
#include <cstring>

using namespace std;
const int N = 20;

char ss[N];
int lims[N], num[N], len;

bool dfs(int depth, int cur, bool reached) {
    num[depth] = cur;
    if (depth == len - 1) return true;
    int true_limit = reached ? lims[depth + 1] : 9;
    if (cur > true_limit) return false;
    for (int j = true_limit; j >= cur; j--) {
        if (dfs(depth + 1, j, reached && (j == lims[depth + 1]))) return true;
    }
    return false;
}

int main() {
    freopen("/Users/liuxiao/Downloads/B-large.in", "r", stdin);
    freopen("/Users/liuxiao/Downloads/B-large.out", "w", stdout);
    int TTT;
    scanf("%d", &TTT);
    for (int TT = 1; TT <= TTT; TT++) {
        scanf("%s", ss);
        len = strlen(ss);
        for (int i = 0; i < len; i++) lims[i] = ss[i] - '0';
        memset(num, 0, sizeof(num));
        for (int i = lims[0]; i >= 0; i--)
            if (dfs(0, i, i == lims[0]))
                break;
        printf("Case #%d: ", TT);
        int pos = 0;
        while (num[pos] == 0 && pos < len - 1) pos++;
        while (pos < len) printf("%c", num[pos++] + '0');
        printf("\n");
    }
    return 0;
}