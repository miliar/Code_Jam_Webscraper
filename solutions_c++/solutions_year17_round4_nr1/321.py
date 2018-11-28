#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

int c[4];

int main(){
    int T;
    scanf("%d", &T);
    for(int kase=1; kase<=T; kase++){
        int n, p;
        scanf("%d%d", &n, &p);
        memset(c, 0, sizeof(c));
        while(n--){
            int t;
            scanf("%d", &t);
            c[t%p]++;
        }
        printf("Case #%d: ", kase);
        if(p == 2){
            printf("%d\n", c[0]+(c[1]+1)/2);
            continue;
        }
        if(p == 3){
            if(c[1] > c[2]) swap(c[1], c[2]);
            c[2] -= c[1];
            printf("%d\n", c[0]+c[1]+(c[2]+2)/3);
            continue;
        }
        if(c[1] > c[3]) swap(c[1], c[3]);
        c[3] -= c[1];
        if(c[2] % 2){
            printf("%d\n", c[0]+(c[2]+1)/2+c[1]+(c[3]+1)/4);
        }else{
            printf("%d\n", c[0]+c[2]/2+c[1]+(c[3]+3)/4);
        }
    }
    return 0;
}
