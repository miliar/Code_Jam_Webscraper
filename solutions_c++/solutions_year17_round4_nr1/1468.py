#include  <bits/stdc++.h>
#define FOR(i,n) for(int i=0;i<(int)n;i++)
#define ALL(v) v.begin(),v.end()
#define UNIQUE(c) (c).resize(distance((c).begin(), unique(ALL(c))))
using namespace std;

typedef long long int LL;
typedef long long unsigned int LLU;

typedef vector<int>   VI;       typedef vector<bool> VB;
typedef vector<VI>   VVI;       typedef vector<double> VD;
typedef vector<VVI> VVVI;       typedef vector<VD> VDD;

typedef pair<int,int> PI;       typedef pair<double,double> PD;
typedef pair<PI,int> PII;


#define MAXI 100

int dyn2[2*MAXI+1];
int dyn3[2*MAXI+1][2*MAXI+1];
int dyn4[2*MAXI+1][2*MAXI+1][2*MAXI+1];

int solve2(int x1)
{
  if (dyn2[x1] != -1)
    return dyn2[x1];
  
  if (x1 == 0)
    return 0;
  
  dyn2[x1] = 1;
  
  if (x1 >= 2) dyn2[x1] = max(dyn2[x1], solve2(x1-2)+1);
  
  return dyn2[x1];
}

int solve3(int x1, int x2)
{
  if (dyn3[x1][x2] != -1)
    return dyn3[x1][x2];
  
  if (x1 == 0 && x2 == 0)
    return 0;
  
  dyn3[x1][x2] = 1;
  
  if (x1 >= 2 && x2 < 2*MAXI)
    dyn3[x1][x2] = max(dyn3[x1][x2], solve3(x1-2, x2+1));
  if (x2 >= 2 && x1 < 2*MAXI)
    dyn3[x1][x2] = max(dyn3[x1][x2], solve3(x1+1, x2-2));
  if (x1 >= 1 && x2 >= 1)
    dyn3[x1][x2] = max(dyn3[x1][x2], solve3(x1-1, x2-1)+1);
  
  return dyn3[x1][x2];
}

int solve4(int x1, int x2, int x3)
{
  if (dyn4[x1][x2][x3] != -1)
    return dyn4[x1][x2][x3];
  
  if (x1 == 0 && x2 == 0 && x3 == 0)
    return 0;
  
  dyn4[x1][x2][x3] = 1;
  
  if (x1 >= 2 && x2 < 2*MAXI)
    dyn4[x1][x2][x3] = max(dyn4[x1][x2][x3], solve4(x1-2, x2+1, x3));
  if (x2 >= 2)
    dyn4[x1][x2][x3] = max(dyn4[x1][x2][x3], solve4(x1, x2-2, x3)+1);
  if (x3 >= 2 && x2 < 2*MAXI)
    dyn4[x1][x2][x3] = max(dyn4[x1][x2][x3], solve4(x1, x2+1, x3-2));
  if (x1 >= 1 && x2 >= 1 && x3 < 2*MAXI)
    dyn4[x1][x2][x3] = max(dyn4[x1][x2][x3], solve4(x1-1, x2-1, x3+1));
  if (x1 >= 1 && x3 >= 1)
    dyn4[x1][x2][x3] = max(dyn4[x1][x2][x3], solve4(x1-1, x2, x3-1)+1);
  if (x2 >= 1 && x3 >= 1 && x1 < 2*MAXI)
    dyn4[x1][x2][x3] = max(dyn4[x1][x2][x3], solve4(x1+1, x2-1, x3-1));
  
  return dyn4[x1][x2][x3];
}


void main2()
{
  int N, P; cin >> N >> P;
  int x[4] = {0, 0, 0, 0};
  for (int i=0; i<N; i++)
  {
    int tmp; cin >> tmp;
    x[tmp % P]++;
  }
  
  //cerr << x[0] << " " << x[1] << " " << x[2] << " " << x[3] << endl;
  
  if (P == 2)
    cout << x[0] + solve2(x[1]) << endl;
  if (P == 3)
    cout << x[0] + solve3(x[1], x[2]) << endl;
  if (P == 4)
    cout << x[0] + solve4(x[1], x[2], x[3]) << endl;
}

int main()
{
  for (int x1=0; x1<=2*MAXI; x1++)
  {
    dyn2[x1] = -1;
    for (int x2=0; x2<=2*MAXI; x2++)
    {
      dyn3[x1][x2] = -1;
      for (int x3=0; x3<=2*MAXI; x3++)
      {
        dyn4[x1][x2][x3] = -1;
      }
    }
  }
  
  for (int x1=0; x1<=2*MAXI; x1++)
  {
    solve2(x1);
    for (int x2=0; x2<=2*MAXI; x2++)
    {
      solve3(x1, x2);
      for (int x3=0; x3<=2*MAXI; x3++)
      {
        solve4(x1, x2, x3);
      }
    }
  }
  
  int T;
  cin >> T;
  for (int t=0; t<T; t++)
  {
    cout << "Case #" << t+1 << ": ";
    main2();
  }
}
