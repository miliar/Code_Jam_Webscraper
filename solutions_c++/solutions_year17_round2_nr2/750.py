#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <cmath>
#include <cctype>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <bitset>
#include <list>
#include <cstdarg>

#ifndef DBG
#define	DBG	0
#endif

//#define	DBG(f,x)	if(_____debug & f) { x; }
using namespace std;

#define	rep(i,n)	for((i) = 0; (i) < (n); (i)++)
#define	rab(i,a,b)	for((i) = (a); (i) <= (b); (i)++)
#define all(v)		(v).begin(),(v).end()
#define	Fi(n)		rep(i,n)
#define	Fj(n)		rep(j,n)
#define	Fk(n)		rep(k,n)
#define	sz(v)		(v).size()

struct Color {
  char c;
  int count;

  bool operator < (const Color &r) const {
    return count > r.count;
  }
};

#define IMPOSSIBLE "IMPOSSIBLE"

string arrange(vector<Color>& v) {
  vector <string> vs;
  int i,j;

  if (sz(v) == 1) {
    if (v[0].count == 1) {
      string s = "";
      s += v[0].c;
      return s;
    } else {
      return IMPOSSIBLE;
    }
  }

  int k = v[0].count;

  Fi(k) {
    string s = "";

    for (j = 1; j < sz(v); j++) {
      if (v[j].count > 0) {
        break;
      }
    }
    if (j >= sz(v)) return IMPOSSIBLE;
  
    s += v[0].c;
    s += v[j].c;
    v[0].count--;
    v[j].count--;
    //cout << s << endl;
    vs.push_back(s);
  }

  Fi(sz(vs)) {
    Fj(sz(v)) {
      if (v[j].count > 0) {
        vs[i] += v[j].c;
        v[j].count--;
      }
    }
    //cout << vs[i] << endl;
  }

  string a = "";

  Fi(sz(vs)) a += vs[i];

  return a;
}

int main() {
  int T,cs;
  int N,R,O,Y,G,B,V;
  int i;

  scanf("%d",&T);

  rab(cs,1,T) {
    scanf("%d %d %d %d %d %d %d",&N,&R,&O,&Y,&G,&B,&V);

    vector <Color> c;

    Color r,g,b,y;

    r.c = 'R';
    r.count = R;

    g.c = 'G';
    g.count = G;

    b.c = 'B';
    b.count = B;

    y.c = 'Y';
    y.count = Y;
   
    c.push_back(r);
    c.push_back(g);
    c.push_back(b);
    c.push_back(y);

    sort(all(c));

    cout << "Case #" << cs << ": " << arrange(c) << endl;
  }

  return 0;
}
