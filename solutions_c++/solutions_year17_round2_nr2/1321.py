#include <bits/stdc++.h>
using namespace std;
int meh[10];
// shld be 6 but just inkays
// 1  12 2  23 3  13
// 0  1  2  3  4  5
int arns[1050];
int main(){
    freopen("B-small-attempt1 (1).in","r",stdin);
    freopen("B-small-attempt0.txt","w",stdout);
    int teesee, n, prev, wtf, magx, zecond;
    scanf("%d", &teesee);
    for(int asd=0; asd<teesee; asd++){
        scanf("%d", &n);
        prev = -1;
        wtf = -1;
        magx = 2;
        zecond = -1;
        memset(arns, 0 ,sizeof(arns));
        for(int i=0; i<6; i++){scanf("%d", &meh[i]);}
        if(meh[0]<meh[3] || meh[2]<meh[5] || meh[4]<meh[1]){
            printf("Case #%d: IMPOSSIBLE\n", asd+1);continue;
        }
        if(meh[0] - meh[3]> meh[2]-meh[5] && meh[0] - meh[3] > meh[4]-meh[1]){
                swap(meh[0], meh[2]);
                swap(meh[3], meh[5]);
                magx = 0;
        }
        if(meh[4] - meh[1]> meh[2]-meh[5] && meh[0] - meh[3] <= meh[4]-meh[1]){
                swap(meh[4], meh[2]);
                swap(meh[1], meh[5]);
                magx = 4;
        }
        if(meh[0] - meh[3] > meh[4]-meh[1]){
                zecond = 0;
            swap(meh[0], meh[4]);
            swap(meh[3], meh[1]);
        }else{
            zecond = 4;
        }
        for(int i=0; i<n; i++){
            if(i>0 && arns[n] == 0){arns[n] = arns[0];}
            if(meh[1]>0){
                if(prev != 1){
                    arns[i] = 1;
                    meh[1]--;
                    prev = 1;
                    continue;
                }
                    arns[i] = 1;
                    arns[i+1] = 4;
                    meh[1]--;
                    meh[4]--;
                    i++;
                    prev = 1;
                    continue;
                }
            if(meh[5]>0){
                if(prev != 2){
                    arns[i] = 2;
                    meh[2]--;
                    prev = 2;
                    continue;
                }
                    arns[i] = 5;
                    arns[i+1] = 2;
                    meh[5]--;
                    meh[2]--;
                    i++;
                    prev = 2;
                    continue;
                }
            if(meh[3]>0){
                if(prev != 0){
                    arns[i] = 0;
                    meh[0]--;
                    prev = 0;
                    continue;
                }
                    arns[i] = 3;
                    arns[i+1] = 0;
                    meh[3]--;
                    meh[0]--;
                    i++;
                    prev = 0;
                    continue;
                }
            wtf = i;
            break;
        }
        if(wtf == 0){arns[0] = 4;meh[4]--;wtf = 1;}
        while(meh[2]>0){
            arns[wtf] = 2;
            meh[2]--;
            wtf++;
            if(meh[2]==0){
            break;
            }

            if((meh[4]>=meh[0] || meh[0]<=0) && meh[4]>0){
                arns[wtf] =4;
          //      printf("Set %d to 4\n", wtf+1);
                meh[4]--;
                wtf++;
            }else{
                arns[wtf] = 0;
                meh[0]--;
                wtf++;
        }
         //       printf("%d %d\n", meh[4], meh[0]);
        }
        if(meh[4]>meh[0]){
            printf("Case #%d: IMPOSSIBLE\n", asd+1);continue;
        }
        if(meh[4] == meh[0]){
            arns[wtf] = 4;
        }else{
        arns[wtf] = 0;
        }
        wtf++;
        for(int i=wtf; i<n; i++){
            if(arns[i-1] == 0){
                arns[i] = 4;
            }else{
                arns[i] = 0;
            }
        }
        arns[n] = arns[0];
    /*    for(int i=0; i<n-1; i++){
            if(arns[i] == arns[i+1] || (arns[i] == 0 && arns[i+1] == 3) || (arns[i] == 2 && arns[i+1] == 5)||(arns[i] == 4 && arns[i+1] == 1)||(arns[i] == 3 && arns[i+1] == 0)||(arns[i] == 5 && arns[i+1] == 2)||(arns[i] == 1 && arns[i+1] == 4)){
                printf("Case #%d: IMPOSSIBLE\n", asd+1);
                continue;
            }
        }*/
        printf("Case #%d: ", asd+1);
        if(zecond == 0){
        for(int i=0; i<n; i++){
                if(arns[i] == 0){
                    arns[i] = 4;
                }
                else{
                    if(arns[i] == 4){arns[i] = 0;}
                }
            if(arns[i] == 3){arns[i] = 1;}else{if(arns[i] == 1){arns[i] = 3;}}
            }
        }
        if(magx!=2){
            for(int i=0; i<n; i++){
                if(arns[i] == magx){arns[i] = 2;}else{
                    if(arns[i] == 2){arns[i] = magx;}
                }
                if(arns[i] == (magx+3)%6){arns[i] = 5;}else{if(arns[i]==5){arns[i] = (magx+3)%6;}}
            }
        }
        for(int i=0; i<n; i++){
            if(arns[i] == 0){printf("R");}
            if(arns[i] == 1){printf("O");}
            if(arns[i] == 2){printf("Y");}
            if(arns[i] == 3){printf("G");}
            if(arns[i] == 4){printf("B");}
            if(arns[i] == 5){printf("V");}
        }
        printf("\n");
    }
}
