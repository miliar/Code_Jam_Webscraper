#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

vector <char> A[1001];
int T, N, R, O, Y, G, B, V, M, Top;

int main(void) {

    int i, j, k, l, x, y, z;

    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d",&T);
    for(i=1 ; i<=T ; i++) {
        scanf("%d %d %d %d %d %d %d",&N,&R,&O,&Y,&G,&B,&V);
        printf("Case #%d: ",i);
        if(O>B || G>R || V>Y) {
            printf("IMPOSSIBLE\n");
            continue;
        }
        if(O==B && O) {
            if(N>2*O) {
                printf("IMPOSSIBLE\n");
                continue;
            }
            for(j=1 ; j<=O ; j++)
                printf("OB");
            printf("\n");
            continue;
        }
        if(G==R && G) {
            if(N>2*G) {
                printf("IMPOSSIBLE\n");
                continue;
            }
            for(j=1 ; j<=G ; j++)
                printf("GR");
            printf("\n");
            continue;
        }
        if(V==Y && V) {
            if(N>2*V) {
                printf("IMPOSSIBLE\n");
                continue;
            }
            for(j=1 ; j<=V ; j++)
                printf("VY");
            printf("\n");
            continue;
        }
        x=B-O;
        y=R-G;
        z=Y-V;
        if(x>=y && x>=z && x>y+z) {
            printf("IMPOSSIBLE\n");
            continue;
        }
        if(y>=x && y>=z && y>x+z) {
            printf("IMPOSSIBLE\n");
            continue;
        }
        if(z>=x && z>=y && z>x+y) {
            printf("IMPOSSIBLE\n");
            continue;
        }
        M=max(max(x,y),z);
        for(j=1 ; j<=M ; j++)
            A[j].clear();
        if(x>=y && x>=z) {
            Top=1;
            A[Top].push_back('B');
            for(j=1 ; j<=O ; j++) {
                A[Top].push_back('O');
                A[Top].push_back('B');
            }
            for(j=2 ; j<=x ; j++) {
                Top++;
                if(Top>M)
                    Top=1;
                A[Top].push_back('B');
            }
            Top=0;
            if(y) {
                Top++;
                A[Top].push_back('R');
                for(j=1 ; j<=G ; j++) {
                    A[Top].push_back('G');
                    A[Top].push_back('R');
                }
                for(j=2 ; j<=y ; j++) {
                    Top++;
                    if(Top>M)
                        Top=1;
                    A[Top].push_back('R');
                }
            }
            if(z) {
                Top++;
                if(Top>M)
                    Top=1;
                A[Top].push_back('Y');
                for(j=1 ; j<=V ; j++) {
                    A[Top].push_back('V');
                    A[Top].push_back('Y');
                }
                for(j=2 ; j<=z ; j++) {
                    Top++;
                    if(Top>M)
                        Top=1;
                    A[Top].push_back('Y');
                }
            }
        }
        else if(y>=x && y>=z) {
            Top=1;
            A[Top].push_back('R');
            for(j=1 ; j<=G ; j++) {
                A[Top].push_back('G');
                A[Top].push_back('R');
            }
            for(j=2 ; j<=y ; j++) {
                Top++;
                if(Top>M)
                    Top=1;
                A[Top].push_back('R');
            }
            Top=0;
            if(x) {
                Top++;
                A[Top].push_back('B');
                for(j=1 ; j<=O ; j++) {
                    A[Top].push_back('O');
                    A[Top].push_back('B');
                }
                for(j=2 ; j<=x ; j++) {
                    Top++;
                    if(Top>M)
                        Top=1;
                    A[Top].push_back('B');
                }
            }
            if(z) {
                Top++;
                if(Top>M)
                    Top=1;
                A[Top].push_back('Y');
                for(j=1 ; j<=V ; j++) {
                    A[Top].push_back('V');
                    A[Top].push_back('Y');
                }
                for(j=2 ; j<=z ; j++) {
                    Top++;
                    if(Top>M)
                        Top=1;
                    A[Top].push_back('Y');
                }
            }
        }
        else {
            Top=1;
            A[Top].push_back('Y');
            for(j=1 ; j<=V ; j++) {
                A[Top].push_back('V');
                A[Top].push_back('Y');
            }
            for(j=2 ; j<=z ; j++) {
                Top++;
                if(Top>M)
                    Top=1;
                A[Top].push_back('Y');
            }
            Top=0;
            if(x) {
                Top++;
                A[Top].push_back('B');
                for(j=1 ; j<=O ; j++) {
                    A[Top].push_back('O');
                    A[Top].push_back('B');
                }
                for(j=2 ; j<=x ; j++) {
                    Top++;
                    if(Top>M)
                        Top=1;
                    A[Top].push_back('B');
                }
            }
            if(y) {
                Top++;
                if(Top>M)
                    Top=1;
                A[Top].push_back('R');
                for(j=1 ; j<=G ; j++) {
                    A[Top].push_back('G');
                    A[Top].push_back('R');
                }
                for(j=2 ; j<=y ; j++) {
                    Top++;
                    if(Top>M)
                        Top=1;
                    A[Top].push_back('R');
                }
            }
        }
        for(j=1 ; j<=M ; j++) {
            l=A[j].size();
            for(k=0 ; k<l ; k++)
                printf("%c",A[j][k]);
        }
        printf("\n");
    }

    return 0;
}
