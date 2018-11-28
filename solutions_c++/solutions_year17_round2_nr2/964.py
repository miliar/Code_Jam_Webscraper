#include <bits/stdc++.h>

using namespace std;
typedef unsigned long long ll;

int main (){
    int T;
    //////////////.0...1...2...3...4...5.//
    char out[] = {'R','O','Y','G','B','V'};
    scanf("%d" ,&T);
    for (int t=1;t<=T;t++){
        //for each test
        int col[6],n,last=0,max=0, co=0, cg=0, cv = 0;
        bool impossible = false;
        scanf("%d %d %d %d %d %d %d", &n, &col[0], &col[1], &col[2], &col[3], &col[4], &col[5]);
        if(col[1]>0){
            if(col[1]>=col[4]){
                if(col[1]==col[4] && col[1]*2==n){
                    printf("Case #%d: ",t);
                    for(int i=0;i<col[1];i++){
                        printf("OB");
                    }
                    printf("\n");
                    continue;
                }else{
                    impossible = true;
                    //printf(">>1<<");
                }
            }else{
                //printf("zm");
                    co = col[1];
                    col[1]=0;
                    col[4] -= co;
            }
        }
        if(col[3]>0){
            if(col[3]>=col[0]){
                if(col[3]==col[0] && col[3]*2==n){
                        printf("Case #%d: ",t);
                        for(int i=0;i<col[3];i++){
                            printf("GR");
                        }
                        printf("\n");
                        continue;
                }else{
                    impossible = true;
                    //printf(">>3<<");
                }
            }else{
                //printf("zm");
                    cg = col[3];
                    col[3]=0;
                    col[0] -= cg;
            }
        }
        if(col[5]>0){
            if(col[5]>=col[2] ){
                if(col[5]==col[2] && col[5]*2==n){
                    printf("Case #%d: ",t);
                        for(int i=0;i<col[5];i++){
                            printf("VY");
                        }
                        printf("\n");
                        continue;
                }else{
                    impossible = true;
                    //printf(">>5<<");
                }
            }else{
                //printf("zm");
                cv = col[5];
                col[5]=0;
                col[2] -= cv;
            }
        }
        //printf("%d => COMP: %d %d %d %d %d %d", (int)impossible,  col[0],col[1],col[2],col[3],col[4],col[5]);
        int maxval = col[0];
        for(int i=2;i<6;i+=2){
            if(col[i]>maxval){
                maxval = col[i];
                max = i;
            }
        }
        int sum = col[0]+col[2]+col[4];
        impossible = impossible ||  sum<2*maxval;
        if(impossible){
            printf("Case #%d: IMPOSSIBLE\n", t);
        }else{
            printf("Case #%d: ",t);
            for(int i=0;i<sum;i++){
                int left = ((last!=max || i==0 )? col[max] : 0);
                int color = max;
                for(int y=0;y<6;y++){
                    if(y!=last && col[y]>left){
                        left = col[y];
                        color = y;
                    }
                }
                if(color==0){
                    while(cg-->0)printf("RG");
                }
                if(color==2){
                    while(cv-->0)printf("YV");
                }
                if(color==4){
                    while(co-->0)printf("BO");
                }

                printf("%c",out[color]);
                col[color]--;
                last=color;
            }
            printf("\n");
        }
        
    }
    return 0;
}
