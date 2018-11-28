#include <cstdio>
#include <set>
#include <cstring>
//#include <algorithm>
#include <vector>
#include <limits>
#include <cmath>

using namespace std;
//--common
typedef __int64_t ll;
#define forr(i,f,t) for (int i = (f); i <= (t); i++)
#define fori(i,t) for (int i = 0; i < (t); i++)
#define forc(i,c) for (int i = 0; i < (c).size(); i++)
#define forit(it,c) for (auto it = (c).begin(), end = (c).end(); it != end; ++it)

template <typename C> void rerase(C& s, const typename C::const_reverse_iterator &it ) { s.erase(s.find(*it)); }
template <typename T> vector<T>& operator<<(vector<T>& v, const T& t) { v.push_back(t); return v; }
template <typename T> set<T>& operator<<(set<T>& v, const T& t) { v.insert(t); return v; }
//--end common

const int MAXN = 105;

int D[MAXN][MAXN];

typedef long double ldd;

const ldd inf = std::numeric_limits<ldd>::infinity();

ldd space[MAXN][MAXN];
ldd time[MAXN][MAXN];

int main(int argc, char *argv[])
{
     int T;
     scanf("%i", &T);

     long double test = inf;

     /*if (isinf(test+test)) printf("a\n");

     printf("%Lf\n",  test);
     printf("%Lf\n",  test+test);
     printf("%Lf\n",  2*test);
return 0;*/

     forr (tt, 1, T) {
          int n,q;
          scanf("%i %i\n", &n, &q);
          int endurance[MAXN], speed[MAXN];
          fori (i, n) scanf("%i %i\n", &endurance[i], &speed[i]);
          fori (i, n) fori (j, n)
              scanf("%i", &D[i][j]);

          fori (i, n) fori (j, n)
              if (D[i][j] == -1) space[i][j] = inf;
              else space[i][j] = D[i][j];

         /* fori (i, n) {
            fori (j, n)
                printf("%Lf", space[i][j]);
            printf("\n");
          }
          printf("\n");*/

          fori (k, n)
              fori (i, n) fori (j, n) {
            ldd overk = space[i][k]+space[k][j];
            if (overk < space[i][j]) space[i][j] = overk;
          }

          fori (i, n) fori (j, n) {
            time[i][j]=space[i][j];
            if (! isinf( time[i][j] ) && time[i][j] <= endurance[i]){
              time[i][j] = time[i][j] / speed[i];
            }
          }

          fori (k, n)
              fori (i, n) fori (j, n) {
            ldd overk = time[i][k]+time[k][j];
            if (overk < time[i][j]) time[i][j] = overk;
          }



          printf("Case #%i: ", tt);
          fori (i, q) {
            int from,to;
            scanf("%i %i\n", &from, &to);
            if (i) printf(" ");
            printf("%Lf",  time[from-1][to-1]);
          }
           printf("\n");
     }
}
