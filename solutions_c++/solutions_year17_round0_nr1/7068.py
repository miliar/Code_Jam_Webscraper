#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int main()
{
    //freopen("A-large.in", "r", stdin);
    freopen("Out.out", "w", stdout);
    int casos;
    int i, j, k;
    char linea[1005];
    int numero, tamanio, volteos;
    scanf("%d", &casos);
    for(i=1; i<=casos; i++){
        scanf("%s %d", linea, &numero);
        tamanio = strlen(linea);
        for(j=0, volteos=0; j<tamanio; j++){
            if(linea[j]=='-'){
                volteos++;
                if((j+numero)<=tamanio){
                    for(k=0; k<numero; k++){
                        if(linea[j+k]=='-'){
                            linea[j+k]='+';
                        } else {
                            linea[j+k]='-';
                        }
                    }
                } else {
                    volteos=-1;
                    break;
                }
            }
        }
        if(volteos>=0){
            printf("Case #%d: %d\n", i, volteos);
        }
        else {
            printf("Case #%d: IMPOSSIBLE\n", i);
        }
    }
    return 0;
}
