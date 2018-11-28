#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <unordered_set>
#include <cmath>
#include <list>
#include <chrono>
#include <thread>

using namespace std;

const bool debug = false;

#ifndef M_PI
    const double M_PI = acos(-1.0);
#endif // M_PI

#define y1 roman_kaban
#define rank oryshych_konb
#define ull unsigned long long
//#define ll long long
//const int mod = int(1e9) + 7;
//const int inf = 1e9;
//const long long infLL = 1e16;
//const int MX2 = 10100500; //  e7
//const long long INF = 1e18 + 0.5;
const int MX = 300500; //       e5
const int SZ = 1100;
//const int delta = 1 << 19;

int a[SZ][SZ];
int b[SZ];

int main()
{
    ios_base::sync_with_stdio(false);
    //if(debug)
//freopen("/Users/ozzy/Documents/in.txt","r", stdin);
freopen("/Users/ozzy/Documents/B-small-attempt0.in-2.txt","r", stdin);
freopen("/Users/ozzy/Documents/out.txt","w", stdout);
    int t;
    cin >> t;
    for(int tt = 1; tt <= t; tt++){
        cout << "Case #" << tt << ": ";
        int n, c, m;
        cin >> n >> c >> m;
        if(n == 1) {cout << m << ' ' << 0 << "\n"; continue;}
        for(int i = 0; i < c; i++){
            b[i] = 0;
            for(int j = 0; j < n; j++)
                a[i][j] = 0;
        }
        while(m--){
            int pos, x;
            cin >> pos >> x; pos--; x--;
            a[x][pos]++;
            b[x]++;
        }
        int ans = max(b[0], b[1]);
        int z = 0;
        for(int i = 0; i < n; i++){
            if(a[0][i] + a[1][i] > ans) {
                    if(i == 0) ans = a[0][i] + a[1][i]; else
                        z = a[0][i] + a[1][i] - ans;
            }
        }
        cout << ans << ' ' << z << "\n";
    }
    return 0;
}
