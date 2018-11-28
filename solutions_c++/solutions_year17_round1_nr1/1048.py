#include<cstdio>
#include<cstring>
using namespace std;
char cakemap[26][26];
bool hasletter[25];
int main(){
    int numcases; scanf("%d", &numcases);
    for(int ccase = 0; ccase < numcases; ccase++){
        int ylen, xlen; scanf("%d%d", &ylen, &xlen);
        for(int i = 0; i < ylen; i++){
            scanf("%s", cakemap[i]);
            bool chasletter = false;
            for(int i2 = 0; i2 < xlen; i2++){
                if(cakemap[i][i2] != '?'){
                    chasletter = true;
                    break;
                }
            }
            hasletter[i] = chasletter;
            char cletter = '?';
            for(int i2 = 0; i2 < xlen; i2++){
                if(cakemap[i][i2] == '?')
                    cakemap[i][i2] = cletter;
                else
                    cletter = cakemap[i][i2];
            }
            cletter = '?';
            for(int i2 = xlen - 1; i2 >= 0; i2--){
                if(cakemap[i][i2] == '?')
                    cakemap[i][i2] = cletter;
                else
                    cletter = cakemap[i][i2];
            }
        }
        for(int i = 0; i < ylen; i++){
            if(!hasletter[i] && i > 0){
                for(int i2 = 0; i2 < xlen; i2++){
                    cakemap[i][i2] = cakemap[i-1][i2];
                }
            }
        }
        for(int i = ylen - 1; i >= 0; i--){
            if(!hasletter[i] && i < ylen - 1){
                for(int i2 = 0; i2 < xlen; i2++){
                    cakemap[i][i2] = cakemap[i+1][i2];
                }
            }
        }
        printf("Case #%d:\n", ccase + 1);
        for(int i = 0; i < ylen; i++){
            printf("%s\n", cakemap[i]);
        }
    }
    return 0;
}
