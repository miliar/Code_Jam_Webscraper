#include <stdio.h>
#include <iostream>

using namespace std;

int getMaxServe(int re, int in){

    int s = in/(re*0.9);
    s++;
    while (s*re*90/100 > in) {
        s--;
    }
    return s;
}

int getMinServe(int re, int in){

    int s = in/(re*1.1);
    while (s*re*110/100 < in) {
        s++;
    }
    return s;
}

int main(){
    int T;
    cin >> T;

    for (int t=  1 ; t<= T; t++){

        int N,P;

        cin >> N;
        cin >> P;

        int rec[60];

        for (int i = 0 ; i < N ; i++){

            cin >> rec[i];
        }

        int ing[60][60];
        for (int i = 0 ; i < N ; i++){

            for (int j = 0 ; j < P ; j++){
                cin >> ing[i][j];
            }
        }

        for (int i = 0 ; i < N ; i++){

            for (int j = 0 ; j < P ; j++){
                for (int k = 1 ; k < P; k++){

                    if (ing[i][k-1] > ing[i][k]){
                        int tmp = ing[i][k];
                        ing[i][k] = ing[i][k-1];
                        ing[i][k-1] = tmp;
                    }
                }

            }
        }
/*
        printf("Case #%d:\n",t);
        for (int i = 0; i  < N ; i++){
            for (int j = 0 ; j < P ; j++){
                printf("%d/%d ",getMinServe(rec[i],ing[i][j]),getMaxServe(rec[i],ing[i][j]));
            }
            printf("\n");
        }*/

        int I[60] = {};
        int ans = 0;

        while (1){

            bool isstop = false;

            for (int i = 0 ;i  < N ; i++){
                if (I[i] >= P){
                    isstop = true;
                    break;
                }
            }

            if (isstop){
                break;
            }

            int minMax=-1,maxMin= - 1,minId;

            for (int i = 0 ;i  < N ; i++){
                int tmpMax = getMaxServe(rec[i],ing[i][I[i]]);
                int tmpMin = getMinServe(rec[i],ing[i][I[i]]);
                while (tmpMin > tmpMax){
                    I[i]++;
                    if (I[i] >= P){
                        isstop = true;
                        break;
                    }
                    tmpMax = getMaxServe(rec[i],ing[i][I[i]]);
                    tmpMin = getMinServe(rec[i],ing[i][I[i]]);
                }

                if (minMax == -1 || minMax > tmpMax) {
                    minMax = tmpMax;
                    minId = i;
                }
                if (maxMin == -1 || maxMin < tmpMin){
                    maxMin = tmpMin;
                }
            }
            if (isstop){
                break;
            }

            if (maxMin <= minMax){
                ans++;
                for (int i = 0 ; i< N ;i++){
                    I[i]++;
                }
            } else {
                I[minId]++;
            }
        }

        printf("Case #%d: %d\n",t,ans);
    }
}
