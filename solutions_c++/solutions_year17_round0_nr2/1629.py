#include <iostream>
using namespace std;
using LL = unsigned long long int;

LL n;
LL add;

LL POWERS_OF_10[19];
LL STREAM_OF_1S[19];

void read()
{
  cin >> n;
}

void findD(int d)
{
  for(int k=9;k>=0;k--)
    {
      if(add+k*STREAM_OF_1S[d]<=n)
	{
	  add+=k*POWERS_OF_10[d];
	  return;
	}
    }
}

LL solve()
{
  add=0L;
  for(int i=18;i>=0;i--)
    findD(i);
  return add;
}

void init()
{
  LL p = 1;
  LL acc = 0;
  for(int i=0;i<=18;i++)
    {
      POWERS_OF_10[i]=p;
      acc+=p;
      STREAM_OF_1S[i]=acc;
      p*=10;
    }
}


int main()
{
  init();
  int T;
  cin >> T;
  for(int t=1;t<=T;t++)
    {
      read();
      cout << "Case #"<< t <<": " << solve() << endl;
    }
  return 0;
}
