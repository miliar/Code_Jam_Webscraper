#include <iostream>
#include <cstdio>
#include <algorithm>
#define pii pair<int,int>
#define F first
#define S second
#define mp make_pair

using namespace std;

char C[6] = {'R','O','Y','G','B','V'};
int T;
int N,col[6];
int ans[1005];

int main(){
    freopen("data2.in","r",stdin);
    freopen("data2.out","w",stdout);
    scanf("%d",&T);
    for (int z = 1; z <= T; z++){
        scanf("%d",&N);
        for (int i = 0; i < 6; i++) scanf("%d",&col[i]);
        bool flag = 0, d = 0;
        for (int i = 1; i < 6 && !flag && !d; i+=2){
            if (col[(i+3)%6] < col[i]) flag = 1;
            else if (col[(i+3)%6] == col[i]){
                if (0 < col[(i+3)%6]+col[i] && col[(i+3)%6]+col[i] < N) flag = 1;
                else if (col[(i+3)%6]+col[i] == N){
                    for (int j = 0; j < N; j++){
                        if (j%2) ans[j] = i;
                        else ans[j] = (i+3)%6;
                    }
                    d = 1;
                }
            }
            col[(i+3)%6] -= col[i];
        }
        if (flag) goto impossible;
        if (!d){
            pii ar[3] = {mp(col[0],0),mp(col[2],2),mp(col[4],4)};
            sort(ar,ar+3); reverse(ar,ar+3);
            int triplets = ar[2].F;
            int pairs = ar[1].F-triplets;
            int rem = ar[0].F-triplets-pairs;
            if (rem > triplets) flag = 1;
            bool f[3] = {0,0,0};
            for (int j = 0; j < N;){
                if (ar[0].F > 0){
                    ar[0].F--;
                    ans[j++] = ar[0].S;
                    if (!f[0]){
                        f[0] = 1;
                        int o = (ar[0].S+3)%6;
                        for(;col[o] > 0 && j < N;){
                            ans[j++] = o, ans[j++] = ar[0].S;
                            col[o]--;
                        }
                    }
                }
                if (ar[1].F > 0){
                    ar[1].F--;
                    ans[j++] = ar[1].S;
                    if (!f[1]){
                        f[1] = 1;
                        int o = (ar[1].S+3)%6;
                        for(;col[o] > 0 && j < N;){
                            ans[j++] = o, ans[j++] = ar[1].S;
                            col[o]--;
                        }
                    }
                }
                if (rem > 0 && ar[0].F > 0){
                    ar[0].F--;
                    rem--;
                    ans[j++] = ar[0].S;
                }
                if (ar[2].F > 0){
                    ar[2].F--;
                    ans[j++] = ar[2].S;
                    if (!f[2]){
                        f[2] = 1;
                        int o = (ar[2].S+3)%6;
                        for(;col[o] > 0 && j < N;){
                            ans[j++] = o, ans[j++] = ar[2].S;
                            col[o]--;
                        }
                    }
                }
            }
        }
        if (flag || ans[0] == ans[N-1]) goto impossible;
        printf("Case #%d: ",z);
        for (int i = 0; i < N; i++){
            printf("%c",C[ans[i]]);
        }
        printf("\n");
        continue;
    impossible:
        printf("Case #%d: IMPOSSIBLE\n",z);
    }
    return 0;
}
