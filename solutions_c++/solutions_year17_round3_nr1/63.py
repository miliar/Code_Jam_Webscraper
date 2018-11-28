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

pair<int,int> a[MX];

double solve(){
    int n, k;
    cin >> n >> k;
    for(int i = 0; i < n; i++){
        cin >> a[i].first >> a[i].second;
    }
    sort(a, a + n);
    priority_queue<long long> h;
    long long hh = 0;

    for(int i = 0; i < k - 1; i++){
        long long curr = a[i].second * 2; curr *= a[i].first;
        hh += curr;
        h.push(-curr);
    }
    //cerr << hh << endl;
    //cerr << h.size() << endl;
    double ans = -1;
    for(int i = k - 1; i < n; i++){
        long long curr = a[i].second * 2; curr *= a[i].first;
        hh += curr;
        double r = a[i].first;
        double s = hh * M_PI + M_PI * r * r;
        if(s > ans) ans = s;
        h.push(-curr);
        hh += h.top();
        //cerr << hh << endl;
        h.pop();
    }
    return ans;
}

int main()
{
    freopen("/Users/ozzy/Documents/A-large.in.txt","r", stdin);
    freopen("/Users/ozzy/Documents/out.in.txt","w", stdout);

    ios_base::sync_with_stdio(false);
    int t;
    cin >> t;
    for(int tt = 1; tt <= t; tt++){
        printf("Case #%d: %.10f\n", tt, solve());
    }
    return 0;
}
