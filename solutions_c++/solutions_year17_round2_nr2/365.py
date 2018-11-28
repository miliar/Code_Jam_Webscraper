#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <cstring>
#include <cstdio>
#include <map>
#include <set>
#include <deque>
#include <algorithm>

using namespace std;

#define f first
#define s second
#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()
#define sqr(x) (x) * (x)
#define forn(i, l, r) for(int i = l; i < r; i ++)
#define forit(it, s) for(__typeof(s.begin()) it = s.begin(); it != s.end(); it ++)
#define y1 salnk
#define N 200100              
#define sz(a) (int)a.size()
#define ll long long
const int inf = (int)1e9;
const double pi = acos(-1.0);
const double eps = 1e-9;


int t;
int r, o, y, b, g, v;
pair <int, char> a[N];
string res[N];
int n;
int main () {
    //freopen("in", "r", stdin);
     cin >> t;
     int cs = 0;
     while (t--) {
           cs++;
      	printf("Case #%d: ",cs);
     	cin >> n;
     	cin >> r >> o >> y >> g >> b >> v;
          if (o+g+v>0) {
           	cout << "bad\n";
           	continue;
          }
     	a[1].f = r;
     	a[2].f = y;
     	a[3].f = b;
     	a[1].s= 'R';
     	a[2].s = 'Y';
     	a[3].s = 'B';

     	sort(a + 1, a + 4);
     	if (a[1].f + a[2].f < a[3].f) {
     	 	printf("IMPOSSIBLE\n");
     	 	continue;
     	}

     	int pos = 1;
     	for (int i = 1; i <= a[3].f; i++)
     		res[i] = a[3].s;
     	for (int i = 1; i <= a[2].f; i++) {
     		res[pos] = a[2].s+res[pos];
     		pos++;
     		if (pos > a[3].f) pos = 1;
     	}
     	for (int i = 1; i <= a[1].f; i++) {
     		res[pos] = a[1].s+res[pos];
     		pos++;
     		if (pos > a[3].f) pos = 1;
     	}

     	for (int i = 1; i <= a[3].f; i++)
     		cout << res[i];
     	cout << endl;

     }
     return 0;
}