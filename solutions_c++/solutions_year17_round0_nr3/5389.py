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
#define forv(i, v) for(int i = 0; i < int(v.size()); ++i)

#define ll long long 
#define ld long double 
#define x first
#define y second
#define PII pair <ll, ll> 
#define pb push_back 
#define sz size

const int MAXN = 1000;
const ld EPS = 1e-9;
const ld PI = 3.1415926535897932384626433832795;
int tk;

ll n, k;
PII cut(ll x) {
    //cout << "cut" << " " << x << endl;
    return PII(x / 2, (x - 1) / 2);
}

int main() {
    //freopen("input.txt", "rt", stdin);
    //freopen("output.txt", "wt", stdout);
   
    scanf("%d\n", &tk); 
    
    forn(ii, tk) {
        cin >> n >> k;
        
        PII ans = PII(-1, -1);
        
        
        printf("Case #%d: ", ii + 1);
        
        vector <PII> a, b;
        a.clear();
        a.pb(PII(n, 1));
        
        while (true) {
            sort(a.begin(), a.end());
            reverse(a.begin(), a.end());
            forn(i, a.size()) {
                if (a[i].y >= k) {
                    ans = cut(a[i].x);
                    break;
                }
                k -= a[i].y;
            }
            if (ans != PII(-1, -1)) break;
            b = a;
            a.clear();
            forn(i, b.size()) {
                ll x = b[i].x, cnt = b[i].y;
                a.pb(PII((x - 1) / 2, cnt));
                a.pb(PII(x / 2, cnt));
            }
            sort(a.begin(), a.end());
            forn(i, (int)(a.size()) - 1) {
                if (a[i].x == a[i + 1].x) {
                    a[i + 1].y += a[i].y;
                    a[i].x = 0;
                }
            }
            
           
            for(int i = int(a.size()) - 1; i > -1; --i) {
                if (a[i].x == 0) {
                    a.erase(a.begin() + i, a.begin() + i + 1);
                }
            }
            
        }
        cout << ans.x << " " << ans.y << endl;
    }

    return 0;
};

