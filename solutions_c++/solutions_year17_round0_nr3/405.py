#include<iostream>
#include<cstdio>

using namespace std;

int a[100];


int main()
{
  freopen("c.in.txt","r",stdin);
  freopen("c.out","w",stdout);
  int t;
  scanf("%d", &t);
  long long n,k;
  long long a,b,c,d;
  long long aa,bb,cc,dd;
  for (int tt = 0; tt < t; tt++)
    {
      scanf("%lld%lld", &n, &k);
      a = n;
      b = 1;
      c = 0;
      d = 0;

      cout << "Case #" << tt+1 << ": ";
      while (k > 0)
	{
	  k-= b;
	  if (k <= 0)
	    {
	      cout << a/2 << " " << (a-1)/2 << endl;
	      break;
	    }
	  k-= d;
	  if (k <= 0)
	    {
	      cout << c/2 << " " << (c-1)/2 << endl;
	      break;
	    }
	  if (a % 2 == 0)
	    {
	      aa = a / 2; cc = (a-1)/2;
	      bb = b;
	      dd = b + d * 2;
	    }
	  else {
	    aa = (a-1)/2; cc = aa-1;
	    bb = b * 2 + d;
	    dd = d;
	  }
	  a = aa;
	  b = bb;
	  c = cc;
	  d = dd;
	}
    }
}
