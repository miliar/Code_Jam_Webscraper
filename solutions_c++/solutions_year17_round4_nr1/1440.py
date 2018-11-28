// ya rab
#include <bits/stdc++.h>
#include <ext/hash_map>

using namespace std;
using namespace __gnu_cxx;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define mp make_pair
#define pb push_back
#define oo (1<<30)
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
int arr[101], n, p;

int bf() {
  sort(arr, arr + n);
  int res = 0;
  do {
    int c = 1, tot = arr[0];
    FOR (i , 1 , n)
    {
      c += (tot % p == 0);
      tot += arr[i];
    }
    res = max(res, c);
  } while (next_permutation(arr, arr + n));
  return res;
}

int main() {
  ios::sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL);
#ifndef ONLINE_JUDGE
  freopen("test.in", "rt", stdin);
  freopen("o.txt", "wt", stdout);
#endif
//  cout << 1000 << endl;
//  FOR (k , 0 , 1000) {
//    int n = 6;
//    cout << n << " 4" << endl;
//    FOR (i , 0 , n) {
//      int x = (rand() % 3) + 1;
//      cout << x << " ";
//    }
//    cout << endl;
//  }
//  return 0;
  int t;
  cin >> t;
  FOR (cs, 1 , t + 1)
  {
    cin >> n >> p;
    int cnt[5] = { 0 };
    FOR (i , 0 , n)
    {
      int x;
      cin >> x;
      arr[i] = x;
      cnt[x % p]++;
    }
    int res = cnt[0];
    if (p == 2) {
      res += (cnt[1] + 1) / 2;
    } else if (p == 3) {
      int mn = min(cnt[1], cnt[2]);
      res += mn, cnt[1] -= mn, cnt[2] -= mn;
      res += (cnt[1] + 2) / p + (cnt[2] + 2) / p;
    } else if (p == 4) {
      int c2 = cnt[2] / 2;
      cnt[2] -= c2 * 2, res += c2;
      int mn = min(cnt[1], cnt[3]);
      cnt[1] -= mn, cnt[3] -= mn;
      res += mn;
      int rem = max(cnt[1], cnt[3]);
      if (cnt[2]) {
        res++;
        rem -= min(rem, 2);
      }
      res += (rem + 3) / 4;
    }

    printf("Case #%d: %d\n", cs, res);
  }
  return 0;
}
