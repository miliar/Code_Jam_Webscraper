//Mitesh Agrawal
#include <bits/stdc++.h>
using namespace std;

#define infi 2000000000

int Hd,Ad,Hk,Ak,B,D;
int dp[105][20000][105][105];

int f(int H1, int A1, int H2, int A2){
    // printf("IN %d %d %d %d\n",H1,A1,H2,A2);
    int i,j;
    if(H1<=0) 
        return infi+2;
    if(H2<=0) 
        return 0;
    if(H2-A1<=0) 
        return 1;
    int &mini = dp[H1][A1][H2][A2];
    if(mini!=infi){ 
        // printf("OUT %d %d %d %d %d\n",H1,A1,H2,A2,mini);    
        return mini;
    }
    //attack
    if(!(A1==0 && A2==0))
        mini = min(mini,1+f(H1-A2,A1,H2-A1,A2));
    //buff
    if(!(A2==0 && B==0))
        mini = min(mini,1+f(H1-A2,A1+B,H2,A2));
    //cure
    if(!(Hd-A2==H1))
        mini = min(mini,1+f(Hd-A2,A1,H2,A2));
    //debuff
    if(A2!=0)
        mini = min(mini,1+f(H1-max(0,A2-D),A1,H2,max(0,A2-D)));
    // printf("OUT %d %d %d %d %d\n",H1,A1,H2,A2,mini);
    return mini;
}

int main(){
    freopen ("C-small-attempt2.in","r",stdin); 
    // freopen ("output.out","w",stdout); 

    int i,j,k,l,t,test,temp;
    scanf("%d",&t);
    for(test=1;test<=t;test++){
        scanf("%d %d %d %d %d %d",&Hd,&Ad,&Hk,&Ak,&B,&D);
        for(i=0;i<=Hd;i++)
        for(j=0;j<=Ad+B*100;j++)
        for(k=0;k<=Hk;k++)
        for(l=0;l<=Ak;l++)
            dp[i][j][k][l] = infi;
        int temp = f(Hd,Ad,Hk,Ak);
        if(temp!=infi)
            printf("Case #%d: %d\n",test,temp);
        else
            printf("Case #%d: IMPOSSIBLE\n",test);
    }


    return 0;
}