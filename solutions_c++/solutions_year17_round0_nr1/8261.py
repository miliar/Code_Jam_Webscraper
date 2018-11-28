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
  scanf("%d",&t);
  FORN(i,t) {
    string s;
    int n;
    cin >> s >> n;
    int ans = 0;
    FORN(i,s.sz())
      if (s[i] == '-') {
        if (s.sz()-i < n) {
          ans = -1;
          break;
        }
        int x = 0;
        while (x < n) {
          if (s[i+x] == '+') {
            if (s.sz()-i-x < n) {
              ans = -1;
              break;
            }
            FOR(j,i+x,i+x+n)
              if (s[j] == '-')
                s[j] = '+';
              else
                s[j] = '-';
            ans++;
          }
          x++;
        }
        if (ans == -1)
          break;
        FOR(j,i,i+n)
          if (s[j] == '-')
            s[j] = '+';
          else
            s[j] = '-';
        ans++;
      }
    if (ans == -1)
      printf("Case #%d: IMPOSSIBLE\n", i+1);
    else
      printf("Case #%d: %d\n",i+1, ans);
  }
}