#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("Out.out", "w", stdout);
    int casos, i, j;
    char numeros[22];
    char mayor;
    int inicio;
    int tamanio;
    scanf("%d", &casos);
    for(i=1; i<=casos; i++){
        scanf("%s", numeros);
        tamanio = strlen(numeros);
        mayor=numeros[0];
        inicio = 0;
        for(j=1; j<tamanio; j++){
            if(mayor>numeros[j]){
                break;
            } else if(mayor<numeros[j]){
                mayor=numeros[j];
                inicio=j;
            }
        }
        if(j<tamanio){
           numeros[inicio]-=1;
           inicio++;
           while(inicio<tamanio){
                numeros[inicio]='9';
                inicio++;
           }
           j=0;
           while(numeros[j]=='0'){
                j++;
           }
        }
        else{
            j=0;
        }
        printf("Case #%d: %s\n", i, numeros+j);
    }
    return 0;
}
