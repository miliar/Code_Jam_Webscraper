#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text

int count(int n)
{
	if(n < 10)
	return n;
	else
	{
		for(int k=n;k>=0;k--)
		{
			
		
			int c,d1,d2,r,x;
			r=k;x=0;
			c=0;
			d1=r%10;
			
			while(r!=0)
			{
				r=r/10;
				d2=r%10;
				if(d2>d1)
					c=1;
				
				d1=d2;
			}
			if(c!=1)
			return k;
		}
		
	}
}
int main() {
	freopen("B-small-attempt4.in","r",stdin);
	freopen("B-small-attempt4.out","w",stdout);
  int t, n,m;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> n ;  // read n and then m.
    m=count(n);
    cout << "Case #" << i << ": " <<m << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
  return 0;
}


