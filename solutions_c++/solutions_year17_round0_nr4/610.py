#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

char base[105][105];
char fin[105][105];

int main()
{
    //To solve the large dataset do matching for the position of pluses
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int tc;
    scanf("%d",&tc);
    for (int itr=1; itr<=tc; itr++)
    {
        int n,m;
        scanf("%d%d",&n,&m);
        for (int i=1; i<=n; i++)
        {
            for (int j=1; j<=n; j++)
                base[i][j]='.';
            base[i][n+1]=0;
        }
        for (int i=1; i<=m; i++)
        {
            int x,y;
            char k[10];
            scanf("%s%d%d",k,&x,&y);
            base[x][y]=k[0];
        }
        for (int i=1; i<=n; i++)
            for (int j=1; j<=n+1; j++)
                fin[i][j]=base[i][j];
        for (int j=1; j<=n; j++)
        {
            if (fin[1][j]=='.')
                fin[1][j]='+';
            if (fin[1][j]=='x')
                fin[1][j]='o';
        }
        int xplace=1337;
        for (int j=1; j<=n; j++)
            if (fin[1][j]=='o')
                xplace=j;
        if (xplace==1337)
        {
            fin[1][1]='o';
            xplace=1;
        }
        for (int i=2; i<=n; i++)
            fin[i][i-1+1*(i>=xplace+1)]='x';
        for (int j=2; j<n; j++)
        {
            if (fin[n][j]=='.')
                fin[n][j]='+';
            else
                fin[n][j]='o';
        }
        vector <pair <int,int> > ret;
        int score=0;
        for (int i=1; i<=n; i++)
            for (int j=1; j<=n; j++)
            {
                if (fin[i][j]!='.')
                    score++;
                if (fin[i][j]=='o')
                    score++;
                if (fin[i][j]!=base[i][j])
                    ret.push_back(make_pair(i,j));
            }
        printf("Case #%d: %d %d\n",itr,score,ret.size());
        for (int i=0; i<(int)ret.size(); i++)
            printf("%c %d %d\n",fin[ret[i].first][ret[i].second],ret[i].first,ret[i].second);
    }
}
