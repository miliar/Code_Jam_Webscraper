#include <cstdio>
#include <algorithm>

using namespace std;

int D[777][777][2][2];
int A[1444], B[1444];

int TC()
{
    int a,b,c,d,x,y,i,j;

    scanf("%d%d",&a,&b);

    for(i=0;i<=1440;i++){
        A[i] = B[i] = 0;
    }

    for(i=0;i<a;i++){
        scanf("%d%d",&x,&y);
        for(j=x;j<y;j++) A[j] = 1;
    }
    for(i=0;i<b;i++){
        scanf("%d%d",&x,&y);
        for(j=x;j<y;j++) B[j] = 1;
    }

    for(i=0;i<=720;i++){
        for(j=0;j<=720;j++){
            D[i][j][0][0] = D[i][j][1][0] = D[i][j][0][1] = D[i][j][1][1] = 1e9;

            if(A[i+j] == 0 && B[i+j] == 0){
                if(i) D[i][j][0][0] = min(D[i][j][0][0], D[i-1][j][0][0]);
                if(i) D[i][j][0][0] = min(D[i][j][0][0], D[i-1][j][0][1]+1);

                if(j) D[i][j][0][1] = min(D[i][j][0][1], D[i][j-1][0][1]);
                if(j) D[i][j][0][1] = min(D[i][j][0][1], D[i][j-1][0][0]+1);

                if(i) D[i][j][1][0] = min(D[i][j][1][0], D[i-1][j][1][0]);
                if(i) D[i][j][1][0] = min(D[i][j][1][0], D[i-1][j][1][1]+1);

                if(j) D[i][j][1][1] = min(D[i][j][1][1], D[i][j-1][1][1]);
                if(j) D[i][j][1][1] = min(D[i][j][1][1], D[i][j-1][1][0]+1);
            }
            else if(A[i+j] == 0){
                if(i) D[i][j][0][0] = min(D[i][j][0][0], D[i-1][j][0][0]);
                if(i) D[i][j][0][0] = min(D[i][j][0][0], D[i-1][j][0][1]+1);

                if(i) D[i][j][1][0] = min(D[i][j][1][0], D[i-1][j][1][0]);
                if(i) D[i][j][1][0] = min(D[i][j][1][0], D[i-1][j][1][1]+1);
            }
            else{
                if(j) D[i][j][0][1] = min(D[i][j][0][1], D[i][j-1][0][1]);
                if(j) D[i][j][0][1] = min(D[i][j][0][1], D[i][j-1][0][0]+1);

                if(j) D[i][j][1][1] = min(D[i][j][1][1], D[i][j-1][1][1]);
                if(j) D[i][j][1][1] = min(D[i][j][1][1], D[i][j-1][1][0]+1);
            }

            D[0][0][0][0] = D[0][0][1][1] = 0;
        }
    }

    a = D[720][720][0][0];
    b = D[720][720][0][1]+1;
    c = D[720][720][1][0]+1;
    d = D[720][720][1][1];

//    printf("%d %d %d %d\n",a,b,c,d);

    return min(min(a,b),min(c,d));
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);

    int i,t;
    scanf("%d",&t);

    for(i=1;i<=t;i++){
        printf("Case #%d: %d\n",i,TC());
    }

    return 0;
}
