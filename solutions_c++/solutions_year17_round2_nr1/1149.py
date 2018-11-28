#include <iostream>
#include <cstdio>
#include <cmath>
#define MAX_N 1500
using namespace std;

int N,D;
int S[MAX_N],K[MAX_N];

void read()
{
  cin >> D >> N;
  for(int i=0;i<N;i++)
    cin >> K[i] >> S[i];
}

double solve()
{
  double rst = pow(10,20);
  for(int i=0;i<N;i++)
    {
      double tmp = 1.0*D*S[i]/(D-K[i]);
      if(tmp<rst)
	rst=tmp;
    }
  return rst;
}

int main()
{
  int T;
  cin >> T;
  for(int t=1;t<=T;t++)
    {
      read();
      printf("Case #%d: %.7lf\n",t,solve());
    }
  return 0;
}
