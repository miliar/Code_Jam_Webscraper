#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <vector>
#include <map>
#include <string>

using namespace std;
char maz[55][55];
int stats[3000][2];
int can[55][55][3000];
int di[55][55][3000][2];
int R,C;
vector<pair<int,int> > idx;
const int dx[4]={-1,1,0,0};
const int dy[4]={0,0,-1,1};
bool invalid(int x,int y)
{
    if(x<1||x>R||y<1||y>C) return false;
    if(maz[x][y]=='#') return false;
    return true;
}
int main()
{
    int T;
    scanf("%d",&T);
    for(int kase=1;kase<=T;kase++){

        idx.clear();
        int cnt=0;
        memset(can,0,sizeof(can));
        memset(di,0,sizeof(di));
        for(int i=1;i<=R*C;i++) stats[i][0]=stats[i][1]=1;
        scanf("%d%d",&R,&C);
        for(int i=1;i<=R;i++) scanf("%s",maz[i]+1);
        idx.push_back(make_pair(-1,-1));
        for(int i=1;i<=R;i++)
            for(int j=1;j<=C;j++)
            if(maz[i][j]=='|'||maz[i][j]=='-') {
            idx.push_back(make_pair(i,j));
            ++cnt;
            for(int dir=0;dir<4;dir++){
                int Dir=dir;
                int I=i,J=j;
                while(1){
                    if(invalid(I+dx[Dir],J+dy[Dir])) break;
                    if(maz[I+dx[Dir]][J+dy[Dir]]=='.'){
                        I+=dx[Dir];
                        J+=dy[Dir];
                        if(!can[I][J][cnt])
                            can[I][J][0]++;
                        can[I][J][cnt]=1;
                        di[I][J][cnt][dir/2]=1;

                    }
                    else if(maz[I+dx[Dir]][J+dy[Dir]]=='|'||maz[I+dx[Dir]][J+dy[Dir]]=='-'){
                        I+=dx[Dir];
                        J+=dy[Dir];
                        if(!can[I][J][cnt])
                            can[I][J][0]++;
                        can[I][J][cnt]=1;
                        stats[cnt][dir/2]=0;
                        di[I][J][cnt][dir/2]=1;
                    }
                }
            }
            bool impossible=false;
            for(int i=1;i<=R;i++){
                for(int j=1;j<=C;j++){
                    if(maz[i][j]=='.'){
                        for(int k=1;k<=cnt;k++) {
                            if(can[i][j][k]){
                                if( (di[i][j][k][0]&&(!stats[k][0])) && (di[i][j][k][1]&&(!stats[k][1])) ) {
                                        can[i][j][0]--;
                                        can[i][j][k]=0;
                                }
                            }
                        }
                        if(can[i][j][0]==0){
                            impossible=true;
                        }

                    }
                }
            }

        }

    }
    return 0;
}
