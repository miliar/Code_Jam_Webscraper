#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef pair< ll, ll > ii;
typedef vector< ll > vi;
typedef vector< ii > vii;

#define INF 0x3F3F3F3F
#define LINF 0x3F3F3F3F3F3F3F3FLL
#define pb push_back
#define mp make_pair
#define pq priority_queue
#define LSONE(s) ((s)&(-s))
#define DEG_to_RAD(X)   (X * PI / 180)
#define F first
#define S second
#define PI 2*acos(0)

#ifdef ONLINE_JUDGE
#define debug(args...)
#else
#define debug(args...) fprintf(stderr,args)
#endif

const int N = 1010;
int test = 1;

map< pair<char, char>, int > nop;

char s[N];
int n;

int r, o, y, g, b, v;


inline void main2() {
  scanf("%d %d %d %d %d %d %d", &n, &r, &o, &y, &g, &b, &v);
  int len = 0;

  int fst = 0;
  if(r >= y && r >= b) {
    r--; 
    s[len++] = 'R';
    fst = 0;
  }
  else if(y >= r && y >= b) {
    y--;
    s[len++] = 'Y';
    fst = 1;
  }
  else {
    b--;
    s[len++] = 'B';
    fst = 2;
  }

  while(len < n) {
    if(s[len - 1] == 'R') {
      if(y == 0 && b == 0) break;
      if(y > b || (y == b && fst == 1)) {
        y--;
        s[len++] = 'Y';
      }
      else {
        b--;
        s[len++] = 'B';
      }
    }
    else if(s[len - 1] == 'Y') {
      if(r == 0 && b == 0) break;
      if(r > b || (r == b && fst == 0)) {
        s[len++] = 'R';
        r--;
      }
      else {
        s[len++] = 'B';
        b--;
      }
    }
    else if(s[len - 1] == 'B') {
      if(y == 0 && r == 0) break;
      if(y > r || (y == r && fst == 1)) {
        s[len++] = 'Y';
        y--;
      }
      else {
        s[len++] = 'R';
        r--;
      }
    }
  }

  if(len < n) printf("Case #%d: IMPOSSIBLE\n", test++);
  else {
    if(s[len - 1] == s[0]) printf("Case #%d: IMPOSSIBLE\n", test++);
    else {
      printf("Case #%d: ", test++);
      for(int i = 0; i < n; ++i) printf("%c", s[i]);
      printf("\n");
    }
  }
}

int main() {
  nop[mp('R', 'R')] = 1;
  nop[mp('Y', 'Y')] = 1;
  nop[mp('B', 'B')] = 1;
  int t; scanf("%d", &t);
  while(t--) main2();
  return 0;
}