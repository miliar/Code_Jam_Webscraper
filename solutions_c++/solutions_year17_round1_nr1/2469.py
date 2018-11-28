#include <cstdio>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <list>
#include <set>
using namespace std;

const int MAXN=30;
char g[MAXN][MAXN];

void fill(int left,int right,int bottom,int top,char ch)
{
    for (int r=bottom;r<=top;r++){
        for (int c=left;c<=right;c++){
            g[r][c]=ch;
        }
    }
}
void output(int R)
{
    for (int i=0;i<R;i++){
        printf("%s\n",g[i]);
    }
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A_output_large.txt","w",stdout);
    int T,R,C;
    bool col[MAXN];
    vector<int> row;
    scanf("%d",&T);
    for (int index=1;index<=T;index++){
        scanf("%d%d",&R,&C);
        memset(col,0,sizeof(col));
        for (int i=0;i<R;i++){
            scanf("%s",g[i]);
            for (int j=0;j<C;j++){
                if (g[i][j]!='?') col[j]=true;
            }
        }
        int left,right;
        left = 0;
        for (int c=0;c<C;c++){
            if (!col[c]) continue;
            if (left>0) left=c;
            right=c;
            for (int i=c+1;i<C;i++){
                if (col[i]) {right=i-1; break;}
                else right=i;
            }
            //printf("left=%d right=%d\n",left,right);
            row.clear();
            for (int r=0;r<R;r++){
                if (g[r][c]!='?') row.push_back(r);
            }
            //printf("c=%d\n",c);
            //for (int i=0;i<row.size();i++) printf("%d ",row[i]); printf("\n");
            int bottom,top;
            if (row.size()==1){
                bottom = 0; top = R-1;
                fill(left,right,bottom,top,g[row[0]][c]);
            }else{
                bottom = 0; top = row[1]-1;
                fill(left,right,bottom,top,g[row[0]][c]);
                for (int i=1;i<row.size();i++){
                    bottom = row[i];
                    if (i==row.size()-1){
                        top = R-1;
                    }else{
                        top = row[i+1]-1;
                    }
                    fill(left,right,bottom,top,g[row[i]][c]);
                }
            }
            left=c+1;
        }
        printf("Case #%d:\n",index);
        output(R);
    }
    return 0;
}
