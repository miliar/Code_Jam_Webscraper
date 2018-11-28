/* You lost the game. */

#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <numeric>
#include <cassert>
#include <unordered_set>
#include <unordered_map>
#include <fstream>
#include <vector>

#define fin(i,n) for (int i = 0; i < n; i++)
#define fin2(i,a,b) for (int i = a; i < b; i++)

#define mp make_pair
#define mt make_tuple
#define pb push_back
#define mod 1000000007

#define si(n) scanf("%d", &n)
#define sii(n,m) scanf("%d %d", &n, &m)
#define siii(n,m,k) scanf("%d %d %d", &n, &m, &k)
#define sl(n) scanf("%lld", &n)
#define sll(n,m) scanf("%lld %lld", &n, &m)
#define slll(n,m,k) scanf("%lld %lld %lld", &n, &m, &k)
#define sd(n) scanf("%lf", &n)
#define sdd(n,m) scanf("%lf %lf", &n, &m)
#define sddd(n,m,k) scanf("%lf %lf %lf", &n, &m, &k)
#define ss(s) scanf("%s", s)
#define sai(t,n) fin(i,n) { scanf("%d", &t[i]); }
#define sal(t,n) fin(i,n) { scanf("%lld", &t[i]); }
#define sad(t,n) fin(i,n) { scanf("%lf", &t[i]); }

#define pi(n) printf("%d\n", n)
#define pc(n) printf("%c\n", n)
#define ps(s) printf("%s\n", s);
#define pii(n,m) printf("%d %d\n", n, m)
#define pl(n) printf("%lld\n", n)
#define pll(n,m) printf("%lld %lld\n", n, m)
#define pd(n) printf("%lf\n", n)
#define pai(t,n) fin(i,n) { printf("%d ", t[i]); } printf("\n"); 
#define pal(t,n) fin(i,n) { printf("%lld ", t[i]); } printf("\n"); 

#define L long long int
#define D double
#define PII pair<int, int>
#define VPII vector<PII>
#define VL vector<L>
#define VI vector<int>
#define VVI vector<VI>

using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    L n,k,r, tot, rep;
    VL tri;
    si(t);
    fin(i, t) {
        sll(n,k);
        map<L, L> table;
        set<L>::iterator it;
        set<L> liste;
        table[n] = 1;
        liste.insert(n);
        tot = 1;
        r = 1;
        if (k == 1) { 
            if (n % 2 == 0) { printf("Case #%d: %lld %lld\n", (i+1), n/2, n/2 - 1); }
            else { printf("Case #%d: %lld %lld\n", (i+1), n/2, n/2); }
            continue;
        }
        tri.pb(n);
        int vu = 0;
        while (r < k) {
            tot = r;
            map<L, L> temp;
            set<L> lt;
            for (it = liste.begin(); it != liste.end(); it++) {
                L m = *it;
                if (m % 2 == 0) { 
                    if (m/2 > 0) {
                        lt.insert(m/2);
                        if (temp.find(m/2) == temp.end()) { temp[m/2] = table[m]; }
                        else { temp[m/2] += table[m]; }
                    }
                    if (m/2 - 1 > 0) {
                        lt.insert(m/2 - 1);
                        if (temp.find(m/2 - 1) == temp.end()) { temp[m/2 - 1] = table[m]; }
                        else { temp[m/2 - 1] += table[m]; }
                    }
                }
                else { 
                    if (m/2 > 0) {
                        lt.insert(m/2);
                        if (temp.find(m/2) == temp.end()) { temp[m/2] = 2*table[m]; }
                        else { temp[m/2] += 2*table[m]; }
                    }
                }
            }
            table = temp;
            liste = lt;
            tri.clear();
            r = tot;
            for (it = liste.begin(); it != liste.end(); it++) {
                tri.pb(*it);
                r += table[*it];
            }
        }
        sort(tri.begin(), tri.end());
        r = tot;
        fin(j, tri.size()) {
            int e = tri[tri.size()-1-j];
            r += table[e];
            if (r >= k) { 
                rep = e; break; 
            }
        }
        if (rep % 2 == 0) { printf("Case #%d: %lld %lld\n", (i+1), rep/2, rep/2 - 1); }
        else { printf("Case #%d: %lld %lld\n", (i+1), rep/2, rep/2); }
    }
    return 0;
} 