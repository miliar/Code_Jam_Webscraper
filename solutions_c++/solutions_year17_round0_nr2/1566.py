#include <bits/stdc++.h>
using namespace std;
int danum[20];
int arns[20];
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out", "w", stdout);
    int teesee, lmeow, curnum, ssf;
    long long en;
    scanf("%d", &teesee);
    for(int hnc=0; hnc<teesee; hnc++){
        memset(arns, 0, sizeof(arns));
        ssf = 0;
        scanf("%lld", &en);
        lmeow = 0;
        while(en>0){
            danum[lmeow] = en%10;
            en/=10;
            lmeow++;
        }
        curnum=danum[lmeow-1];
        arns[0] = curnum;
        for(int i=lmeow-2; i>=0; i--){
    //        printf("curnum: %d\n", curnum);
    if(ssf==1){
               // printf("Operation 3\n");
                arns[lmeow-1-i] = 9;
            }
            if(danum[i]<curnum && ssf==0){
            //        printf("Operation 1\n");
                int k = lmeow-2-i;
                arns[lmeow-1-i] = 9;
                for(int j=k; j>=0; j--){
                    arns[j]-=1;
                    if(j==0){
                        break;
                    }
                    if(arns[j]<arns[j-1]){
                        arns[j] = 9;
                    }else{
                        break;
                    }
                }
                ssf = 1;
            }
            if(danum[i]>=curnum && ssf == 0){
          //      printf("Operation 2\n");
                curnum = danum[i];
                arns[lmeow-1-i] = curnum;
            }
        }
        printf("Case #%d: ", hnc+1);
        int countah = 0;
        int np = 1;
     howisthissoannoying:   while(arns[countah]>0){
            printf("%d", arns[countah]);
            countah++;
            np = 0;
        }
        if(np==1){
            countah++;
            goto howisthissoannoying;
        }
        printf("\n");
    }
}
