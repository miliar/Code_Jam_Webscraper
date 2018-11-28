#include <iostream>
#include <vector>
using namespace std;

struct Node
{
    char v;
    int r,c;
};
vector<Node> res;
vector<Node> all;
char mat[200][200];
char origin[200][200];
int mark[4][1000];

int main()
{
    ios::sync_with_stdio(false);
    int T,cas=0;
    cin >> T;
    while(T--)
    {
        res.clear();
        all.clear();
        memset(mat,0,sizeof(mat));
        memset(origin,0,sizeof(origin));
        memset(mark,0,sizeof(mark));
        cout << "Case #" << ++cas << ": ";
        int N,M;
        cin >> N >> M;
        int ans1=0,ans2=0;
        for(int i=0;i<M;++i)
        {
            Node u;
            string str;
            cin >> str;
            cin >> u.r >> u.c;
            origin[u.r][u.c]=str[0];
            mat[u.r][u.c]=str[0];
            all.push_back(Node{str[0],u.r,u.c});
            if(str[0]=='x')
            {
                mark[0][u.r]=1;
                mark[1][u.c]=1;
            }
            else if(str[0]=='+')
            {
                mark[2][u.r+u.c]=1;
                mark[3][u.r-u.c+100]=1;
            }
            else
            {
                mark[0][u.r]=1;
                mark[1][u.c]=1;
                mark[2][u.r+u.c]=1;
                mark[3][u.r-u.c+100]=1;
            }
        }
        for(int i=1;i<=N;++i)
        {
            int r[4]={1,i,N,i},c[4]={i,1,i,N};
            for(int j=0;j<4;++j)
            if(!mat[r[j]][c[j]]&&!mark[2][r[j]+c[j]]&&!mark[3][r[j]-c[j]+100])
            {
                mark[2][r[j]+c[j]]+=1;mark[3][r[j]-c[j]+100]+=1;
                mat[r[j]][c[j]]='+';
                all.push_back(Node{'+',r[j],c[j]});
            }
        }
        for(int i=1;i<=N;++i)
        {
            for(int j=1;j<=N;++j)
                if(!mat[i][j]&&!mark[0][i]&&!mark[1][j])
            {
                mark[0][i]+=1,mark[1][j]+=1;
                mat[i][j]='x';
                all.push_back(Node{'x',i,j});
            }
        }
//        cout << mark[0][N] << mark[1][N-1] << endl;
        for(int i=0;i<all.size();++i)
        {
            char v=all[i].v;
            int r=all[i].r,c=all[i].c;
            if(v=='+')
            {
                if(!mark[0][r]&&!mark[1][c])
                {
//                    cout << r << "*" << c << endl;
                    mark[0][r]+=1,mark[1][c]+=1;
                    mark[2][r+c]+=1,mark[3][r-c+100]+=1;
                    mat[r][c]='o';
                }
            }
            else if(v=='x')
            {
                if(!mark[2][r+c]&&!mark[3][r-c+100])
                {
                    mark[0][r]+=1,mark[1][c]+=1;
                    mark[2][r+c]+=1,mark[3][r-c+100]+=1;
                    mat[r][c]='o';
                }
            }
        }
        for(int i=1;i<=N;++i)
            for(int j=1;j<=N;++j)
            {
        if(mat[i][j]!=origin[i][j]) res.push_back(Node{mat[i][j],i,j}),ans2++;
                if(mat[i][j]) ans1++;
                if(mat[i][j]=='o') ans1++;
            }
        cout << ans1 << " " << ans2 << endl;
        for(int i=0;i<res.size();++i)
            cout << res[i].v << " " << res[i].r << " " << res[i].c << endl;

    }
}
