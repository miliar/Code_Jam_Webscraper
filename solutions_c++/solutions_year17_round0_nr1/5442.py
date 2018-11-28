#include <cstdio>
#include <algorithm>
#include <cstring>
#include <climits>

using namespace std;

const int maxn = 1010;
char ss[maxn];
char cs[maxn];
int mn = INT_MAX, ans;

bool solve1(char* rs, int l, int k) {
    ans = 0;
    int st = 0;
    while (st < l && rs[st] == '+')
        st++;
    if (st == l) 
        return true;
    else {
        while (st + k - 1 < l) {
            for (int i = 0; i < k; i++)
                rs[st + i] = (rs[st + i] == '-') ? '+' : '-';
            ans++;
            while (st < l && rs[st] == '+') st++;
        }
        for (int i = 0; i < l; i++)
            if (rs[i] == '-') return false;
        return true;
    }
}

void cpy_rev(char* d, int l, char* s) {
    for (int i = 0; i < l; i++)
        d[i] = s[l - 1 - i];
    d[l] = 0;
}

int main() {
    int tt, k;
    scanf("%d\n", &tt);
    for (int t = 1; t <= tt; t++) {
        printf("Case #%d: ", t);
        scanf("%s %d\n", ss, &k);
        mn = INT_MAX;
        bool b = true;
        int l = strlen(ss);
        cpy_rev(cs, l, ss);
        bool res = solve1(ss, l, k);
        if (res) mn = min(mn, ans);
        res = solve1(cs, l, k);
        if (res) mn = min(mn, ans);
        if (mn == INT_MAX) printf("IMPOSSIBLE\n");
        else printf("%d\n", mn);
    }
}
