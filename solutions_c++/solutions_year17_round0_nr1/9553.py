#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <deque>
#include <list>
#include <map>
#include <set>
#include <cmath>
#include <cstring>
#include <string>
#include <bitset>
#include <fstream>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef double db;
typedef vector<int> vi;
typedef vector<long long> vll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<double,double> pdd;
typedef vector<pii> vii;

#define INF 1000000007ll
#define PB push_back
#define MP make_pair
#define X first
#define Y second
#define Min(a,b) (((a) < (b))?(a):(b))
#define Max(a,b) (((a) > (b))?(a):(b))
#define Abs(a) (((a) > 0)?(a):(-1)*(a))
#define cil(a,b) ( ((a)%(b) == 0)?((a)/(b)):((a)/(b)+1) )
#define SIZE 0

char s[1002];
int main() {
   int t;
   scanf("%d", &t);
   for (int tc = 1 ; tc <= t ; ++tc) {
      int k, ans = 0;
      memset(s, 0, sizeof(s));
      scanf("%s %d", s, &k);
      int l = strlen(s);
      for (int i = 0 ; i <= l-k ; ++i) {
         if (s[i] == '-') {
            ++ans;
            for (int j = i ; j < i+k ; ++j) {
               if (s[j] == '+') s[j] = '-';
               else s[j] = '+';
            }
         }
      }
      for (int i = l-1 ; i >= l-k ; --i) {
         if (s[i] == '-') { ans = -1; break; }
      }
      if (ans == -1) printf("Case #%d: IMPOSSIBLE\n", tc);
      else printf ("Case #%d: %d\n", tc, ans); 
   } 
   return 0;
}

