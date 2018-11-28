#include <cstdio>
#include <vector>
#include <cstring>

using namespace std;

const int maxN = 111;

int N, P, G[maxN], mark[maxN], ans;

void solve() {
    ans = 0;
    memset(mark, 0, sizeof(mark));
    //case 1:
    for(int i = 0; i < N; ++i) {
        if(G[i] % P == 0 && !mark[i]) {
            ++ans, mark[i] = 1;
            //printf("%d\n", i);
        }
    }
    //case 2:
    for(int i = 0; i < N; ++i) {
        for(int j = i+1; j < N; ++j) {
            if((G[i]+G[j]) % P == 0 && !mark[i] && !mark[j]) {
                ++ans, mark[i] = mark[j] = 1;
                //printf("%d %d\n", i, j);
            }
        }
    }
    //case 3:
    for(int i = 0; i < N; ++i) {
        for(int j = i+1; j < N; ++j) {
            for(int k = j+1; k < N; ++k) {
                if((G[i]+G[j]+G[k]) % P == 0 && !mark[i] && !mark[j] && !mark[k]) {
                    ++ans, mark[i] = mark[j] = mark[k] = 1;
                    //printf("%d %d %d\n", i, j, k);
                }
            }
        }
    }
    //case 4:
    for(int i = 0; i < N; ++i) {
        for(int j = i+1; j < N; ++j) {
            for(int k = j+1; k < N; ++k) {
                for(int l = k+1; l < N; ++l) {
                    if((G[i]+G[j]+G[k]+G[l]) % P == 0 && !mark[i] && !mark[j] && !mark[k] && !mark[l]) {
                        ++ans, mark[i] = mark[j] = mark[k] = mark[l] = 1;
                        //printf("%d %d %d %d\n", i, j, k, l);
                    }
                }
            }
        }
    }
    //leftover:
    for(int i = 0; i < N; ++i) if(!mark[i]) {
        ++ans; break;
    }
}

int main() {
#ifdef RS16
    //freopen("inp.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
#endif // RS16

    int T; scanf("%d", &T);
    for(int t = 1; t <= T; ++t) {
        printf("Case #%d: ", t);
        scanf("%d%d", &N, &P);
        for(int i = 0; i < N; ++i) {
            scanf("%d", G+i);
        }

        solve();
        printf("%d\n", ans);
    }
}
