#include <cstdlib>
#include <cstdio>

using namespace std;

int main(){
    int k; scanf("%d", &k);
    for(int case_num = 1; case_num <= k;case_num++){
        char str[2000]; int k;
        int b[2000];
        int len;
        scanf("%s %d", str, &k);
        for(len = 0;str[len];len++)
            b[len] = (str[len] == '-');
        
        int step = 0;
        for(int i = 0;i + k-1 < len;i++){
            if(b[i]){
                step++;
                for(int lx = i;lx < i+k;lx++)
                    b[lx] ^= 1;
            }
        }

        bool unsolve = false;
        for(int lx = 0;lx < len and not unsolve;lx++)
            unsolve = b[lx];
    
        printf("Case #%d: ", case_num);
        if(unsolve)
            puts("IMPOSSIBLE");
        else
            printf("%d\n", step);
    }
    return 0;
}
