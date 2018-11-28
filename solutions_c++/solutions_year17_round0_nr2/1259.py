#include<cstdio>

int main() {
    int T;
    char n[1024];
    scanf("%d", &T);
    for(int ca=1; ca<=T; ca++) {
        scanf("%s", n);
        printf("Case #%d: ", ca);
        int i = 0, j = 0;
        while(n[i+j]) {
            if(!n[i+j+1]){
                i += j + 1;
                break;
            }
            if(n[i+j] > n[i+j+1]) 
                break;
            else if(n[i+j] == n[i+j+1])
                j++;
            else {
                i += j + 1; 
                j = 0;
            }
        }
        for(int k=0; n[k]; k++) {
            if(k > i)
                n[k] = '9';
            else if(k == i) {
                n[k]--;
                if(!k && n[k] == '0') continue;
            }
            printf("%c", n[k]);
        }
        puts("");
    }
    return 0;
}
