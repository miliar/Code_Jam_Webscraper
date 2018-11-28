#include<stdio.h>
#include<iostream>
#include<map>
#include<string.h>
#include<vector>
#include<algorithm>
using namespace std;
typedef long long LL;
const int N = 30;
int n;
int r,c;
char s[N][N];
char res[N][N];
bool col[N],row[N];
vector<int> vr,vc;

void Do(int n,int m){

}

int main(){
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    int T;scanf("%d",&T);
    int cas = 1;
    while(T--){
        scanf("%d%d",&r,&c);
        for(int i=1;i<=r;i++) scanf("%s",s[i]+1);
        // for(int i=1;i<=r;i++) puts(s[i]+1);
        memset(col,0,sizeof col);
        memset(row,0,sizeof row);
        for(int i=1;i<=r;i++) for(int j=1;j<=c;j++)
            if(s[i][j]!='?') row[i]=1,col[j]=1;
        vc.clear();


        for(int j=1;j<=c;j++) if(col[j]) vc.push_back(j);
        vc.push_back(c+1);
       
        int L,R;
        int x,y;
        for(int j=0;j<vc.size()-1;j++){
            y = vc[j];
            if(j==0) L = 1;
            else L = y;

            R = vc[j+1]-1;

            // printf("L:%d,R:%d\n",L,R);
            
            vr.clear();
            
            for(int i=1;i<=r;i++){
                if(s[i][y]!='?') vr.push_back(i);
            }
            vr.push_back(r+1);
            int up,down;
            for(int i=0;i<vr.size()-1;i++){
                x = vr[i];
                if(i==0) up = 1;
                else up = x;
                down = vr[i+1]-1;

                char ch = s[x][y];
                for(int ii=up;ii<=down;ii++){
                    for(int jj=L;jj<=R;jj++)
                        res[ii][jj]=ch;
                }
            }

        }
        printf("Case #%d:\n",cas++);
        for(int i=1;i<=r;i++){
            for(int j=1;j<=c;j++)
                printf("%c",res[i][j]);
            puts("");
        }

    }

    return 0;
}
