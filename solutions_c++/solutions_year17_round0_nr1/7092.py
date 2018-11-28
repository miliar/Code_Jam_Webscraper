#include <stdio.h>
#include <string.h>

int main(){
    int inst,n, i,j,count,siz, deuBom, k;
    
    scanf("%d", &inst);
    
    for (k = 0; k< inst; k++ ){
        char vet[12345] = {0};
        scanf("%s", vet);
        scanf("%d", &siz);

        n = strlen(vet);
        count = 0;
        for ( i = 0; i <= n - siz; i++){
            if ( vet[i] == '-'){
                count ++;
                for ( j = 0; j < siz; j++)
                    vet[i+j] = vet[i+j]=='-'? '+': '-';
            }
        }
        
        deuBom = 1;
        for ( i = n-1; i >= 0 ; i--){
            if ( vet[i] == '-'){
                deuBom = 0;
                break;
            }
        }
        
        if (deuBom){
            printf("Case #%d: %d\n",k+1,count);
        }else{
            printf("Case #%d: IMPOSSIBLE\n",k+1);
        }

    }
    
}
