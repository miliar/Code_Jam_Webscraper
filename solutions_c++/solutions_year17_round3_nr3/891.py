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

const int N = 100500;

int n;
double a[N];

bool can(double x, double sum) {
     double res = 0;
     for (int i = 1; i <= n; i++)
         res += max(0.0, x - a[i]);
     return res <= sum;
}

int main() {
    srand(time(NULL));
    /*#ifndef ONLINE_JUDGE
    freopen(fname".in", "r", stdin);
    freopen(fname".out", "w", stdout);
    #endif   */
    int test;
    cin >> test;
    for (int tt = 1; tt <= test; tt++) {
        int k;
        cin >> n >> k;
        double u;
        cin >> u;
        for (int i = 1; i <= n; i++) {
            cin >> a[i];
        }
        double l = 0.0;
        double r = 1.0;
        for (int i = 1; i <= 1000; i++) {
            double mid = (l + r) / 2;
            if (can(mid, u)) {
               l = mid;            
            } else {
               r = mid;
            }
        }
        double ans = 1.0;
        for (int i = 1; i <= n; i++) {
            ans = (ans * max(a[i], l));                    
        }
        cout << "Case #" << tt << ": ";
        cout << fixed << setprecision(6) << ans << endl;
    }
    #ifndef ONLINE_JUDGE
       cerr << clock() << " ms";
    #endif
    return 0;
}