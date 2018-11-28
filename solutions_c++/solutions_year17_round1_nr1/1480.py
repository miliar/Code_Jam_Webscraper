// Made By Haireden Aibyn
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <ctime>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>

using namespace std;

#define fname ""
#define INF 2147483647
#define MOD 1000000007
#define mp make_pair
#define F first
#define S second
#define sc scanf
#define all(x) x.begin(), x.end()
#define size(x) int(x.size())
#define pr printf
#define deb(x) cerr << " | " << #x << " = " << x
#define pb push_back
#define ex exit(0)
#define y1 y4

typedef long long ll;
typedef unsigned long long ull;

const int N = 200;

int n, m;
bool was[N];
char a[N][N];

bool check(int x, int l, int r) {
     for (int i = l; i <= r; i++) {
         if (a[x][i] != '?') return false;     
     }
     return true;
}

void go(int x, int y) {
     int l = y;
     while (l > 0 && (l == y || a[x][l] == '?')) l--;
     l++;
     int r = y;
     while (r <= m && (r == y || a[x][r] == '?')) r++;
     r--;
     int lx = x;
     int rx = x;
     while (lx > 0 && (lx == x || check(lx, l, r))) lx--;
     lx++;
     while (rx <= n  && (rx == x || check(rx, l, r))) rx++;
     rx--;
     for (int i = lx; i <= rx; i++) {
         for (int j = l; j <= r; j++)
             a[i][j] = a[x][y];     
     }
     return;
}

int main() {
    /*srand(time(NULL));
    #ifndef ONLINE_JUDGE
    freopen(fname".in", "r", stdin);
    freopen(fname".out", "w", stdout);
    #endif                   */
    ios_base::sync_with_stdio(0);
    int test;
    cin >> test;
    for (int tt = 1; tt <= test; tt++) {
        cin >> n >> m;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                cin >> a[i][j];            
            }
        }
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (!was[a[i][j] - 'A']) {
                   was[a[i][j] - 'A'] = 1;
                   go(i, j);
                }            
            }        
        }
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= m; j++) was[a[i][j] - 'A'] = 0;
        cout << "Case #" << tt << ":\n";
        for (int i = 1; i <= n; i++, cout << endl) {
            for (int j = 1; j <= m; j++) {
                cout << a[i][j] << "";            
            }        
        }
    }
    #ifndef ONLINE_JUDGE
       cerr << clock() << " ms";
    #endif
    return 0;
}