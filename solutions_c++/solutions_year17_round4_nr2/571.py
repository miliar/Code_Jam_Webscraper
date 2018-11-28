#include <cstdio>
#include <algorithm>
using namespace std;

int REQ[1000][1000]; // requested [cust][seat] cnt
int N; // seats nr
int C; // customers
int M; // tickets total
int R; // rides
int CT[1000];


void clear0() {
    for (int c=0; c<C; c++) {
        for (int w=0; w<N; w++)
            REQ[c][w] = 0;
        CT[c]=0;
    }
}

int main() {
    
    int T; scanf("%d", &T);
    for (int t=1; t<=T; t++) {
        scanf("%d%d%d", &N, &C, &M);
        clear0();
        
        int m = 0;
        for (int i=0; i<M; i++) {
            int p, b; scanf("%d%d", &p, &b); p--, b--;
            REQ[b][p]++;
            CT[b]++;
            m = max(m, REQ[b][p]);
            m = max(m, CT[b]);
        }
        
        for (int R=m; R<=1000; R++) {
            
            int spare = 0;
            int P = 0;
            for (int w=0; w<N; w++) {
                int needed = 0;
                for (int c=0; c<C; c++)
                    needed += REQ[c][w];
                if (spare + R < needed)
                    goto increase_r;
                
                if (needed <= R) {
                    spare += R-needed;
                }
                else {
                    P += (needed-R);
                    spare -= (needed-R);
                }
            }
            
            printf("Case #%d: %d %d\n", t, R, P);
            break;
            
            increase_r: {}
        }
    }
    
    return 0;
}
