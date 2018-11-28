#include<bits/stdc++.h>
using namespace std;
void f(long long int N , int (&d)[32] , int &ndig)
{
  int i , j;
  ndig = 0;
  while(N != 0)
  {
    d[++ndig] = N%10;
    N = N/10;
  }
  for(i=1,j=ndig;i<j;i++,j--)
  {
    swap(d[i],d[j]);
  }
  return;
}
int main()
{
  ios_base::sync_with_stdio(false);
  int T , t;
  long long int N;
  int i , j , ndig , d[32]={0};
  cin >> T;
  for(t = 1 ; t<= T; t++)
  {
    cin >> N;
    f(N,d,ndig);
    /*for(i=1;i<=ndig;i++)
      cout << d[i];
    cout << endl;*/
    for(i=1;i<ndig;i++)
    {
      if(d[i] > d[i+1])
      {
        for(j=i;j>=1;j--)
        {
          if(d[j] > d[j-1]) break;
        }
        d[j]--;
        for(j=j+1;j<=ndig;j++)
          d[j] = 9;
        break;
      }
    }
    N = 0;
    for(i=1;i<=ndig;i++)
      N = N*10 + (long long)d[i];
    cout << "Case #" << t  << ": " << N << "\n";
  }
  return 0;
}
