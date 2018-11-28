#include<iostream>
#include<cstdio>
using namespace std;

int s[1001][1001];

int n,c,m;
int b[2000];

int check(int a)
{
    memset(b,0,sizeof(b));
    int lef = 0;
    int ret = 0;
    for (int i = 1; i <= n; i++)
    {
        int ss =0;
        
        for (int j = 1; j<= c; j++)
        {
            if (s[i][j] > a - b[j]) return -1;
            ss += s[i][j];
            b[j] += s[i][j];
                    }
                    if (ss > a) ret += ss - a;
                    lef = lef + a - ss;
                    if (lef <0 ) return -1;
        
                    
    }
                    return ret;
}

int main()
{

  freopen("b.in.txt","r",stdin);
  freopen("b.out","w",stdout);
  int tt;
  scanf("%d", &tt);
  for (int t = 0; t< tt; t++)
  {
      scanf("%d %d %d", &n, &c, &m);
      memset(s,0,sizeof(s));
      for (int i = 0; i < m; i++)
      {
          int x,y;
          scanf("%d %d", &x, &y);
          s[x][y]++;
      }
      int l; int r;
      l = 1; r = m;
      while (l != r)
      {
          int mid = (l+r)/ 2;
          int ret = check(mid);
          if (ret == -1) l = mid + 1; else r = mid;
      }
                    printf("Case #%d: %d %d\n", t+1,l,check(l));
  }
}
