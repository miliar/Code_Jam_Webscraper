#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <bitset>
#include <cstdlib>
#include <cmath>
#include <set>
#include <list>
#include <deque>
#include <map>
#include <queue>
#include <fstream>
#include <cassert>
#include <cmath>
#include <sstream>
#include <time.h>
#include <complex>
#include <iomanip>

using namespace std;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef pair<double,double> dd;
typedef pair<char,char> cc;
typedef vector<ii> vii;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<ll, ll> l4;
const double eps = 0.005;
const int maxn = 110;
const ll mod = 1e9+7;

int T,n,p,t;
int a[4];

int main() {
    scanf("%d",&T);
    for (int tt = 1; tt <= T; tt++) {
        memset(a, 0, sizeof(a));
        printf("Case #%d: ",tt);
        scanf("%d%d",&n,&p);
        for (int i = 0; i < n; i++) {
            scanf("%d",&t);
            a[t%p]++;
        }
        int ans = a[0];
        if (p == 2) {
            ans += a[1]/2;
            ans += a[1]%2;
        } else if (p == 3) {
            if (a[1] < a[2]) {
                swap(a[1],a[2]);
            }
            ans += a[2];
            a[1] -= a[2];
            ans += a[1]/3;
            ans += a[1]%3>0;
        } else {
            if (a[1] < a[3]) {
                swap(a[1], a[3]);
            }
            ans += a[3];
            a[1] -= a[3];
            ans += a[2]/2;
            a[2] %= 2;
            if (a[2] && a[1] >= 2) {
                ans++;
                a[2] = 0;
                a[1] -= 2;
            }
            ans += a[1]/4;
            a[1] %= 4;
            if (a[2] || a[1]) {
                ans++;
            }
        }
        printf("%d\n",ans);
    }
}




