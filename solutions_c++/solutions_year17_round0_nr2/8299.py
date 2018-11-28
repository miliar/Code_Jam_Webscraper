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
    string s;
    cin >> s;
    int x = 0;
    FOR(j, 1, s.sz())
      if (s[j] > s[j-1])
        x = j;
      else if (s[j] < s[j-1]) {
        if (s[j-1] > '1') {
          s[x] = (char)((int)s[x]-1);
          FOR(k, x+1, s.sz())
            s[k] = '9';
        } else {
          string tmp = "";
          FORN(k, s.sz()-1)
            tmp += '9';
          s = tmp;
        }
        break;
      }
    printf("Case #%d: %s\n", i+1, s.c_str());
  }
}