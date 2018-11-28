#pragma comment(linker, "/STACK:36777216")
#include <iostream>
#include <stdio.h>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <sstream>
#include <utility>
#include <map>
#include <set>
#include <memory.h>
using namespace std;

#define forn(i, n) for(int i = 0; i < (int) (n); ++i) 
#define fore(i, a, b) for(int i = (int) (a); i < (int) (b); ++i) 
#define fores(i, a, b, step) for(int i = (int) (a); i < (int) (b); i += step) 
#define forv(i, v) for(int i = 0; i < int(v.size()); ++i)

#define ll long long 
#define ld long double 
#define PLL pair <ld, ld> 
#define PII pair <int, int> 
#define x first
#define y second
#define pb push_back 
#define sz size

const int MAXN = 1010;
const ld EPS = 1e-9;
const ld INF = 1e9;

int d, n;
PII a[6];

int c = 0;
string Q="ROYGBV";

vector <string> buf[6];
vector <int> res;

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
   
    int tk;
    cin >> tk;

    forn(ii, tk) {
        cin >> n;

        string ans = "";

        forn(i, 6) {
            buf[i].clear();
            buf[i].reserve(MAXN);
            int x;
            cin >> x;
            a[i] = PII(x, i);
        }
      
        fores(i, 1, 6, 2) {
            if (ans != "") {
                break;
            }
            fores(j, 0, 6, 2) {
                if (j == i - 1 || j == ((i + 1) % 6)) {
                    continue;
                }
                if (a[i].x * 2 > a[j].x) {
                    ans = "IMPOSSIBLE";
                    break;
                }
                string s1 = "", s2 = "";
                s1 += Q.substr(j, 1);
                s1 += Q.substr(i, 1);
                s1 += Q.substr(j, 1);
                s2 += Q.substr(j, 1);
                forn(k, a[i].x) {
                    buf[j].pb(s1);
                }
                forn(k, a[j].x - 2 * a[i].x) {
                    buf[j].pb(s2);
                }
                n -= 2 * a[i].x;
                a[j].x -= a[i].x;
                a[i].x = 0;
            }
        }

        if (ans != "") {
            printf("Case #%d: %s\n", ii + 1, ans.c_str());
            continue;
        } 
        bool ok = 1;
        int ls = -1, fs = -1;       

        res.clear();
        //cout << n << endl;
        forn(i, 6) {
            //cout << a[i].x << " ";
        }
        //cout << endl << "ok" << endl;
        forn(i, n) {
            sort(a, a + 6);
            bool found = 0;
            for(int j = 5; j > -1; --j) {
                if (a[j].x > 0 && a[j].y != ls) {
                    found = 1;
                    if (fs == ' ') {
                        fs = a[j].y;
                    }
                    ls = a[j].y;
                    --a[j].x;
                    res.push_back(a[j].y);
                    break;
                }
            }
            
            if (!found) {
                ans = "IMPOSSIBLE";
                break;
            }
        } 
        //cout << "dog" << res.size() << endl;
        forn(i, 6) {
            //cout << a[i].x << " ";
        }
        if (ans != "") {
            printf("Case #%d: %s\n", ii + 1, ans.c_str());
            continue;
        }
        if (res[0] == res[n - 1]) {
            swap(res[n - 1], res[n - 2]);
        }
        if (res[0] == res[n - 1]) {
            ans = "IMPOSSIBLE";
        }
        forn(i, n - 1) {
            if (res[i] == res[i + 1]) {
                ans = "IMPOSSIBLE";
            }
        }
        if (ans != "") {
            printf("Case #%d: %s\n", ii + 1, ans.c_str());
            continue;
        }
        forn(i, n) {
            int idx = res[i];
            ans += buf[idx].back();
            buf[idx].pop_back();
        }
 
        printf("Case #%d: %s\n", ii + 1, ans.c_str());
    }


    return 0;
};

