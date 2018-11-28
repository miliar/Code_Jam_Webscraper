#include <cstdio>
#include <algorithm>
using namespace std;


int C[4];
int N, P;

int main() {
    int T; scanf("%d", &T);
    for (int t=1; t<=T; t++) {
        scanf("%d%d", &N, &P);
        C[0]=C[1]=C[2]=C[3]=0;
        for (int i=0; i<N; i++) {
            int x; scanf("%d", &x);
            C[x%P]++;
        }
        
        int result = C[0];
        if (P==2) {
            result += (C[1]+1)/2;
        }
        else if (P==3) {
            int a = min(C[1], C[2]);
            result += a;
            C[1] -= a; C[2] -= a;
            result += (C[1]+2) / 3;
            result += (C[2]+2) / 3;
        }
        else if (P==4) {
            int a = C[2]/2;
            result += a;
            C[2] -= 2*a;
            
            int b = min(C[1], C[3]);
            result += b;
            C[1] -= b; C[3] -= b;
            
            if (C[2] && C[1]>=2)
                C[2]--, C[1]-=2, result++;
            if (C[2] && C[3]>=2)
                C[2]--, C[3]-=2, result++;
            if (C[2]==1) result++;
            else {
                result += (C[1]+3) / 4;
                result += (C[3]+3) / 4;
            }
        }
        
        printf("Case #%d: %d\n", t, result);
    }
    return 0;
}
