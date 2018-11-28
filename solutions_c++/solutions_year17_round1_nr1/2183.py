#include <cstdio>
#include <cstring>
int nTest;
int cutH[55], cutW[55];
char a[55][55];
char findSeed(int eR, int eC, int h, int w){
    for (int i = eR; eR - i + 1 <= h; i--){
        for (int j = eC; eC - j + 1 <= w; j--){
            if (a[i][j] != '?') return a[i][j];
        }
    }
    return '?';
}
void fillCake(int eR, int eC, int h, int w, char seed){
    for (int i = eR; eR - i + 1 <= h; i--){
        for (int j = eC; eC - j + 1 <= w; j--){
            a[i][j] = seed;
        }
    }
}
int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    scanf("%d", &nTest);
    for (int test = 1; test <= nTest; test++){
        // printf("\n");
        printf("Case #%d:", test);
        memset(cutH, 0, sizeof(cutH));
        memset(cutW, 0, sizeof(cutW));

        int n, m;
        scanf("%d %d\n", &n, &m);
        // printf("\n");
        for (int i = 0; i < n; i++){
            scanf("%s\n", a[i]);
            // printf("%s\n", a[i]);
        }
        
        for (int i = 0; i < n; i++){
            int numInit = 0;
            for (int j = 0; j < m; j++){
                if (a[i][j] != '?') {
                    numInit++;
                    if (numInit > 1){
                        cutW[j - 1] = 1;
                    }
                }
            }
            if (numInit > 0){
                cutH[i] = 1;
            }
        }
        cutH[n - 1] = 1;
        cutW[m - 1] = 1;

        for (int i = 0; i < n; i++){
            char lastSeed = '?';
            for (int j = 0; j < m; j++){
                if (cutH[i] && cutW[j]){
                    int W, H;
                    W = H = 1;
                    for (int k = i - 1; k >= 0; k--){
                        if (cutH[k]) break;
                        H++;
                    }
                    for (int k = j - 1; k >= 0; k--){
                        if (cutW[k]) break;
                        W++;
                    }
                    char seed = findSeed(i, j, H, W);
                    // printf("%d %d %c\n", i, j, seed);
                    if (seed == '?'){
                        if (lastSeed == '?'){
                            //dosth
                        } else {
                            seed = lastSeed;
                            fillCake(i, j, H, W, seed);
                        }
                    } else {
                        fillCake(i, j, H, W, seed);
                    }
                    lastSeed = seed;
                }
            }
        }
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                if (a[i][j] != '?'){
                    for (int k = j - 1; k >= 0; k--){
                        if (a[i][k] != '?') break;
                        else {
                            a[i][k] = a[i][j];
                        }
                    }
                }
            }
        }
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                if (a[i][j] == '?'){
                    if (i > 0 && a[i - 1][j] != '?'){
                        a[i][j] = a[i - 1][j];
                    } else {
                        //
                    }
                } else {
                    
                }
            }
        }
        

        printf("\n");
        for (int i = 0; i < n; i++){
            printf("%s\n", a[i]);
        }
    }
}