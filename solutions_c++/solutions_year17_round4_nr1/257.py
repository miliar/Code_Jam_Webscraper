#include<iostream>
#include<cstdio>
using namespace std;

int a[100];
int f[101][101][101];
int main()
{

  freopen("a.in.txt","r",stdin);
  freopen("a.out","w",stdout);
  int tt;
  scanf("%d", &tt);
  for (int t = 0; t< tt; t++)
    {
      int n,p;
      scanf("%d %d", &n, &p);
      memset(a,0,sizeof(a));
      printf("Case #%d: ", t+1);
      for (int i = 0; i < n; i++)
	{
	  int x;
	  scanf("%d", &x);
	  x = x %p;
	  a[x]++;
	}
      int ret = 0;
      ret += a[0];
      if (p == 2)
	{
	  ret += (a[1]+1)/2;
	}
      if (p == 3)
	{
	  int m = a[1];
	  if (a[2] < a[1]) m = a[2];
	  ret += m;
	  m = a[1] + a[2] - m - m;
	  ret += (m + 2)/3;
	}
      if (p == 4)
	{
	  memset(f,0,sizeof(f));
		 f[0][0][0] = 0;
		 for (int i = 0; i <= a[1]; i++)
		   for (int j = 0; j <= a[2]; j++)
		     for (int k = 0; k <= a[3] ;k++)
		       {
			 int s = i + j*2+ k*3;
			 s= s%4;
			 int u = 0;
			 if (s==0) u = 1;
			 if (i < a[1])
			   {
			     if (f[i+1][j][k] < f[i][j][k] + u) f[i+1][j][k] = f[i][j][k] + u;
		      
			   }

			 if (j < a[2])
			   {
			     if (f[i][j+1][k] < f[i][j][k] + u) f[i][j+1][k] = f[i][j][k] + u;
		      
			   }

			 if (k < a[3])
			   {
			     if (f[i][j][k+1] < f[i][j][k] + u) f[i+1][j][k+1] = f[i][j][k] + u;
		      
			   }
		       }
		 ret+= f[a[1]][a[2]][a[3]];
	}
      printf("%d\n", ret);
    }
}
