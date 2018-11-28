#include <cstdio>
#include <algorithm>
#include <queue>
using namespace std;

int P[1009];
int B[1009];
int A[1009][1009];

int K[1009];
int L[1009];

int main(){
    freopen("B-large (3).in", "r", stdin);
    freopen("Blargeout2.out","w",stdout);
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++){
        int N, C, M;
        scanf("%d %d %d", &N, &C, &M);
        for (int i = 1; i <= N; i++){
            K[i] = 0;
            /*for (int j = 1; j <= C; j++){
                A[i][j] = 0;
            }*/
        }
        for (int i = 1; i <= C; i++){
            L[i] = 0;
        }
        for (int i = 0; i < M; i++){
            scanf("%d %d", &P[i], &B[i]);
            K[P[i]]++;
            L[B[i]]++;
            A[P[i]][B[i]]++;
        }
        int ansy = 0;
        int total = 0;
        for (int i = 1; i <= N; i++){
            total += K[i];
            ansy = max((total+i-1)/i,ansy);
        }
        for (int i = 1; i <= C; i++){
            ansy = max(ansy,L[i]);
        }
        printf("Case #%d: %d ", t, ansy);
        int ansz = 0;
        for (int i = 1; i <= N; i++){
            ansz += max(0,K[i]-ansy);
        }
        printf("%d\n", ansz);
    }
}
