#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

int N;
int E[1000],S[1000];
int D[1000];
void read()
{
  int g;
  cin >> N >> g;
  for(int i=0;i<N;i++)
    cin >> E[i] >> S[i];
  for(int i=0;i<N;i++)
    for(int j=0;j<N;j++)
      {
	cin >> g;
	if(g!=-1)
	  D[i]=g;
      }
  cin >> g;
  cin >> g;
}

double solve()
{
  double OPT[N];
  OPT[N-1]=0;
  for(int c=N-2;c>=0;c--)
  {
    double min = pow(10,20);
    int e = E[c],s=S[c];
    double acc = 0;
    for(int i=c+1;i<N;i++)
      {
	acc+=D[i-1];
	if(acc>e)
	  break;
	double tmp = acc/s + OPT[i];
	if(tmp<min)
	  min=tmp;
      }
    OPT[c]=min;
  }
  return OPT[0];
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
