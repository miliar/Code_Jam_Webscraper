#include <cstdio>
#include <set>
#include <string>
//#include <algorithm>
#include <vector>
#include "string.h"

using namespace std;
//--common
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
     char s[10000];
     bool swap[10000];
     forr (tt, 1, T) {
          int k;
          scanf("%s %i\n",s,&k);

          memset(swap, 0, sizeof(swap));
          int swaps=0; bool inswap = false;
          int lastswap = 0;
          int i=0;
          for (i=0;s[i];i++){
            if (swap[i]) inswap = !inswap;
            if (s[i]==(inswap ? '+':'-'))  {
              swaps++;
              inswap = !inswap;
              swap[i+k]=true;
              lastswap = i+k;
              //fprintf(stderr,"  swap: %i %i\n",i,i+k);
            }
          }


          printf("Case #%i: ", tt);
          if (lastswap > i) printf("%s\n",  "IMPOSSIBLE");
          else printf("%i\n",  swaps);
     }
}
