#include <cstdio>
#include <set>
#include <cstring>
//#include <algorithm>
#include <vector>
#include <map>

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
          ll n,k;
          scanf("%li %li\n", &n,&k);
          
          std::map<ll, ll, greater<ll>> pieces;
          pieces[n]=1;

          ll piece=0;
          while (k > 0) {
            auto it = pieces.begin();
            while (it->second == 0) {
              pieces.erase(it);
              it = pieces.begin();
            }
            piece = it->first;
            ll count = it->second;
            ll delta = min(k, it->second);
            pieces.erase(it);
            pieces[piece / 2] += delta;
            pieces[(piece - 1) / 2] += delta;
            k-=delta;
            //fprintf(stderr, "%li \t %li\n",  piece, count);
          }



          printf("Case #%i: ", tt);
          printf("%li %li\n",  piece/2, (piece-1)/2);
     }
}
