#include <bits/stdc++.h>

using namespace std;

char a[105][105],s[5];
bool col[105];

int main(){

    freopen("out.out","w",stdout);

    int T;
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++){

        int n,m,r,c;
        scanf("%d%d",&n,&m);
        memset(a,'.',sizeof a);

        bool haveO=false,haveX=false;
        for (int i=0;i<m;i++){
            scanf("%s%d%d",s,&r,&c);
            r--,c--;
            a[r][c]=s[0];
            if (s[0]=='o') haveO=true;
            if (s[0]=='x') haveX=true;
        }

        int cnt=-1;
        if (haveO) cnt=n-m;
        else if (haveX) cnt=n-m+1;
        else if (a[0][0]=='+') cnt=n-m+1;
        else cnt=n-m;

        int score=3*n-2;
        if (n==1) score=2;
        else cnt+=2*n-3;
        printf("Case #%d: %d %d\n",cas,score,cnt);


        if (haveX){
            for (int i=0;i<n;i++){
                if (a[0][i]=='x'){
                    a[0][i]='o';
                    printf("o %d %d\n",1,i+1);
                    break;
                }
            }
        }
        else if (!haveO){
            a[0][0]='o';
            printf("o 1 1\n");
        }
        for (int i=0;i<n;i++){
            if (a[0][i]=='.'){
                a[0][i]='+';
                printf("+ %d %d\n",1,i+1);
            }
        }

        memset(col,false,sizeof col);
        for (int i=1;i<n-1;i++)
            a[n-1][i]='+';
        for (int i=0;i<n;i++){
            if (a[0][i]=='o'){
                col[i]=true;
                if (i==0) a[n-1][n-1]='x',col[n-1]=true;
                else a[n-1][0]='x',col[0]=true;
                break;
            }
        }

        for (int i=1;i<n-1;i++){
            for (int j=0;j<n;j++){
                if (false==col[j]){
                    col[j]=true;
                    a[i][j]='x';
                    break;
                }
            }
        }

        for (int i=1;i<n;i++){
            for (int j=0;j<n;j++){
                if (a[i][j]=='x') printf("x %d %d\n",i+1,j+1);
                if (a[i][j]=='+') printf("+ %d %d\n",i+1,j+1);
            }
        }

    }

    return 0;
}
