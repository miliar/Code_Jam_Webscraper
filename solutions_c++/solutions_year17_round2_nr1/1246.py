#include <cstdio>
#include <set>
#include <cstring>
//#include <algorithm>
#include <vector>

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


int main(int argc, char *argv[])
{
     int T;
     scanf("%i", &T);
     forr (tt, 1, T) {
          int D,N;
          scanf("%i %i\n", &D, &N);
          long double maxv = 10e100;
          long double d = D;
          fori (i, N){
            int Ki, Si;
            scanf("%i %i\n", &Ki, &Si);
            if (Ki >= D) continue;
            long double s = Si, k = Ki;
            long double v = (s*d)/(d-k);
            if (v < s) v = s;
            if (v < maxv) maxv = v;
          }


          printf("Case #%i: ", tt);
          printf("%Lf\n",  maxv);
     }
}
