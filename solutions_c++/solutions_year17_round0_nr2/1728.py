#include <cstdio>
#include <cstring>

char s[100];
void solve(int k) {
    bool ok = true;
    for (int i = 0; i < k; i++)
        if (s[i] > s[i + 1])
            ok = false;
    if (ok) return;
    s[k] = '9';
    s[k - 1] -= 1;
    int cur = k - 1;
    while (s[cur] < '0') {
        s[cur] = '9';
        s[cur - 1] -= 1;
        cur -= 1;
    }
    solve(k - 1);
}

void run(int cas) {
    scanf(" %s", s);
    int l = strlen(s);
    solve(l - 1);
    int p = 0;
    while (s[p] == '0') p++;
    printf("Case #%d: %s\n", cas, s + p);
}

int main() {
    int tt;
    scanf("%d", &tt);
    for (int cas = 1; cas <= tt; cas++)
        run(cas);
    return 0;
}
