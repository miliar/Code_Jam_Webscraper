#include<iostream>
#include<cstdio>

using namespace std;

int a[2000];
int b[2000];

int main()
{
  freopen("a.in.txt","r",stdin);
  freopen("a.out","w",stdout);
  int t;
  scanf("%d", &t);
  for (int i = 0; i < t; i++)
    {
      char c;
      scanf("%c", &c);
      scanf("%c", &c);
      int n = 0;
      
      memset(b,0,sizeof(b));
      while (c != ' ')
	{
	  if (c == '+') a[n] = 0; else a[n] = 1;
	  n++;
	  scanf("%c", &c);
	}
      int k;
      scanf("%d", &k);
      int s = 0;
      int ans = 0;
      int f = 0;
      
      for (int i = 0; i < n; i++)
	{
	  if (i >= k) s += b[i-k];
	   b[i] = (a[i] + s)%2;
	   ans += b[i];
	   s+= b[i];
	   if (i > n-k && b[i] != 0) f = 1;
	}
      cout << "Case #" << i+1 << ": ";
      if (f == 1) cout << "IMPOSSIBLE\n"; else cout << ans << endl;
    }
}
