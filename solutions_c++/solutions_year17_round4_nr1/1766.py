#include <cstdio>
#include <string.h>
#include <algorithm>

int arr[4];
int main(){
    int T;
    scanf("%d",&T);
    for(int tc = 1; tc <= T; tc++){
        printf("Case #%d: ",tc);
        int N, P;
        arr[0] = arr[1] = arr[2] = arr[3] = 0;
        scanf("%d%d",&N,&P);
        for(int i =0 ; i< N; i++){
            int v;
            scanf("%d",&v);
            arr[v%P]++;
        }
        if(P == 2) {
            printf("%d", arr[0] + (arr[1]+1)/2);
        }
        if(P == 3){
            int mval = std::min(arr[1],arr[2]);
            printf("%d", arr[0] + mval + (arr[1]-mval+2)/3 + (arr[2]-mval+2)/3);
        }
        printf("\n");

    }
}
