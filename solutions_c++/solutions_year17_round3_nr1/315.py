#include <iostream>
#include <cstdio>
#include <cmath>
#include <unordered_map>
using namespace std;

int N,K;
int R[2000],H[2000];

void read()
{
  cin >> N >> K;
  for(int n=0;n<N;n++)
    cin >> R[n] >> H[n];
}

void sort()
{
  for(int i=0;i<N;i++)
    {
      int max = i;
      for(int j=i+1;j<N;j++)
	if(R[j]>R[max])
	  max=j;
      int tmp = R[i];
      R[i] = R[max];
      R[max]=tmp;
      tmp = H[i];
      H[i]=H[max];
      H[max]=tmp;
    }
}

double area(int r)
{
  return M_PI*r*r;
}

double side(int r,int h)
{
  return 2*M_PI*r*h;
}

unordered_map<long long int,double> M;

long long int code(int a,int b)
{
  return (((long long int)a)<<32) | ((long long int)b);
}

double solve(int i,int k)
{
  auto key = code(i,k);
  if(M.find(key)!=M.end())
    return M[key];
  if(i==N && k!=0)
    return -10000.0;
  if(k==0)
      return 0;
  double rst = solve(i+1,k);
  double alt = side(R[i],H[i])+solve(i+1,k-1);
  if(k==K)
    alt+=area(R[i]);
  
  if(alt>rst)
    rst=alt;
  
  M[key]=rst;
  return rst;
}

double solve()
{
  sort();
  M.clear();
  return solve(0,K);
}

int main()
{
  int T;
  cin >> T;
  for(int t=1;t<=T;t++)
    {
      read();
      printf("Case #%d: %.9lf\n",t,solve());
    }
  return 0;
}
