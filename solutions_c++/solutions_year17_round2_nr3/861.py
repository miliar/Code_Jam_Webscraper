#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cstring>

using namespace std;

const double eps = 1e-6;

const int N = 120;

long long n, E[N], S[N];
long long D[N][N];
int U, V;

void init()
{
  int Q;
  cin >> n >> Q;
  for (int i=0; i<n; ++i)
    cin >> E[i] >> S[i];
  for (int i=0; i<n; ++i)
    for(int j=0; j<n; ++j)
      cin >> D[i][j];
  cin >> U >> V;
}

double f[N];
long long suf[N];
double work()
{
  f[n-1] = 0;
  suf[n-1] = 0;
  for (int i=n-2; i>=0; --i)
  {
    f[i] = 1e50;
    suf[i] = suf[i+1] + D[i][i+1];
    for (int j=i+1; j<n; ++j)
    {
      if (suf[i]-suf[j] > E[i])
        continue;
      f[i]=min(f[i], f[j]-1.0*(suf[j]-suf[i])/S[i]);
    }
  }
  return f[0];
}

int main()
{
  //freopen("B-small-attempt1.in", "r", stdin);
  freopen("C-small-attempt0.in", "r", stdin);
  freopen("C.out", "w", stdout);
  int T;
  cin >> T;
  for (int i=1; i<=T; ++i)
  {
    cout << "Case #" << i << ": ";
    init();
    printf("%.6f\n", work());
  }
}
