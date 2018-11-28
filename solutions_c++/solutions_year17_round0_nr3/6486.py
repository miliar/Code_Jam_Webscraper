#include <stdio.h>
#include <stdlib.h>
#include <vector>

using namespace std;

int T, N, K;
int y,z;

vector <int> LS;
vector <int> RS;
vector <bool> ocupado;

int LEFT(int index){
    int cont = 0;
    while( ocupado[index-1] == false ){
        cont++;
        index--;
    }
    return cont;
}

int RIGHT(int index){
    int cont = 0;
    while( ocupado[index+1] == false ){
        cont++;
        index++;
    }
    return cont;
}

int main(){

    scanf("%d", &T);

    for(int caso = 1; caso <= T; caso++){

        scanf("%d %d", &N, &K);

        LS.resize(N+2);
        RS.resize(N+2);

        for(int i = 1; i<= N; i++){
            LS[i] = i-1;
            RS[i] = N-i;
            //printf("LR[%d] = (%d,%d)\n", i, LS[i], RS[i]);

        }

        ocupado.assign(N+2, false);
        ocupado[0] = true;
        ocupado[N+1] = true;

        for(int j = 1; j <= K; j++){

            int index = -1;
            for(int i = 1; i <= N; i++){

                if(ocupado[i]) continue;

                if(index==-1){
                    index = i;
                }else{
                    int min_i     = min(LS[i],RS[i]);
                    int min_index = min(LS[index],RS[index]);
                    if(  min_i > min_index ){
                        index = i;
                    }else if( min_i == min_index ){
                        int max_i = max(LS[i],RS[i]);
                        int max_index = max(LS[index],RS[index]);
                        if( max_i > max_index ){
                            index = i;
                        }
                    }
                }
            }

            //printf("index %d LS %d RS %d\n", index, LS[index], RS[index]);

            ocupado[index] = true;

            y = max( LS[index], RS[index] );
            z = min( LS[index], RS[index] );

            for(int i = 1; i <= N; i++){
                if( i <= index ){
                    RS[i] = RIGHT(i);
                }

                if( i >= index){
                    LS[i] = LEFT(i);
                }
            }

        }

        printf("Case #%d: %d %d\n", caso, y, z);





    }

}
