#include<stdio.h>

int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int N, R , O , Y , G , B , V;
    int T, cases ,i;
    char U[1002];
    scanf("%d",&T);
    for(cases=1;cases<=T;cases++){
        scanf("%d%d%d%d%d%d%d",&N,&R,&O,&Y,&G,&B,&V);
        if(Y+B<R || R+B<Y || Y+R<B)printf("Case #%d: IMPOSSIBLE\n",cases);
        else {
            printf("Case #%d: ",cases);
            if(R>=B && R>=Y)U[1]='R',R--;
            else if(B>=R && B>=Y)U[1]='B',B--;
            else U[1]='Y',Y--;
            for(i=2;i<=N;i++){
                if(U[i-1]=='R'){
                    if(B>Y)U[i]='B',B--;
                    else if(Y>B)U[i]='Y',Y--;
                    else if(U[1]=='Y')U[i]='Y',Y--;
                    else U[i]='B',B--;
                }
                if(U[i-1]=='B'){
                    if(R>Y)U[i]='R',R--;
                    else if(Y>R)U[i]='Y',Y--;
                    else if(U[1]=='Y')U[i]='Y',Y--;
                    else U[i]='R',R--;
                }
                if(U[i-1]=='Y'){
                    if(R>B)U[i]='R',R--;
                    else if(B>R)U[i]='B',B--;
                    else if(U[1]=='B')U[i]='B',B--;
                    else U[i]='R',R--;
                }
            }
            for(i=1;i<=N;i++)printf("%c",U[i]);
            printf("\n");
        }
        
    }

    return 0;
}
