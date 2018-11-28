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
long double eps = 1e-9;

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

const int N = 20100;

string s;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int test;
    cin >> test;
    for (int j(1); j <= test; j++) {
        string s;
        cin >> s;
        bool fl = true;
        while (fl) {
            fl = false;
            for (int i(0);i < s.size() - 1; i++) {
                if (s[i] > s[i+1]) {
                    s[i] = (char)(s[i] - 1);
                    fl = true;
                    while(++i < s.size())
                        s[i] = '9';
                }
            }
        }
        if(s[0] == '0') {
            int x = s.size() - 1;
            s.clear();
            for(int i(0);i<x;i++)
                s.pb('9');
        }
        cout << "Case #" << j << ": " << s << "\n";
    }
}
