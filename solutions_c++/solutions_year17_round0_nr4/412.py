#include<iostream>
#include<cstdio>

using namespace std;

int a[200][200];
int b[200][200];
int c[200][200];
int d[400];
int e[400];

int main()
{
  freopen("d.in.txt","r",stdin);
  freopen("d.out","w",stdout);
  int t;
  scanf("%d", &t);
  int n,m;

  for (int tt = 0; tt < t; tt++)
    {
      scanf("%d %d", &n,&m);
      memset(a,0,sizeof(a));
      memset(b,0,sizeof(b));
      memset(c,0,sizeof(c));
      for (int i = 0; i < m; i++)
	{
	  char c;
	  scanf("%c",&c);
	  scanf("%c",&c);
	  int x,y;
      scanf("%d %d", &x,&y);
	  x--;y--;
	  if (c == 'x' || c == 'o') a[x][y]=1;
	  if (c == '+' || c == 'o') b[x][y]=1;
	}
      memset(d,0,sizeof(d));
      memset(e,0,sizeof(e));
      for (int i = 0; i < n; i++)
	for (int j = 0; j < n; j++) if (a[i][j] == 1)
				      {
					d[i] = 1;
					e[j] = 1;
				      }
      int p = 0;
      int q = 0;
      while (p < n && q < n)
	{
	  while (p < n && d[p] == 1) p++;
	  while (q < n && e[q] == 1) q++;
	  if (p <n && q < n) 
	    {
	      a[p][q] = 1;
	      c[p][q] = 1;
	    }
	  p++;
	  q++;
	}
      memset(d,0,sizeof(d));
      memset(e,0,sizeof(e));
      for (int i = 0; i <n ; i++)
	for (int j = 0; j < n; j++)
	  if (b[i][j] == 1)
	    {
	      d[i + j] = 1;
	      e[i-j+n] = 1;
	    }
      for (int i = 0; i < n + n - 1; i++)
	if (d[i] == 0){
	  int fl = -1;
	  int jj = 0;
	  for (int j = 1; j < n + n ; j++)
	    if (e[j] == 0 && (j+i-n)%2 == 0)
	      {
		int x = (i+j-n)/2;
		int y = (i-j+n)/2;
		if (x >= 0 && x < n && y >=0 && y < n)
		  {
		    int u  = j-n;
		    if (u <0) u= -u;
		    if (u > fl)
		      {
			jj=j;
			fl =u;
		      }
		  }
	      }
	  if (fl != -1) 
	    {
	      //cout << i << " " << jj << " " << fl << endl;
	      e[jj] = 1;
		int x = (i+jj-n)/2;
		int y = (i-jj+n)/2;
		b[x][y] =1;
		c[x][y]=1;
	    }
	}
      int ans = 0;
      int aa = 0;
      for (int i= 0; i < n; i++)
	for (int j = 0; j < n; j++) 
	  {
	    ans+= a[i][j] + b[i][j];
	    aa += c[i][j];
	  }
      cout << "Case #" << tt+1 << ": "<< ans << " " << aa << endl;
      for (int i = 0; i<n ;i++)
	for (int j = 0; j < n; j++)
	  if (c[i][j] == 1){
	    if (a[i][j] + b[i][j] == 2) cout << "o";
	    if (a[i][j] == 0 && b[i][j] == 1) cout << "+";
	    if (a[i][j] == 1 && b[i][j] == 0) cout << "x";
	    cout << " " << i+1 << " " << j+1 << endl;
	  }
      
    }
}
