#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

int A[100][100];
int R[100];
int N,P;

void read()
{
  cin >> N >> P;
  for(int i=0;i<N;i++)
    cin >> R[i];
  for(int i=0;i<N;i++)
    for(int j=0;j<P;j++)
      cin >> A[i][j];
  
}


pair<int,int> findK(int Q,int r)
{
  int a = (int)ceil(Q/1.1/r);
  int b = (int)floor(Q/0.9/r);
  if(b>=a)
    return pair<int,int>(a,b);
  return pair<int,int>(-1,-1);
}

int solveOne()
{
  int rst =0;
  for(int i=0;i<P;i++)
    {
      int Q = A[0][i];
      int r = R[0];
      if(findK(Q,r).first>0)
	rst++;
    }
  return rst;
}

int solveTwo()
{
  int Arr[P];
  for(int i=0;i<P;i++)
    Arr[i]=i;
  int best = 0;
  do
    {
      int rst =0;
      for(int i=0;i<P;i++)
	{
	  pair<int,int> x = findK(A[0][i],R[0]);
	  pair<int,int> y = findK(A[1][Arr[i]],R[1]);
	  if(x.first<=0 || y.first<=0)
	    continue;
	  int a = x.first,b=x.second,c = y.first,d = y.second;
	  if((a<=c && b>=c) || (c<=a && d>=a))
	    rst++;
	}
      if(rst>best)
	best=rst;
  } while (next_permutation(Arr,Arr+P) );
  return best;
}


int solve()
{
  if(N==1)
    return solveOne();
  return solveTwo();
}


int main()
{
  int T;
  cin >> T;
  for(int t=1;t<=T;t++)
    {
      read();
      cout << "Case #"<<t<<": " << solve()  << endl;
    }
  return 0;
}
