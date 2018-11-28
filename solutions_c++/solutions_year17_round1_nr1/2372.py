#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <sstream>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <limits>
#include <iomanip>

#define INF 1000000007
#define MAXN 30

using namespace std;

char mat[MAXN][MAXN];
int esq[1000], dir[1000], cim[1000], bai[1000];

int main() {
//    freopen("alphabet_cake_large.txt", "r", stdin);
//    freopen("alphabet_cake_large_out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    int caso;
    for (caso=1; caso<=t; caso++) {
        int r, c;
        scanf("%d %d", &r, &c);
        int i, j;
        for (i=1; i<=r; i++) {
            scanf("%s", mat[i]+1);
        }
        char x;
        memset(esq, -1, sizeof(esq));
        memset(dir, -1, sizeof(dir));
        memset(cim, -1, sizeof(cim));
        memset(bai, -1, sizeof(bai));
        for (i=1; i<=r; i++) {
            for (j=1; j<=c; j++) {
                x=mat[i][j];
                if (x!='?') {
                    if (esq[x]==-1 || j<esq[x]) {
                        esq[x]=j;
                    }
                    if (dir[x]==-1 || j>dir[x]) {
                        dir[x]=j;
                    }
                    if (cim[x]==-1 || i<cim[x]) {
                        cim[x]=i;
                    }
                    if (bai[x]==-1 || i>bai[x]) {
                        bai[x]=i;
                    }
                }
            }
        }
        for (x='A'; x<='Z'; x++) {
            if (esq[x]!=-1) {
                for (i=cim[x]; i<=bai[x]; i++) {
                    for (j=esq[x]; j<=dir[x]; j++) {
                        mat[i][j]=x;
                    }
                }
            }
        }
        int pode;
//        printf("**\n");
//        for (i=1; i<=r; i++) {
//            printf("%s\n", mat[i]+1);
//        }
//        printf("**\n");
        // aumentar na esquerda
        int esqCand;
        for (x='A'; x<='Z'; x++) {
            if (esq[x]!=-1) {
                esqCand=esq[x]-1;
                while (esqCand>=1) {
                    pode=1;
                    for (i=cim[x]; i<=bai[x]; i++) {
                        if (mat[i][esqCand]!='?' && mat[i][esqCand]!=x) {
                            pode=0;
                            break;
                        }
                    }
                    if (pode==0) {
                        break;
                    }
                    esqCand--;
                }
                esqCand++;
                for (i=cim[x]; i<=bai[x]; i++) {
                    for (j=esqCand; j<esq[x]; j++) {
                        mat[i][j]=x;
                    }
                }
                esq[x]=esqCand;
//                printf("++ esq %c: %d\n", x, esqCand);
            }
        }

//        printf("**\n");
//        for (i=1; i<=r; i++) {
//            printf("%s\n", mat[i]+1);
//        }
//        printf("**\n");

        // aumentar na direita
        int dirCand;
        for (x='A'; x<='Z'; x++) {
            if (dir[x]!=-1) {
                dirCand=dir[x]+1;
                while (dirCand<=c) {
                    pode=1;
                    for (i=cim[x]; i<=bai[x]; i++) {
                        if (mat[i][dirCand]!='?' && mat[i][dirCand]!=x) {
                            pode=0;
                            break;
                        }
                    }
                    if (pode==0) {
                        break;
                    }
                    dirCand++;
                }
                dirCand--;
                for (i=cim[x]; i<=bai[x]; i++) {
                    for (j=dir[x]+1; j<=dirCand; j++) {
                        mat[i][j]=x;
                    }
                }
                dir[x]=dirCand;
//                printf("++ dir %c: %d\n", x, dirCand);
            }
        }

//        printf("**\n");
//        for (i=1; i<=r; i++) {
//            printf("%s\n", mat[i]+1);
//        }
//        printf("**\n");

        // aumentar encima
        int cimCand;
        for (x='A'; x<='Z'; x++) {
            if (cim[x]!=-1) {
                cimCand=cim[x]-1;
                while (cimCand>=1) {
                    pode=1;
                    for (j=esq[x]; j<=dir[x]; j++) {
                        if (mat[cimCand][j]!='?' && mat[cimCand][j]!=x) {
                            pode=0;
                            break;
                        }
                    }
                    if (pode==0) {
                        break;
                    }
                    cimCand--;
                }
                cimCand++;
                for (i=cimCand; i<cim[x]; i++) {
                    for (j=esq[x]; j<=dir[x]; j++) {
                        mat[i][j]=x;
                    }
                }
                cim[x]=cimCand;
            }
        }

//        printf("**\n");
//        for (i=1; i<=r; i++) {
//            printf("%s\n", mat[i]+1);
//        }
//        printf("**\n");

        // aumentar embaixo
        int baiCand;
        for (x='A'; x<='Z'; x++) {
            if (bai[x]!=-1) {
                baiCand=bai[x]+1;
                while (baiCand<=r) {
                    pode=1;
                    for (j=esq[x]; j<=dir[x]; j++) {
                        if (mat[baiCand][j]!='?' && mat[baiCand][j]!=x) {
                            pode=0;
                            break;
                        }
                    }
                    if (pode==0) {
                        break;
                    }
                    baiCand++;
                }
                baiCand--;
                for (i=bai[x]+1; i<=baiCand; i++) {
                    for (j=esq[x]; j<=dir[x]; j++) {
                        mat[i][j]=x;
                    }
                }
                bai[x]=baiCand;
            }
        }
        printf("Case #%d:\n", caso);
        for (i=1; i<=r; i++) {
            printf("%s\n", mat[i]+1);
        }
    }
    return 0;
}









