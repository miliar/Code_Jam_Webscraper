#include<iostream>
#include<cstdio>
using namespace std;

int f[100][300];
int s[100][300];
int pre[100][300];

char g[300][300];

int b[10];
char h[10];
int sh[10];
int nb[10];

int r,c;

int two(int x)
{
    int ret = 1;
    for (int i = 0; i < x; i++) ret = ret *2;
    return ret;
}


int thr(int x)
{
    int ret = 1;
    for (int i = 0; i < x; i++) ret = ret *3;
    return ret;
}

void pr(int x, int y)
{
    if (x == 0) return;
    pr(x-1,pre[x][y]);
    //cout << x <<  " " << y << " " << s[x][y] << endl;
    int z = s[x][y];
    for (int i = 0 ; i < r; i++)
    {
        if (z % 2== 1 && g[i][x-1] == '-')g[i][x-1] = '|';
        else{
            if (z % 2 == 1 && g[i][x-1] == '|') g[i][x-1] = '-';}
        z = z /2;
    }
}
int main()
{

  freopen("c.in.txt","r",stdin);
  freopen("c.out","w",stdout);
  int tt;
  scanf("%d", &tt);
  for (int t = 0; t< tt; t++)
    {
        scanf("%d %d\n", &r, &c);
        for (int i = 0; i < r; i++){
            
        
            for (int j = 0; j < c; j++)
                scanf("%c", &g[i][j]);
            scanf("\n");
        }
        memset(f,0,sizeof(f));
        f[0][0] = 1;
        for (int i = 0; i < c; i++)
            for (int j = 0; j < 300; j++)
                if (f[i][j] == 1)
                {
                    int x = j;
                    for (int k =0; k < r; k++)
                    {
                        b[k] = x % 3;
                        x = x / 3;
                    }
                    for (int l = 0; l < two(r); l++)
                    {
                        x = l;
                        for (int k = 0; k< r; k++)
                        {
                            h[k] = g[k][i];
                            if (x% 2 ==1 && g[k][i] == '-') h[k] = '|';
                            
                            if (x% 2 ==1 && g[k][i] == '|') h[k] = '-';
                            x = x/ 2;
                        }
                        int flag = 1;
                        memset(sh,0,sizeof(sh));
                        for (int k = 0; k < r; k++)
                            if (h[k] == '|')
                            {
                                int p = k-1;
                                while (p >= 0)
                                {
                                    if (h[p] == '#') break;
                                    sh[p] = 1;
                                    p--;
                                }
                                p = k+1;
                                while (p < r)
                                {
                                    if (h[p] == '#') break;
                                    sh[p] = 1;
                                    p++;
                                }
                            }
                        for (int k = 0; k < r; k++)
                        {
                            if (h[k] == '#')
                            {
                                if (b[k] == 2) flag  = -1;
                                nb[k] = 0;
                            }
                            if (h[k] == '.')
                            {
                                if (sh[k] == 1) nb[k] = b[k]; else
                                {
                                    
                                nb[k] = b[k];
                                    if (nb[k] == 0) nb[k] = 2;
                                    if (i > 0)
                                        if (nb[k] == 2 && (g[k][i-1] == '|' || g[k][i-1] == '-')) flag = -1;
                                }
                            }
                            if (h[k] == '|')
                            {
                                if (sh[k] == 1 || b[k] == 1) flag = -1;
                                if (b[k] == 2) flag = -1;
                                nb[k] = 0;
                            }
                            if (h[k] == '-')
                            {
                                if (sh[k] == 1 || b[k] == 1) flag = -1;
                                nb[k] = 1;
                                
                                if (i > 0)
                                    if ((g[k][i-1] == '|' || g[k][i-1] == '-')) flag = -1;
                            }
                        }
                        if (flag == 1)
                        {
                            int o = 0;
                            for (int k = r-1; k >= 0; k--) o = o * 3 + nb[k];
                            f[i+1][o] = 1;
                            pre[i+1][o] = j;
                            s[i+1][o] = l;
                        }
                    }
                }
        int ans = -1;
        for (int i = 0; i < 300; i++)
            if (f[c][i] == 1)
            {
                int flag = 0;
                int x = i;
                while (x != 0)
                {
                    if (x % 3 == 2) flag =1;
                    x = x/3;
                }
                if (flag == 0) ans = i;
            }
        //printf("%d\n", ans);
        if (ans == -1) printf("Case #%d: IMPOSSIBLE\n",t+1); else
        {
            pr(c,ans);
            printf("Case #%d: POSSIBLE\n",t+1);
            
            for (int i = 0 ; i < r; i++){
                for (int j = 0; j < c; j++) printf("%c", g[i][j]);
                printf("\n");
            }
        }
    }
}
