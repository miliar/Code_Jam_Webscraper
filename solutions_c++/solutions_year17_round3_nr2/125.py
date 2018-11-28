#include <cstdio>
#include <cstring>

using namespace std;

const int maxN = 1500;
const int N = 1440;
const int H = N>>1;
const int maxA = 111;

int AC, AJ, A[maxN];
int C[maxA], D[maxA], J[maxA], K[maxA];

int f[H+1][H+1][2];
int seg, ans;

inline void updMin(int& a, int b) {
    if(a == -1 || (b != -1 && a > b)) a = b;
}

int main() {
#ifdef RS16
    //freopen("inp.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
#endif // RS16

    int T; scanf("%d", &T);
    for(int t = 1; t <= T; ++t) {
        printf("Case #%d: ", t);

        memset(A, -1, sizeof(A));
        scanf("%d%d", &AC, &AJ);
        for(int i = 1; i <= AC; ++i) {
            scanf("%d%d", C+i, D+i);
            for(int j = ++C[i]; j <= D[i]; ++j) A[j] = 0;
        }
        for(int i = 1; i <= AJ; ++i) {
            scanf("%d%d", J+i, K+i);
            for(int j = ++J[i]; j <= K[i]; ++j) A[j] = 1;
        }

        memset(f, -1, sizeof(f));
        f[1][0][0] = f[0][1][1] = 1;
        for(int tot = 1; tot < N; ++tot) {
            for(int cam = 0, jam; cam <= tot; ++cam) {
                jam = tot-cam;
                if(cam <= H && jam <= H) {
                    if(~f[cam][jam][0]) {
                        if(cam < H && A[tot+1] != 1) updMin(f[cam+1][jam][0], f[cam][jam][0]);
                        if(jam < H && A[tot+1] != 0) updMin(f[cam][jam+1][1], f[cam][jam][0]+1);
                    }
                    if(~f[cam][jam][1]) {
                        if(cam < H && A[tot+1] != 1) updMin(f[cam+1][jam][0], f[cam][jam][1]+1);
                        if(jam < H && A[tot+1] != 0) updMin(f[cam][jam+1][1], f[cam][jam][1]);
                    }
                }
                //++tot;
                //--tot;
            }
            //++tot;
            //--tot;
        }

        seg = -1; updMin(seg, f[H][H][0]); updMin(seg, f[H][H][1]);
        ans = (seg & 1) ? seg-1 : seg;
        printf("%d\n", ans);
    }
}
