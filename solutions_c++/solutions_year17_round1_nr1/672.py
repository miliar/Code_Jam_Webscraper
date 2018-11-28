#include<bits/stdc++.h>
#define y0 asdasdasdsas
#define y1 asdsadasdasd
using namespace std;

int i_mn[27];
int i_mx[27];
int j_mn[27];
int j_mx[27];

int a[27][27];
int u[27];
int n,m;

bool ex(int c, int di, int dj)
{
    int ni = (di<0?i_mn[c]:i_mx[c]) + di;
    if(ni>=0 && ni<n && di)
    {
        bool ok = true;
        for(int j=j_mn[c];j<=j_mx[c] && ok;++j)
            if(a[ni][j]>-1)
                ok=false;
        if(ok)
        {
            for(int j=j_mn[c];j<=j_mx[c] && ok;++j)
                a[ni][j] = c;
            i_mn[c] = min(i_mn[c], ni);
            i_mx[c] = max(i_mx[c], ni);
            return true;
        }
    }


    int nj = (dj<0?j_mn[c]:j_mx[c]) + dj;
    if(nj>=0 && nj<m && dj)
    {
        bool ok = true;
        for(int i=i_mn[c];i<=i_mx[c] && ok;++i)
            if(a[i][nj]>-1)
                ok=false;
        if(ok)
        {
            for(int i=i_mn[c];i<=i_mx[c] && ok;++i)
                a[i][nj] = c;
            j_mn[c] = min(j_mn[c], nj);
            j_mx[c] = max(j_mx[c], nj);
            return true;
        }
    }

    return false;
}





int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin.tie(0);ios_base::sync_with_stdio(0);
    int T;
    cin >> T;
    for(int test=1;test<=T;test++)
    {
        printf("Case #%d:\n",test);
        cin >> n >> m;


        for(int j=0;j<26;++j)
            j_mn[j] = m,
            j_mx[j] = -1,
            i_mn[j] = n,
            i_mx[j] = -1;


        memset(u,0,sizeof(u));

        for(int i=0;i<n;++i)
        {
            string s;
            cin >> s;
            for(int j=0;j<m;++j)
            {
                if(s[j]=='?')
                    continue;
                int c = s[j]-'A';
                u[c]=1;
                i_mn[c] = min(i_mn[c], i);
                i_mx[c] = max(i_mx[c], i);
                j_mn[c] = min(j_mn[c], j);
                j_mx[c] = max(j_mx[c], j);
            }
        }

        memset(a,-1,sizeof(a));

        for(int c=0;c<26;++c)
        {
            if(!u[c])
                continue;
            for(int i=i_mn[c];i<=i_mx[c];++i)
                for(int j=j_mn[c];j<=j_mx[c];++j)
                    a[i][j]=c;
        }

        bool iter = true;
        while(iter)
        {
           iter=false;

            for(int i=0;i<n;++i)
            {
                for(int j=0;j<m;++j)
                {
                    if(a[i][j]>-1)
                        continue;
                    if(i && a[i-1][j]>-1)
                    {
                        while(ex(a[i-1][j],1,0)) iter=true;
                    }
                    if (j && a[i][j-1]>-1)
                    {
                        while(ex(a[i][j-1],0,1)) iter=true;
                    }
                }

                for(int j=m-1;j>=0;--j)
                {
                    if(a[i][j]>-1)
                        continue;
                    if(i && a[i-1][j]>-1)
                    {
                        while(ex(a[i-1][j],1,0)) iter=true;
                    }
                    if (j<m-1 && a[i][j+1]>-1)
                    {
                        while(ex(a[i][j+1],0,-1)) iter=true;
                    }
                }

            }

            for(int i=n-1;i>=0;--i)
            {
                for(int j=0;j<m;++j)
                {
                    if(a[i][j]>-1)
                        continue;
                    if(i<n-1 && a[i+1][j]>-1)
                    {
                        while(ex(a[i+1][j],-1,0)) iter=true;
                    }
                    if (j && a[i][j-1]>-1)
                    {
                        while(ex(a[i][j-1],0,1)) iter=true;
                    }
                }

                for(int j=m-1;j>=0;--j)
                {
                    if(a[i][j]>-1)
                        continue;
                    if(i<n-1 && a[i+1][j]>-1)
                    {
                        while(ex(a[i+1][j],-1,0)) iter=true;
                    }
                    if (j<m-1 && a[i][j+1]>-1)
                    {
                        while(ex(a[i][j+1],0,-1)) iter=true;
                    }
                }

            }

        }


        for(int i=0;i<n;++i)
        {
            for(int j=0;j<m;++j)
                printf("%c",'A'+a[i][j]);
            printf("\n");
        }

    }

}

