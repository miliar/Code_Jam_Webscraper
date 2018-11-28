#include<iostream>
#include<cstdio>

using namespace std;

int a[2000][2000];
int b[2000];

int main()
{
  freopen("a.in.txt","r",stdin);
  freopen("a.out","w",stdout);
  int t;
  scanf("%d", &t);
  int n,m;
  for (int tt= 0; tt < t; tt++)
    {
        scanf("%d %d", &n, &m);
        char ch;
        scanf("%c", &ch);
        for (int i = 0 ; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                scanf("%c", &ch);
                    if (ch >= 'A' && ch <= 'Z') a[i][j] = ch - 'A'+1; else a[i][j] = 0;
            }
                scanf("%c", &ch);
        }
            memset(b,0,sizeof(b));
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < m; j++) if (a[i][j] != 0) b[i] = i+1;
            }
            for (int i = 1; i < n; i++)
                if (b[i] == 0 && b[i-1] != 0) b[i] = b[i-1];
            for (int i = n-2; i >=0 ; i--) if (b[i] == 0 && b[i+1] != 0) b[i] = b[i+1];
            for (int i = 0; i < n; i++)
                if (b[i] == i+1)
                {
                    for (int j = 1; j < m ;j++) if (a[i][j] == 0 && a[i][j-1] != 0) a[i][j] = a[i][j-1];
                    for (int j = m-2; j>=0 ;j--) if (a[i][j] == 0 && a[i][j+1] != 0) a[i][j] = a[i][j+1];
                }
            for (int i = 0; i < n; i++)
                if (b[i]!= i+1)
                {
                    for (int  j = 0; j <m;j++) a[i][j] = a[b[i]-1][j];
                }
        cout << "Case #" << tt+1 << ":\n";
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < m; j++)
                {
                    char cc = 'A' + a[i][j]-1;
                    cout << cc;
                }
                cout << endl;
            }
    }
}
