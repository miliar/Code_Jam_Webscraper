#include <stdio.h>
#include <algorithm>
#define INF 0x7fffffff

using namespace std;

int T, N, P, G[101], Zero, One, Two, Three, D1[101][101][101], D2[101][101][101][101];

int main(void) {

    int i, j, k, l, m;

    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d",&T);
    for(i=1 ; i<=T ; i++) {
        scanf("%d %d",&N,&P);
        for(j=1 ; j<=N ; j++)
            scanf("%d",&G[j]);
        Zero=One=Two=Three=0;
        printf("Case #%d: ",i);
        if(P==2) {
            for(j=1 ; j<=N ; j++) {
                if(G[j]%2)
                    One++;
                else
                    Zero++;
            }
            printf("%d\n",Zero+(One+1)/2);
        }
        else if(P==3) {
            for(j=1 ; j<=N ; j++) {
                if(G[j]%3==1)
                    One++;
                else if(G[j]%3==2)
                    Two++;
                else
                    Zero++;
            }
            D1[0][0][0]=0;
            for(j=0 ; j<=Zero ; j++)
                for(k=0 ; k<=One ; k++)
                    for(l=0 ; l<=Two ; l++) {
                        if(j || k || l)
                            D1[j][k][l]=-INF;
                        if(j-1>=0)
                            D1[j][k][l]=max(D1[j][k][l],D1[j-1][k][l]+1);
                        if(k-3>=0)
                            D1[j][k][l]=max(D1[j][k][l],D1[j][k-3][l]+1);
                        if(l-3>=0)
                            D1[j][k][l]=max(D1[j][k][l],D1[j][k][l-3]+1);
                        if(k-1>=0 && l-1>=0)
                            D1[j][k][l]=max(D1[j][k][l],D1[j][k-1][l-1]+1);
                    }
            if(One-1>=0)
                D1[Zero][One][Two]=max(D1[Zero][One][Two],D1[Zero][One-1][Two]+1);
            if(One-2>=0)
                D1[Zero][One][Two]=max(D1[Zero][One][Two],D1[Zero][One-2][Two]+1);
            if(Two-1>=0)
                D1[Zero][One][Two]=max(D1[Zero][One][Two],D1[Zero][One][Two-1]+1);
            if(Two-2>=0)
                D1[Zero][One][Two]=max(D1[Zero][One][Two],D1[Zero][One][Two-2]+1);
            printf("%d\n",D1[Zero][One][Two]);
        }
        else {
            for(j=1 ; j<=N ; j++) {
                if(G[j]%4==1)
                    One++;
                else if(G[j]%4==2)
                    Two++;
                else if(G[j]%4==3)
                    Three++;
                else
                    Zero++;
            }
            D2[0][0][0][0]=0;
            for(j=0 ; j<=Zero ; j++)
                for(k=0 ; k<=One ; k++)
                    for(l=0 ; l<=Two ; l++)
                        for(m=0 ; m<=Three ; m++) {
                            if(j || k || l || m)
                                D2[j][k][l][m]=-INF;
                            if(j-1>=0)
                                D2[j][k][l][m]=max(D2[j][k][l][m],D2[j-1][k][l][m]+1);
                            if(k-4>=0)
                                D2[j][k][l][m]=max(D2[j][k][l][m],D2[j][k-4][l][m]+1);
                            if(l-2>=0)
                                D2[j][k][l][m]=max(D2[j][k][l][m],D2[j][k][l-2][m]+1);
                            if(m-4>=0)
                                D2[j][k][l][m]=max(D2[j][k][l][m],D2[j][k][l][m-4]+1);
                            if(k-2>=0 && l-1>=0)
                                D2[j][k][l][m]=max(D2[j][k][l][m],D2[j][k-2][l-1][m]+1);
                            if(k-1>=0 && m-1>=0)
                                D2[j][k][l][m]=max(D2[j][k][l][m],D2[j][k-1][l][m-1]+1);
                            if(l-1>=0 && m-2>=0)
                                D2[j][k][l][m]=max(D2[j][k][l][m],D2[j][k][l-1][m-2]+1);
                        }
            if(Three-1>=0)
                D2[Zero][One][Two][Three]=max(D2[Zero][One][Two][Three],D2[Zero][One][Two][Three-1]+1);
            if(Three-2>=0)
                D2[Zero][One][Two][Three]=max(D2[Zero][One][Two][Three],D2[Zero][One][Two][Three-2]+1);
            if(Three-3>=0)
                D2[Zero][One][Two][Three]=max(D2[Zero][One][Two][Three],D2[Zero][One][Two][Three-3]+1);
            if(One-1>=0)
                D2[Zero][One][Two][Three]=max(D2[Zero][One][Two][Three],D2[Zero][One-1][Two][Three]+1);
            if(One-2>=0)
                D2[Zero][One][Two][Three]=max(D2[Zero][One][Two][Three],D2[Zero][One-2][Two][Three]+1);
            if(One-3>=0)
                D2[Zero][One][Two][Three]=max(D2[Zero][One][Two][Three],D2[Zero][One-3][Two][Three]+1);
            if(Two-1>=0)
                D2[Zero][One][Two][Three]=max(D2[Zero][One][Two][Three],D2[Zero][One][Two-1][Three]+1);
            if(One-1>=0 && Two-1>=0)
                D2[Zero][One][Two][Three]=max(D2[Zero][One][Two][Three],D2[Zero][One-1][Two-1][Three]+1);
            if(Two-1>=0 && Three-1>=0)
                D2[Zero][One][Two][Three]=max(D2[Zero][One][Two][Three],D2[Zero][One][Two-1][Three-1]+1);
            printf("%d\n",D2[Zero][One][Two][Three]);
        }
    }

    return 0;
}
