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


ll fullcounts[10][19] = {-1};

ll count(int firstdigit, int len){
  if (fullcounts[firstdigit][len] >=0) return fullcounts[firstdigit][len];
  ll res = 0;
  if (len == 0) res = 1;
  else if (len == 1) res = 10 - firstdigit;
  else {
    for (int f = firstdigit; f <= 9;f++){
      res += count(f, len - 1 );
    }
  }
  fullcounts[firstdigit][len] = res;
  return res;
}

ll strcount(int mindigit, char* s, int len){
  if (*s == '\0') return 0;
  int fd = *s-'0';
  if (fd == '0') return strcount(mindigit,s+1,len-1);
  if (len == 1) return count(max(fd,mindigit), len);
  ll res = 0;
  forr (i, mindigit, fd - 1) res += count(i,len-1);
  if (*s <= *(s+1)) res += strcount(fd, s+1,len-1);
  return res;
}

int main(int argc, char *argv[])
{
     int T;
     scanf("%i", &T);
     char line[100];
     forr (tt, 1, T) {
          //ll n;
          //scanf("%lli\n", &n);
       scanf("%s\n", line);
          int len = strlen(line);
          bool changed = true;
          while (changed) {
            changed = false;
            for (int i=0;i<len-1;i++)
              if (line[i] > line[i+1]) {
                changed = true;
                line[i]--;
                for (i++;i<len;i++) line[i] = '9';
              }
          }

          char * out = line;
          while (*out == '0') out++;

          printf("Case #%i: ", tt);
          printf("%s\n",  out);
     }
}
