#include <cstdio>
#include <cstring>

using namespace std;

const int maxD = 20;

int T, D;

char n[maxD], d[maxD];

inline bool check() {
    for(int i = 0; i < D; ++i) {
        if(d[i] < n[i]) return 1;
        if(d[i] > n[i]) return 0;
    }
    return 1;
}

int main() {
#ifdef RS16
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
#endif // RS16

    scanf("%d", &T);
    for(int t = 1; t <= T; ++t) {
        memset(n, 0, sizeof(n));
        memset(d, 0, sizeof(d));

        scanf("%s", n); D = strlen(n);
        for(int i = 0; i < D; ++i) {
            for(char ch = '9'; ch >= '0'; --ch) {
                for(int j = i; j < D; ++j) d[j] = ch;
                if(check()) break;
            }
        }

        printf("Case #%d: ", t);
        if(d[0] != '0') {
            printf("%s\n", d);
        } else {
            printf("%s\n", d+1);
        }
    }
}
