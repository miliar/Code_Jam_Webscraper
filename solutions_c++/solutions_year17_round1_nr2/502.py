#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
const int SIZE = 55;
typedef pair<int,int> p;
const int MAXQ = 1000000;

int R[SIZE], tr[SIZE], q[SIZE][SIZE];
//bool used[SIZE][SIZE];
int pos[SIZE];
int N, P;

int main() {
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int T;
    scanf("%d",&T);
    int cs = 1;
    while(T--) {
        //memset(used,0,sizeof(used));
        int res =0;
        scanf("%d%d",&N,&P);
        for(int i = 1; i <= N; i++) {
            scanf("%d",&R[i]);
            pos[i] = 1;
        }
        for(int i = 1; i <= N; i++) {
            for(int j = 1; j <= P; j++) {
                scanf("%d",&q[i][j]);
            }
            sort(q[i]+1,q[i]+1+P);
        }
        int GG = 0;
        for(int i = 1;!GG;i++) {
            for(int j = 1; j <= N; j++) {
                tr[j] = R[j] * i;
                if(0.9*tr[j] > MAXQ) break;
            }
            int gg = 0;
            for(int j = 1; j <= N; j++) {
                double l = 0.9*tr[j], r = 1.1*tr[j];
                //printf("%.6f %.6f\n",l,r);
                while(true) {
                    if(pos[j] > P) {
                        gg = 1;
                        GG = 1;
                        break;
                    }
                    if(q[j][pos[j]] > r) {
                        gg = 1;
                        break;
                    }
                    else if(q[j][pos[j]] >= l && q[j][pos[j]] <= r) {
                        break;
                    }
                    else {
                        pos[j]++;
                    }
                }
            }
            if(!gg) {
                res++;
                for(int j = 1; j <= N; j++) {
                    pos[j]++;
                }
                i--;
            }
        }
        printf("Case #%d: %d\n",cs++,res);
    }
    return 0;
}

