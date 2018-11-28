//darkstallion's template

#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<map>
#include<list>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<string>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define popb pop_back
#define del erase
#define sz size
#define ins insert
#define FOR(a,b,c) for(int a = b; a < c; a++)
#define FORS(a,b,c) for(int a = b; a <= c; a++)
#define FORN(a,b) for(int a = 0; a < b; a++)
#define FORD(a,b,c) for (int a = b; a >= c; a--)
#define RES(a,b) memset(a,b,sizeof(a))
#define LL long long
#define PII pair<int,int>
#define PLL pair<long long,long long>
#define PDD pair<double,double>
#define PCC pair<char,char>
#define PSS pair<string,string>
#define PI acos(-1)
#define eps 1e-9
#define MOD 1000000007
using namespace std;

int main() {
  int t;
  scanf("%d", &t);
  FORN(i, t) {
    int n, cr, co, cy, cg, cb, cv;
    scanf("%d%d%d%d%d%d%d", &n, &cr, &co, &cy, &cg, &cb, &cv);
    string st = "";
    if ((cr >= cy) && (cr >= cb)) {
      if (cr <= cy + cb) {
        if (cy > cb) {
          FORN(j, cy-cb)
            st += "RY";
          cr -= (cy-cb);
          cy = cb;
        } else if (cb > cy) {
          FORN(j, cb-cy)
            st += "RB";
          cr -= (cb-cy);
          cb = cy;
        }
        while ((cr != cb) || (cr != cy)) {
          if ((st == "") || (st[st.sz()-1] != 'R')) {
            st += 'R';
            cr--;
          } else if (cy >= cb) {
            st += 'Y';
            cy--;
          } else {
            st += 'B';
            cb--;
          }
        }
        FORN(j, cr)
          if (st[st.sz()-1] != 'R')
            st += "RYB";
          else
            st += "YRB";
      }
    } else if ((cy >= cr) && (cy >= cb)) {
      if (cy <= cr + cb) {
        if (cr > cb) {
          FORN(j, cr-cb)
            st += "YR";
          cy -= (cr-cb);
          cr = cb;
        } else if (cb > cr) {
          FORN(j, cb-cr)
            st += "YB";
          cy -= (cb-cr);
          cb = cr;
        }
        while ((cr != cb) || (cr != cy)) {
          if ((st == "") || (st[st.sz()-1] != 'Y')) {
            st += 'Y';
            cy--;
          } else if (cr >= cb) {
            st += 'R';
            cr--;
          } else {
            st += 'B';
            cb--;
          }
        }
        FORN(j, cr)
          if (st[st.sz()-1] != 'Y')
            st += "YRB";
          else
            st += "RYB";
      }
    } else if ((cb >= cr) && (cb >= cy)) {
      if (cb <= cr + cy) {
        if (cr > cy) {
          FORN(j, cr-cy)
            st += "BR";
          cb -= (cr-cy);
          cr = cy;
        } else if (cy > cr) {
          FORN(j, cy-cr)
            st += "BY";
          cb -= (cy-cr);
          cy = cr;
        }
        while ((cr != cb) || (cr != cy)) {
          if ((st == "") || (st[st.sz()-1] != 'B')) {
            st += 'B';
            cb--;
          } else if (cr >= cy) {
            st += 'R';
            cr--;
          } else {
            st += 'Y';
            cy--;
          }
        }
        FORN(j, cr)
          if (st[st.sz()-1] != 'B')
            st += "BRY";
          else
            st += "RBY";
      }
    }
    if (st == "")
      printf("Case #%d: IMPOSSIBLE\n", i+1);
    else
      printf("Case #%d: %s\n", i+1, st.c_str());
  }
}