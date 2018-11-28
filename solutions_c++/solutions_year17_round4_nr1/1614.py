#include <stdio.h>

int cnt[5];
int arr[105];

int main(){
    int T;
    scanf("%d", &T);
    for(int tc=1; tc<=T; tc++){
        int N, P;
        scanf("%d%d", &N, &P);
        for(int i=0; i<5; i++) cnt[i] = 0;
        for(int i=0; i<N; i++){
            int x;
            scanf("%d", &x);
            cnt[x%P]++;
        }
        printf("Case #%d: ", tc);
        if(P == 2){
            printf("%d\n", cnt[0]+(cnt[1]+1)/2);
        } else if(P == 3){
            int res = cnt[0];
            int ptr = 0;
            int rem = 0;
            while(1){
                if(cnt[1] == 0 && cnt[2] == 0) break;
                if(cnt[1]) arr[ptr++] = 1, cnt[1]--;
                if(cnt[2]) arr[ptr++] = 2, cnt[2]--;
            }
            for(int i=0; i<ptr; i++){
                if(!rem) res++;
                rem = (rem+P-arr[i])%3;
            }
            printf("%d\n", res);
        }
    }
    return 0;
}