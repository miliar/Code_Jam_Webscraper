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

bool istriplemin(int a, int b, int c){
  return (a <= b) && (a<=c);
}
bool istriplemax(int a, int b, int c){
  return (a >= b) && (a>=c);
}

#define rput(c) do {if (p > 0 && res[p-1] == c) fail = true;  res[p] = c; p++;  n--; } while(0)

int main(int argc, char *argv[])
{
     int T;
     scanf("%i", &T);
     forr (tt, 1, T) {
          int r, o, y, g, b, v;
          char res[2000] = {0};
          int n;
          bool fail = false;
          scanf("%i %i %i %i %i %i %i\n", &n, &r, &o, &y, &g, &b, &v);
          int oldn = n;
          //int n = r+o+y+g+b+v;
          int c[6]={r,o,y,g,b,v};

          for (int t=0;t<3;t++){
            int p=0;
            r = c[0];
            o = c[1];
            y = c[2];
            g = c[3];
            b = c[4];
            v = c[5];
            n = oldn;

            if (t == 0) { if (r == 0) continue; r--; rput('R'); }
            if (t == 1) { if (y == 0) continue; y--; rput('Y'); }
            if (t == 2) { if (b == 0) continue; b--; rput('B'); }

            while (n > 0 && !fail) {
              if (r > 0 && istriplemax(r,y,b) && res[p-1] != 'R') { r--; rput('R'); }
              else if (y > 0 && istriplemax(y,r,b) && res[p-1] != 'Y') { y--; rput('Y'); }
              else if (b > 0 && res[p-1] != 'B') { b--; rput('B'); }
              else if (y > 0 && res[p-1] != 'Y') { y--; rput('Y'); }
              else if (r > 0 && res[p-1] != 'R') { r--; rput('R'); }
              else fail = true;
            }
            if (oldn > 1) fail = fail || (res[oldn-1] == res[0]);
            if (!fail)break;
        }

          printf("Case #%i: ", tt);
          printf("%s\n",  fail ? "IMPOSSIBLE" : res);
          //printf("%s\n",   res);
     }
}
