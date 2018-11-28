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
char s[105][105];
char t[105][105];

int main() {
    //freopen("in","r",stdin);
    freopen("/home/zyc/Downloads/in","r",stdin);
    freopen("/home/zyc/Downloads/out","w",stdout);
    int T;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; cas++)
    {
        scanf("%d%d", &n, &m);
        for(int i = 0; i < n; i++) for(int j = 0; j < n; j++) s[i][j] = '.';
        for(int i = 0; i < m; i++)
        {
            char ch[2];
            int x, y;
            scanf("%s%d%d", ch, &x, &y);
            s[x - 1][y - 1] = ch[0];
        }
        printf("Case #%d: ", cas);
        if(n == 1)
        {
            printf("2 ");
            if(s[0][0] != 'o') 
            {
                printf("1\n");
                printf("o 1 1\n");
            }
            else printf("0\n");
        }
        else
        {
            printf("%d ", 3 * n - 2);
            for(int i = 0; i < n; i++) for(int j = 0; j < n; j++) t[i][j] = s[i][j];

            int p = -1;
            for(int i = 0; i < n; i++)
            {
                if(t[0][i] == '.') t[0][i] = '+';     
                else if(t[0][i] == 'x') t[0][i] = 'o', p = i;
                else if(t[0][i] == 'o') p = i;
            }
            if(p == -1)
            {
                t[0][0] = 'o';
                p = 0;
            }
            for(int i = 1; i < n - 1; i++) t[n - 1][i] = '+';
            int q;
            if(p == 0) q = n - 1; 
            else q = 0;

            t[n - 1][q] = 'x';
            for(int i = 1, j = 0; i < n - 1; i++)
            {
                while(j == p || j == q) j++;
                t[i][j] = 'x';
                j += 1;
            }

            int c = 0;
            for(int i = 0; i < n; i++) for(int j = 0; j < n; j++) if(t[i][j] != s[i][j]) c+=1;
            printf("%d\n", c);
            //for(int i = 0; i < n; i++)
            //{
            //    for(int j = 0; j < n; j++)
            //    {
            //        printf("%c", t[i][j]); 
            //    }
            //    printf("\n");
            //}
            for(int i = 0; i < n; i++) for(int j = 0; j < n; j++) if(t[i][j] != s[i][j]) printf("%c %d %d\n", t[i][j], i + 1, j + 1);
        }
    }
    return 0;
}
