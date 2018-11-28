#include <cstdio>
#include <set>
#include <cstring>
#include <algorithm>
#include <vector>
#include <math.h>

using namespace std;
//--common
typedef __int64_t ll;
typedef double llf;
#define forr(i,f,t) for (int i = (f); i <= (t); i++)
#define fori(i,t) for (int i = 0; i < (t); i++)
#define forc(i,c) for (int i = 0; i < (c).size(); i++)
#define forit(it,c) for (auto it = (c).begin(), end = (c).end(); it != end; ++it)

template <typename C> void rerase(C& s, const typename C::const_reverse_iterator &it ) { s.erase(s.find(*it)); }
template <typename T> vector<T>& operator<<(vector<T>& v, const T& t) { v.push_back(t); return v; }
template <typename T> set<T>& operator<<(set<T>& v, const T& t) { v.insert(t); return v; }
//--end common


struct pancake{
  int r,h;
  llf side;
  llf top;
  pancake(int r,int h): r(r),h(h){
    side = 2*M_PI * (llf) ( r ) * (llf)h;
    top = M_PI*(llf)(r)*(llf)(r);
  }
  bool operator <(const pancake& o) const{ return side >= o.side; }
};

int main(int argc, char *argv[])
{
     int T;
     scanf("%i", &T);
     forr (tt, 1, T) {
          int n,K;
          scanf("%i %i\n", &n, &K);
          
          vector<pancake> v;

          fori (i, n) {
            int r,h;
            scanf("%i %i\n", &r, &h);
            v.push_back(pancake(r,h));
          }
          std::sort (v.begin(), v.end());

          llf best = 0;
          fori (i, n) {
            llf score=0;
            int k = 0;
            int r = v[i].r;
            k++;
            score += v[i].side + v[i].top;
            if (k < K)
            fori (j, n) {
              if (i != j && v[j].r <= r) {
                k++;
                score += v[j].side;
                if (k >= K) break;
              }
            }
            if (score > best)best=score;
          }

          printf("Case #%i: ", tt);
          printf("%f\n",  best);
     }
}
