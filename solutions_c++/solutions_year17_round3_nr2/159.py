#include <bits/stdc++.h>

using namespace std;

long long _();
int main() { _(); return 0; }
#define main _
#define int long long 

const int INF = 1e12;
const int T_MAX = 1440;

int prop[T_MAX];
int dyn[2][T_MAX][T_MAX/2+1][2];

int fDyn(bool start, int t, int used, bool cur)
{
   if(t == T_MAX)
      return used == T_MAX/2 ? cur != start : INF;
   if(used == T_MAX/2+1)
      return INF;
   if(dyn[start][t][used][cur] != -1)
      return dyn[start][t][used][cur];
   int go0 = prop[t] != 1 ? fDyn(start, t+1, used+1, 0) + cur : INF;
   int go1 = prop[t] != 0 ? fDyn(start, t+1, used, 1) + (cur == 0) : INF;
   return dyn[start][t][used][cur] = min(go0, go1);
}

int main()
{
   ios_base::sync_with_stdio(false);
   int T;
   cin >> T;
   for(int test=1; test<=T; test++)
   {
      int n[2];
      cin >> n[0] >> n[1];
      for(int i=0; i<T_MAX; i++)
         prop[i] = 2;
      for(int a=0; a<2; a++)
         for(int i=0; i<T_MAX; i++)
            for(int j=0; j<=T_MAX/2; j++)
               for(int k=0; k<2; k++)
               dyn[a][i][j][k] = -1;
      for(int k=0; k<2; k++)
         for(int i=0; i<n[k]; i++)
         {
            int a, b;
            cin >> a >> b;
            for(int j=a; j<b; j++)
               prop[j] = k;
         }
      cout << "Case #" << test << ": " << min(fDyn(0, 0, 0, 0), fDyn(1, 0, 0, 1)) << endl;
   }
   return 0;
}