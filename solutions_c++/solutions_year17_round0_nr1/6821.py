#include <cstdio>
#include <cstring>

using namespace std;
const int N = 1005;

char ss[N];
int wid;

int main() {
    freopen("/Users/liuxiao/Downloads/A-large.in", "r", stdin);
    freopen("/Users/liuxiao/Downloads/A-large.out", "w", stdout);
    int TTT;
    scanf("%d", &TTT);
    for (int TT = 1; TT <= TTT; TT++) {
        scanf("%s", ss);
        scanf("%d", &wid);
        int count = 0;
        int len = strlen(ss);
        for (int i = 0; i <= len - wid; i++) {
            if (ss[i] == '-') {
                count++;
                for (int j = 0; j < wid; j++) {
                    if (ss[i + j] == '-') ss[i + j] = '+';
                    else ss[i + j] = '-';
                }
            }
        }
        for (int i = 0; i < len; i++) {
            if (ss[i] == '-') {
                count = -1;
                break;
            }
        }
        printf("Case #%d: ", TT);
        if (count == -1) printf("IMPOSSIBLE\n");
        else printf("%d\n", count);
    }
    return 0;
}