#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <list>
#include <sstream>
#include <ctime>
#include <functional>
#define pi 3.14159265358979323846264338327950288
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define LL long long
#define LD long double
#define INF 1000000000
#define INFll 1000000000000000000ll
#define Vi vector<int>
#define VI Vi::iterator
#define Mi map<int, int>
#define MI Mi::iterator
#define Si set<int>
#define SI Si::iterator
#define FOR(i,s,e) for (int i=(s); i<(e); i++)
#define FOE(i,s,e) for (int i=(s); i<=(e); i++)
#define FOD(i,s,e) for (int i=(s)-1; i>=(e); i--)
#define CLR(a,x) memset(a, x, sizeof(a))
#define SZ(x) ((int)x.size())
#define mid (l + r) / 2
#define Left k * 2, l, mid
#define Right k * 2 + 1, mid + 1, r
#define N 1111
using namespace std;
int T;
LL n, k;
void work(LL n, LL k) {
  if (k == 1) {
    cout << n / 2 << " " << (n - 1) / 2 << endl;
    return;
  }
  if (n <= 1) {
    cout << "0 0" << endl;
    return;
  }
  if (n & 1)
    work(n / 2, k / 2);
  else
    work(n / 2 - (k & 1), k / 2);
}
int main() {
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  scanf("%d", &T);
  for (int cas = 1; cas <= T; cas ++) {
    cin >> n >> k;
    cout << "Case #" << cas << ": " ;
    work(n, k);
  }

}
