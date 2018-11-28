#include<iostream>
#include<cstdio>

using namespace std;

int a[100];


int main()
{
  freopen("b.in.txt","r",stdin);
  freopen("b.out","w",stdout);
  int t;
  scanf("%d", &t);
  char c,cc;
  
      scanf("%c", &c);
  for (int i = 0; i < t; i++)
    {
      
      scanf("%c", &c);
      int n = 0;
      while (c <= '9' && c >= '0')
	{
	  a[n] = c-'0';
	  n++;
	  scanf("%c", &c);
	}
      for (int p = 0; p < 20; p++)
	{
      for (int k = 0; k < n-1; k++)
	if (a[k] > a[k+1])
	  {
	    for (int j = k+1; j < n; j++) a[j] = 9;
	    a[k]--;
	    break;
	  }
	}
      cout << "Case #" << i+1 << ": ";
      for (int k =0 ;k < n; k++) if (a[k] !=0) cout << a[k];
      cout << endl;
    }
}
