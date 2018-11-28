#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <utility>
using namespace std;
using LL = long long int;


int N,P;
int G[1000];

void read()
{
  cin >> N >> P;
  for(int i=0;i<N;i++)
    cin >> G[i];
}

int solve2()
{
  int E=0,O=0;
  for(int i=0;i<N;i++)
    if(G[i]%2==0)
      E++;
    else
      O++;
  return E+(O+1)/2;
}

int solve3()
{
  int M0=0,M1=0,M2=0;
  for(int i=0;i<N;i++)
    if(G[i]%3==0)
      M0++;
    else if((G[i]-1)%3==0)
      M1++;
    else
      M2++;
  int min = M1<M2?M1:M2;
  int max = M1+M2-min;
  return M0+min+(max-min+2)/3;
}

int bruteForce4()
{
  int T[N];
  for(int i=0;i<N;i++)
    T[i]=G[i];
  sort(T,T+N);
  int best = 0;
  do {
    int f=0;
    int l=0;
    for(int i=0;i<N;i++)
      {
	if(l==0)
	  f++;
	l = 4*((T[i]-l+3)/4)-(T[i]-l);
      }

    if(f>best)
      {
      best = f;
      /* for(int i=0;i<N;i++)
	  cout << (T[i]%4) << " ";
	cout << endl;*/
      }
  } while ( next_permutation(T,T+N) );
  return best;
}

int solve4()
{
  int M0=0,M1=0,M2=0,M3=0;
  for(int i=0;i<N;i++)
    if(G[i]%4==0)
      M0++;
    else if((G[i]-1)%4==0)
      M1++;
    else if((G[i]-2)%4==0)
      M2++;
    else
      M3++;
  int min = M1<M3?M1:M3;
  int rst = M0+min;
  int left = M1+M3-2*min;

  int best = 0;
  for(int i=0;i<=M2/2;i++)
  {
    int tmp = i;
    int M2x = M2-2*i;
    int leftx=left;
    int n = M2x;
    if(leftx/2<n)
      n=leftx/2;
    tmp+=n;
    M2x-=n;
    leftx-=2*n;
    tmp+=(leftx+3+M2x)/4;
    if(tmp>best)
      best=tmp;
  }
  rst+=best;
  return rst;
}

int solve()
{
  if(P==2)
    return solve2();
  else if(P==3)
    return solve3();
  else
    return solve4();
}

int main()
{
  int T;
  cin >> T;
  for(int t=1;t<=T;t++)
  {
    read();
    cout << "Case #" << t << ": " << solve() << endl;
  }
  return 0;
}
