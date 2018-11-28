#include<cstdio>
typedef unsigned long long int lli;
struct seg { lli v, n; };

int main (){
    int T;
    scanf("%d", &T);
    for (int i=1;i<=T;i++){
        lli n, k;
        scanf("%llu%llu", &n,&k);
        seg s[2]{{n-1,0},{n,1}};
        lli cnt = 0;
        while ( ((cnt+1)<<1)-1 < k ){
            seg tmp;
            if (s[1].v % 2){
                tmp = {s[1].v/2, s[1].n*2 + s[0].n};
                s[0] = {s[1].v/2-1, s[0].n};
            }
            else {
                tmp = {s[1].v/2, s[1].n};
                s[0] = {s[1].v/2-1, s[1].n + s[0].n*2};
            }
            s[1] = tmp;
            cnt = ((cnt+1)<<1)-1;
        }
        printf("Case #%d: ", i);
        if (s[1].n < k-cnt){
            if (s[0].v % 2) printf("%llu %llu\n", s[0].v/2, s[0].v/2);
            else printf("%llu %llu\n", s[0].v/2, s[0].v/2-1);
        }
        else {
            if (s[1].v % 2) printf("%llu %llu\n", s[1].v/2, s[1].v/2);
            else printf("%llu %llu\n", s[1].v/2, s[1].v/2-1);
        }
    }
}
