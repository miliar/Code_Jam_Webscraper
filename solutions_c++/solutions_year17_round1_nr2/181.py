#include<iostream>
#include<cstdio>

using namespace std;

int a[100][100];
int n,p;
int c[100];
int b[100];
double eps = 1e-9;

int main()
{
  freopen("b.in.txt","r",stdin);
  freopen("b.out","w",stdout);
  int t;
  scanf("%d", &t);
  
    
  for (int tt = 0; tt < t; tt++)
    {
        scanf("%d %d", &n, &p);
        for (int i = 0; i < n; i++) scanf("%d", &b[i]);
            for (int i = 0; i < n; i++)
                for (int j = 0; j < p; j++)scanf("%d", &a[i][j]);
            int ans = 0;
            for (int i = 0; i < n; i++)
                for (int j = 0; j < p; j++)
                    for (int k = j+1; k <p; k++)
                            if (a[i][j] > a[i][k])
                            {
                                int pt = a[i][j];
                                a[i][j] = a[i][k];
                                a[i][k] =pt;
                            }
            memset(c,0,sizeof(c));
        
    while (true)
    {
        bool flag = false;
        for (int i = 0; i < n; i++) if (c[i] == p){ flag =true;break;}
        if (flag == true) break;
        int ii = 0;
        double s = 100000000;
        for (int i = 0; i < n; i++)
        {
            double ss = (double)a[i][c[i]] / b[i];
            if (ss < s)
            {
                s = ss;
                ii = i;
            }
        }
        flag = true;
        s = s / 0.9;
        int sa = (int) (s + eps);
        if (sa > s) sa--;
        //cout << sa << " " << s << " " << ii << endl;
        for (int i = 0; i < n; i++)
        {
            double ss = (double)a[i][c[i]] / b[i];
          //  cout << ss << endl;
            if (ss > ((double)sa) * 1.1 + eps) flag =false;
        }
        if (flag == true)
        {
            ans++;
            for (int i = 0; i < n;i++) c[i] ++;
        }
        else c[ii]++;
    }
      cout << "Case #" << tt+1 << ": "  << ans <<endl;
    }
}
