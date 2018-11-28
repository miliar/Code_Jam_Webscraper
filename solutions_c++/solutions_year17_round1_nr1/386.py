#include <iostream>
#include <string.h>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
using namespace std;
#define maxn 100010
char cake[30][30];
int vis[26];
int n,m;
void sovle(int x,int y,char c) {
    int l=y,r=y;
    while(l>=0&&(cake[x][l]==c||cake[x][l]=='?')) l--;
    while(r<m&&(cake[x][r]==c||cake[x][r]=='?')) r++;
    int up=30,down=30;
    for(int i=l+1;i<r;i++){
        int tup = 0,tdown = 0;
        for(tup=0;tup<=x;tup++){
            if(cake[x-tup][i]!='?'&&cake[x-tup][i]!=c)
                break;
        }
        tup--;
        up=min(up,tup);
        for(tdown=0;tdown+x<n;tdown++){
            if(cake[x+tdown][i]!='?'&&cake[x+tdown][i]!=c)
                break;
        }
        tdown--;
        down = min(down,tdown);
    }
    for(int i=l+1;i<r;i++){
        for(int j=-up;j<=down;j++){
            cake[x+j][i] = c;
        }
    }
}
void print(){
for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                printf("%c",cake[i][j]);
            }
            printf("\n");
        }
}
int main()
{
    freopen("ddl.in","r",stdin);
    freopen("out.txt","w+",stdout);
    int ncase,T=0;
    cin>>ncase;
    while(ncase--){
        printf("Case #%d:\n",++T);
        scanf("%d%d",&n,&m);
        memset(vis,0,sizeof(vis));
        for(int i=0;i<n;i++){
            scanf("%s",cake[i]);
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(cake[i][j]!='?'&&vis[cake[i][j]-'A']==0){
                    sovle(i,j,cake[i][j]);
                    vis[cake[i][j]-'A'] = 1;
                }
            }
            //print();
        }
        print();
    }
    return 0;
}
