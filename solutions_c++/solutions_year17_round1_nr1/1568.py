#include <iostream>
#include <stdio.h>

using namespace std;
char mat[30][30];
int r,c;
bool into(int x,int y){
    return (x>=0 && x<r && y>=0 && y<c);
}
void _fill(int x, int y){
    int d=1;
    while (into(x,y+d) && mat[x][y+d]=='?'){
        mat[x][y+d]=mat[x][y+d-1];
        d++;
    }
    d=1;
    while (into(x,y-d) && mat[x][y-d]=='?'){
        mat[x][y-d]=mat[x][y-d+1];
        d++;
    }
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for (int _case=1; _case<=t; _case++){
        scanf("%d %d",&r,&c);
        for (int i=0; i<r; i++){
            scanf("%s",mat[i]);
        }
        for (int i=0; i<r; i++){
            for (int j=0; j<c; j++){
                if (mat[i][j]!='?'){
                    _fill(i,j);
                }
            }
        }
        for (int i=0; i<r; i++){
            for (int j=0; j<c; j++){
                if (mat[i][j]!='?'){
                    if (into(i+1,j) && mat[i+1][j]=='?'){
                        mat[i+1][j]=mat[i][j];
                    }
                }
            }
        }
        for (int i=r-1; i>=0; i--){
            for (int j=0; j<c; j++){
                if (mat[i][j]!='?'){
                    if (into(i-1,j) && mat[i-1][j]=='?'){
                        mat[i-1][j]=mat[i][j];
                    }
                }
            }
        }
        printf("Case #%d:\n",_case);
        for (int i=0; i<r; i++) printf("%s\n",mat[i]);
    }


    fclose(stdin);
    fclose(stdout);
    return 0;
}
