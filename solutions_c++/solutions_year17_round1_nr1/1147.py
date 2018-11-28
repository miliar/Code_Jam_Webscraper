#include<stdio.h>
#include<string.h>
#include<iostream>
#include<algorithm>
#include<math.h>
#include<map>
#include<vector>
#include<string>
#include<set>
#include<queue>
#define MP(x,y) make_pair(x,y)
#define clr(x,y) memset(x,y,sizeof(x))
#define forn(i,n) for(int i=0;i<n;i++)
#define sqr(x) ((x)*(x))
#define MAX(a,b) if(a<b) a=b;
#define ll long long
using namespace std;

int n, m;
char a[30][30];

int main() {
    //freopen("in","r",stdin);
    freopen("/home/zyc/Downloads/in","r",stdin);
    freopen("/home/zyc/Downloads/out","w",stdout);
    int T;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; cas++)
    {
        scanf("%d%d", &n, &m);
        for(int i = 0; i < n; i++) scanf("%s", a[i]);
        int row_last = -1;
        for(int i = 0; i < n; i++)
        {
            bool has = false;
            for(int j = 0; j < m; j++) if(a[i][j] != '?') has = true;
            if(!has) continue;

            int col_last = -1;
            for(int j = 0; j < m; j++)
            {
                if(a[i][j] != '?')
                {
                    for(int k = row_last + 1; k <= i; k++)
                    {
                        for(int l = col_last + 1; l <= j; l++)
                        {
                            a[k][l] = a[i][j]; 
                        }
                    }
                    col_last  = j;
                }
            }
            if(col_last != m - 1)
            {
                for(int k = row_last + 1; k <= i; k++)
                {
                    for(int l = col_last + 1; l < m; l++)
                    {
                        a[k][l] = a[i][col_last];
                    }
                }
            }
            row_last = i;
        }
        for(int i = row_last + 1; i < n; i++)
        {
            for(int j = 0; j < m; j++)
            {
                if(a[i][j] == '?') a[i][j] = a[i - 1][j];
            }
        }
        printf("Case #%d:\n", cas);
        for(int i = 0; i < n; i++) printf("%s\n", a[i]);
    }
    return 0;
}
