#include <bits/stdc++.h>

using namespace std;

long long _();
int main() { _(); return 0; }
#define main _
#define int long long 

const int INF = 1e15;
const double PI = 3.141592653589;
const int N_MAX = 1e3;

int N, K;
vector<pair<int, int>> t;
int dyn[N_MAX][N_MAX];

int fDyn(int i, int k)
{
   if(k == K)
      return 0;
   if(i == N)
      return -INF;
   if(dyn[i][k])
      return dyn[i][k];
   return dyn[i][k] = max(fDyn(i+1, k+1) + (k == 0 ? t[i].first*t[i].first : 0) +2*t[i].first*t[i].second, 
   fDyn(i+1, k));
}

int main()
{
   ios_base::sync_with_stdio(false);
   int T;
   cin >> T;
   for(int test=1; test<=T; test++)
   {
      cin >> N >> K;
      t.resize(N);
      for(int i=0; i<N; i++)
         for(int j=0; j<K; j++)
            dyn[i][j] = 0;
      for(int i=0; i<N; i++)
         cin >> t[i].first >> t[i].second;
      sort(t.rbegin(), t.rend());
      cout << "Case #" << test << ": " << fixed << setprecision(9) << fDyn(0, 0) * PI << endl;
   }
   return 0;
}