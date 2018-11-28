#include <cstdio>
#include <cstring>
#include <string>

using namespace std;

const int maxN = 1111;

int T, N, R, O, Y, G, B, V;

char ans[maxN];

const char imp[] = "IMPOSSIBLE";

void prepare(int R, int Y, int B, int n[], char c[]) {
    if(R >= Y &&  R >= B) {
        n[0] = R, c[0] = 'R';
        if(Y >= B) {
            n[1] = Y, c[1] = 'Y';
            n[2] = B, c[2] = 'B';
        } else {
            n[1] = B, c[1] = 'B';
            n[2] = Y, c[2] = 'Y';
        }
    } else if(Y >= R && Y >= B) {
        n[0] = Y, c[0] = 'Y';
        if(R >= B) {
            n[1] = R, c[1] = 'R';
            n[2] = B, c[2] = 'B';
        } else {
            n[1] = B, c[1] = 'B';
            n[2] = R, c[2] = 'R';
        }
    } else {
        n[0] = B, c[0] = 'B';
        if(R >= Y) {
            n[1] = R, c[1] = 'R';
            n[2] = Y, c[2] = 'Y';
        } else {
            n[1] = Y, c[1] = 'Y';
            n[2] = R, c[2] = 'R';
        }
    }
}

bool solveRYB(int R, int Y, int B) {
    int n[3]; char c[3];
    prepare(R, Y, B, n, c);

    if(n[0] > n[1]+n[2]) return 0;

    //memset(ans, 0, sizeof(ans));
    int prv = -1, cur;
    int pos = 0;
    while(n[0] || n[1] || n[2]) {
        cur = !prv;
        for(int i = 0; i < 3; ++i) {
            if(i == prv) continue;
            if(n[i] > n[cur]) cur = i;
        }

        ans[pos++] = c[cur];
        --n[cur];
        prv = cur;
    }
    ans[pos] = 0;
    return 1;
}

int main() {
#ifdef RS16
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
#endif // RS16

    scanf("%d", &T);
    for(int t = 1; t <= T; ++t) {
        scanf("%d%d%d%d%d%d%d", &N, &R, &O, &Y, &G, &B, &V);
        printf("Case #%d: ", t);
        if(!O && !G && !V) {
            if(solveRYB(R, Y, B)) {
                printf("%s\n", ans);
            } else {
                printf("%s\n", imp);
            }
        } else {
            printf("not implemented\n");
        }
    }
}
