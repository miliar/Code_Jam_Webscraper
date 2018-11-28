#include <stdio.h>

int main(){
    freopen("out.txt","w",stdout);
    int T;

    scanf("%d",&T);

    for (int i = 1; i<=T; i++){
        int iD,N;
        scanf("%d%d",&iD,&N);
        double D = iD;
        int K,S;
        bool speedSet = false;
        double speed = 0;

        for (int j = 0; j<N; j++){
            scanf("%d%d",&K,&S);
            double answer = D/(D-K)*S;
            if (speed>answer or !speedSet){
                speedSet = true;
                speed = answer;
            }
        }


        printf("Case #%d: %lf\n",i,speed);
    }
    return 0;
}
