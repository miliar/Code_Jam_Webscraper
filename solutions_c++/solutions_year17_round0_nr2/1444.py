#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

char buf[20];

bool check_tidy(char *s)
{
    int n = strlen(s);
    for (int i = 0; i + 1 < n; ++i)
        if (s[i] > s[i + 1])
            return false;
    return true;
}

void solve()
{
    scanf("%s", buf);
    int n = strlen(buf);
    if (check_tidy(buf)) {
        printf("%s", buf);
        return;
    }
    int start = 0;
    for (int i = n - 2; i >= 0; i--) {
        buf[i + 1] = '9';
        if (buf[i] != '0')
            buf[i] -= 1;
        else
            continue;
        if (check_tidy(buf))
            break;
    }
    while (buf[start] == '0')
        start++;
    printf("%s", &buf[start]);
}

int main() {
    int t;
    scanf("%d\n", &t);
    for (int i = 0; i < t; ++i) {
        printf("Case #%d: ", i + 1);
        solve();
        printf("\n");
    }
}
