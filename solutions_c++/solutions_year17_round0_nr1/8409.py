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

map <string, bool> was;
map <string, int>  lvl;

int main() {
    srand(time(NULL));
    /*#ifndef ONLINE_JUDGE
    freopen(fname".in", "r", stdin);
    freopen(fname".out", "w", stdout);
    #endif*/
    int test;
    cin >> test;
    for (int tt = 1; tt <= test; tt++) {
        string s;
        int k;
        cin >> s >> k;
        vector <string> q;
        q.pb(s);
        was[s] = 1, lvl[s] = 0;
        int l = 0;
        while (l < size(q)) {
              string v = q[l++];
              for (int i = 0; i < size(v) - k + 1; i++) {
                  string to = v;
                  for (int j = i; j <= i + k - 1; j++) {
                      if (v[j] == '+')
                         to[j] = '.';
                      else to[j] = '+';                  
                  }
                  if (was[to]) continue;
                  lvl[to] = lvl[v] + 1;
                  was[to] = 1;
                  q.pb(to);            
              }        
        }
        cout << "Case #" << tt << ": ";
        string res (size(s), '+');
        if (was[res] == 0) {
           cout << "IMPOSSIBLE\n";
        } else cout << lvl[res] << endl;
        for (auto v : q) was[v] = 0;
    }
    #ifndef ONLINE_JUDGE
       cerr << clock() << " ms";
    #endif
    return 0;
}