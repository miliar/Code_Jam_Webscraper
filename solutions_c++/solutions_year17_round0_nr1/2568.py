// ya rab
#include <bits/stdc++.h>
#include <ext/hash_map>

using namespace std;
using namespace __gnu_cxx;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define mp make_pair
#define pb push_back
#define oo (1<<29)
#define sz(v) (int)v.size()
#define all(c) (c).begin(),(c).end()
#define rall(c) (c).rbegin(),(c).rend()
#define mem(s,v) memset(s,v,sizeof(s))
#define ppc(x) __builtin_popcount((x))
#define mt make_tuple // you can ignore
#define eb emplace_back

typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<double> vd;
typedef vector<string> vs;
typedef pair<int, int> pi;

//int dx[] = { 0, 0, 1, -1 };
//int dy[] = { 1, -1, 0, 0 };

int main() {
  ios::sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL);
  freopen("test.in", "rt", stdin);
  freopen("o.txt", "wt", stdout);
  int t;
  cin >> t;
  FOR (cs, 1, t + 1)
  {
    string s;
    int k;
    cin >> s >> k;
    int res = 0, n = sz(s);
    FOR (i , 0 , n)
    {
      if (i + k > n)
        break;
      if (s[i] == '-') {
        FOR (j , i , i + k)
          s[j] = (s[j] == '+' ? '-' : '+');
        res ++;
      }
    }
    if (count(all(s), '-'))
      printf ("Case #%d: IMPOSSIBLE\n", cs);
    else
      printf ("Case #%d: %d\n", cs, res);
  }
  return 0;
}
