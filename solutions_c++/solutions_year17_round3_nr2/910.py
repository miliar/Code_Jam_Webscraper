#include <vector>
#include <map>
#include <set>
#include <complex>
#include <ctime>
#include <iostream>
#include <cmath>
#include <stack>
#include <sstream>
#include <stdio.h>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cassert>
#include <sstream>

const long double PI(acosl(-1.0));
const long double E = 2.71828182845904;
long double eps = 1e-10;

#define pb push_back
#define mp(a,b) make_pair(a,b)
#define all(x) x.begin(), x.end()
#define sqr(x) ((x)*(x))
#define F first
#define S second
#define inf (int)(1e9+7)
#define infll (ll)(1e18+3)
#define sz(x) ((int)x.size())
#define bits(x) __builtin_popcount(x)
#define bitsl(x) __builtin_popcountll(x)

using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;
typedef vector <ll > vll;
typedef vector<int> vi;
typedef pair < ll, ll > pll;
typedef pair < int, int > pii;
typedef vector<vi> vii;
typedef int huint;

using namespace std;

const int N = 1050;

struct par {
    int st, fn, ord;
};

bool comp(par &a, par &b) {
    return a.st < b.st;
}

int main() {
    freopen("input.txt", "r", stdin);
     freopen("output.txt", "w", stdout);

    int test;
    cin >> test;
    for (int tt(1);tt <=test; tt++) {
        int n,m;
        cin >> n >> m;
        vector<par> p1(n);
        vector<par> p2(m);
        int s1, s2;
        int ans = 0;

        for(int i(0);i<n;i++) {
            cin >> p1[i].st >> p1[i].fn;
            s1 += p1[i].fn - p1[i].st;
            p1[i].ord = 0;
        }
        for(int i(0);i<m;i++) {
            cin >> p2[i].st >> p2[i].fn;
            s2 += p2[i].fn - p2[i].st;
            p2[i].ord = 1;
        }
        sort(all(p1), comp);
        sort(all(p2), comp);

        int lt = 1440;

        if(n + m == 1) {
            ans = 2;
        } else {
            if (n == 1 && m == 1) ans = 2;
            else {
                if (n == 2) {
                    int x = p1[1].fn - p1[0].st;
                    if (x <= 720) {
                        ans = 2;
                    } else {
                        int y = p1[0].fn + (lt - p1[1].st);
                        if (y <= 720) ans = 2;
                        else             ans = 4;
                    }
                } else {
                    int x = p2[1].fn - p2[0].st;
                    if (x <= 720) {
                        ans = 2;
                    } else {
                        int y = p2[0].fn + (lt - p2[1].st);
                        if (y <= 720) ans = 2;
                        else             ans = 4;
                    }
                }
            }
        }

        cout << "Case #" << tt << ": ";
        cout << ans << "\n";
    }
}
