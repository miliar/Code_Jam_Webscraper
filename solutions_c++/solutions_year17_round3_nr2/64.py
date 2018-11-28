#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <cmath>
#include <list>
#include <chrono>
#include <thread>

using namespace std;

//template<typename T>
//using Matrix2D = std::vector<vector<T>>;

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
//const long long infLL = 1e11;
//const int MX2 = 10100500; //  e7
//const long long INF = 1e18 + 0.5;
const int MX = 200500; //       e5
//const int SZ = 1100;
//const int delta = 1 << 19;

pair<pair<int,int>,int> a[MX];
pair<int,int> b[MX];
int r[2];


int solve(){
    int x, y;
    cin >> x >> y;
    int n = x + y;
    r[0] = r[1] = 12 * 60;
    for(int i = 0; i < x; i++){
        cin >> a[i].first.first >> a[i].first.second;
        a[i].second = 0;
        r[0] -= a[i].first.second - a[i].first.first;
    }
    for(int i = x; i < n; i++){
        cin >> a[i].first.first >> a[i].first.second;
        a[i].second = 1;
        r[1] -= a[i].first.second - a[i].first.first;
    }
    sort(a, a + n);
    a[n] = a[0];
    a[n].first.first += 24 * 60;
    a[n].first.second += 24 * 60;
    int ans = 0;
    int k = 0;
    for(int i = 1; i <= n; i++){
        if(a[i].second == a[i - 1].second){
            b[k++] = {a[i].first.first - a[i - 1].first.second, a[i].second};
        } else ans++;
    }
    sort(b, b + k);
    for(int i = 0; i < k; i++){
        int p = b[i].second;
        if(r[p] >= b[i].first){
            r[p] -= b[i].first;
        } else ans += 2;
    }
    return ans;
}

int main()
{
    //freopen("/Users/ozzy/Documents/in.txt","r", stdin);
    freopen("/Users/ozzy/Documents/B-large.in.txt","r", stdin);
    freopen("/Users/ozzy/Documents/out.in.txt","w", stdout);

    ios_base::sync_with_stdio(false);
    int t;
    cin >> t;
    for(int tt = 1; tt <= t; tt++){
        printf("Case #%d: %d\n", tt, solve());
    }
    return 0;
}
