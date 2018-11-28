#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("out.txt", "w", stdout);
    int casos, filas, columnas;
    int casoActual;
    bool algoEnFila, llenarTodo;
    int i, j, k, l;
    char ultimoChar;
    scanf("%d", &casos);
    for(casoActual=1; casoActual<=casos; casoActual++){
        scanf("%d %d", &filas, &columnas);
        char matriz[filas][columnas];
        ultimoChar=0;
        for(i=0; i<filas; i++){
            cin.ignore();
            llenarTodo = false;
            algoEnFila = false;
            for(j=0; j<columnas; j++){
                scanf("%c", &matriz[i][j]);
                if(matriz[i][j]!='?'){
                    if(ultimoChar==0){
                        llenarTodo = true;
                    }
                    ultimoChar = matriz[i][j];
                    if(!algoEnFila){
                        algoEnFila=true;
                        for(k=0; k<j; k++){
                            matriz[i][k]=ultimoChar;
                        }
                    }
                } else if(ultimoChar!=0){
                    matriz[i][j]=ultimoChar;
                }
            }
            if(!algoEnFila&&!llenarTodo){
                for(k=0; k<columnas; k++){
                    matriz[i][k]=matriz[i-1][k];
                }
            } else if(llenarTodo){
                for(k=0; k<i; k++){
                    for(l=0; l<columnas; l++){
                        matriz[k][l]=matriz[i][l];
                    }
                }
            }
        }
        printf("case #%d:\n", casoActual);
        for(i=0; i<filas; i++){
            for(j=0; j<columnas; j++){
                printf("%c", matriz[i][j]);
            }
            printf("\n");
        }
    }
    return 0;
}
