#include <cstdio>
#include <algorithm>
#include <set>
#include <iostream>
#include <vector>
using namespace std;


int r,c;
char m[100][100];
struct beam{
    int r,c;
    bool hor;
};
vector<beam> s[100][100];
void findbeam(int x,int y){
    for(int i = x + 1 ; i < r ; i ++){
        if(m[i][y]=='|'||m[i][y]=='-'){
            s[x][y].push_back({i,y,false});
        }
        if(m[i][y]=='#')break;
    }
    for(int i = x - 1 ; i >= 0 ; i --){
        if(m[i][y]=='|'||m[i][y]=='-'){
            s[x][y].push_back({i,y,false});
        }
        if(m[i][y]=='#')break;
    }
    for(int i = y + 1 ; i < c ; i ++){
        if(m[x][i]=='|'||m[x][i]=='-'){
            s[x][y].push_back({x,i,true});
        }
        if(m[x][i]=='#')break;
    }
    for(int i = y - 1 ; i >= 0 ; i --){
        if(m[x][i]=='|'||m[x][i]=='-'){
            s[x][y].push_back({x,i,true});
        }
        if(m[x][i]=='#')break;
    }
}
bool canhor[100][100];
bool canver[100][100];
bool musthor[100][100];
bool mustver[100][100];
bool hor[100][100];
int check(){
    for(int i = 0 ; i < r ; i ++){
        for(int j = 0 ; j < c ; j ++){
            if(m[i][j]!='.')continue;
            bool have=false;
            for(const auto& x:s[i][j]){
                if(hor[x.r][x.c]==x.hor){
                    have=true;
                    break;
                }
            }
            if(!have)return -1;
        }
    }
    return 1;
}
int dfs(int x,int y){
    while(1){
        if(x==r)break;
        if(m[x][y]=='-'||m[x][y]=='|')break;
        y++;
        if(y==c){
            y=0;
            x++;
        }
    }
    if(x==r){
        return check();
    }
    if(canhor[x][y]&&(!mustver[x][y])){
        int nextx=x;
        int nexty=y;
        nexty++;
        if(nexty==c){
            nexty=0;
            nextx++;
        }
        hor[x][y]=true;
        int ret = dfs(nextx,nexty);
        if(ret==1)return 1;
    }
    if(canver[x][y]&&(!musthor[x][y])){
        int nextx=x;
        int nexty=y;
        nexty++;
        if(nexty==c){
            nexty=0;
            nextx++;
        }
        hor[x][y]=false;
        int ret = dfs(nextx,nexty);
        if(ret==1)return 1;
    }
    return -1;
}
int main (){
    int T;
    scanf("%d",&T);
    for(int I = 1 ; I <= T ; I ++){
        scanf("%d%d",&r,&c);
        for(int i = 0 ; i < 100 ; i ++){
            for(int j = 0 ; j < 100 ; j ++){
                s[i][j].clear();
                canhor[i][j]=true;
                canver[i][j]=true;
                musthor[i][j]=false;
                mustver[i][j]=false;
            }
        }
        for(int i = 0 ; i < r ; i ++){
            scanf("%s",m[i]);
        }
        bool bad=false;
        for(int i = 0 ; i < r ; i ++){
            for(int j = 0 ; j < c ; j ++){
                if(m[i][j]=='.'||m[i][j]=='|'||m[i][j]=='-'){
                    findbeam(i,j);
                    if(m[i][j]!='.'){
                        for(const auto &x : s[i][j]){
                            if(x.hor){
                                canhor[x.r][x.c]=false;
                            }
                            else{
                                canver[x.r][x.c]=false;
                            }
                        }
                    }
                    else{
                        if(s[i][j].size()==1){
                            if(s[i][j][0].hor){
                                musthor[s[i][j][0].r][s[i][j][0].c]=true;
                            }
                            else{
                                mustver[s[i][j][0].r][s[i][j][0].c]=true;
                            }
                        }
                        if(s[i][j].size()==0)bad=true;
                    }
                }
            }
        }
        int ret;
        if(!bad)ret=dfs(0,0);
        else ret=-1;
        printf("Case #%d: ",I);
        if(ret==1){
            printf("POSSIBLE\n");
            for(int i = 0 ; i < r ; i ++){
                for(int j = 0 ; j < c ; j ++){
                    if(m[i][j]=='|'||m[i][j]=='-'){
                        if(hor[i][j])m[i][j]='-';
                        else m[i][j]='|';
                    }
                    printf("%c",m[i][j]);
                }
                printf("\n");
            }
        }
        else printf("IMPOSSIBLE\n");
    }
}
