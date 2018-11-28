#include <cstdio>
char arr[30][30];
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    int r,c;
    for(int i = 1; i <= t; i++){
        scanf("%d%d",&r,&c);
        scanf("%s",arr[0]);
        for(int j = 1; j < c; j++){
            if(arr[0][j] == '?'){
                arr[0][j] = arr[0][j-1];
            }
        }
        for(int j = c-2; j >= 0; j--){
            if(arr[0][j] == '?'){
                arr[0][j] = arr[0][j+1];
            }
        }
        for(int j = 1; j < r; j++){
            scanf("%s",arr[j]);
            for(int k = 1; k < c; k++){
                if(arr[j][k] == '?'){
                    arr[j][k] = arr[j][k-1];
                }
            }
            for(int k = c-2; k >= 0; k--){
                if(arr[j][k] == '?'){
                    arr[j][k] = arr[j][k+1];
                }
            }
            for(int k = 0; k < c; k++){
                if(arr[j][k] == '?'){
                    arr[j][k] = arr[j-1][k];
                }
            }
        }
        for(int j = r-2; j >= 0; j--){
            for(int k = 0; k < c; k++){
                if(arr[j][k] == '?'){
                    arr[j][k] = arr[j+1][k];
                }
            }
        }
        printf("Case #%d:\n",i);
        for(int j = 0; j < r; j++){
            printf("%s\n",arr[j]);
        }
    }
    return 0;
}
