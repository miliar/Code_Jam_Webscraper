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
//const long long infLL = 1e18;
//const int MX2 = 10100500; //  e7
//const long long INF = 1e18 + 0.5;
const int MX = 1200500; //       e5
const int SZ = 2110;
//const int delta = 1 << 20;


void solve(){
    long long n;
    cin >> n;
    list<pair<long long, long long>> q;
    q.push_back({n, 1});
    long long k;
    cin >> k;
    while(k){
        long long cnt = 0 ;
        long long v = q.front().first;
        while(q.front().first == v){
            cnt += q.front().second;
            q.pop_front();
        }
        v--;
        if(cnt >= k){
            cout << (v + 1) / 2 << ' ' << v / 2 << endl;
            return;
        }
        k -= cnt;
        q.push_back({(v + 1) / 2, cnt});
        q.push_back({v / 2 , cnt});
    }
}

int main()
{
    //ios_base::sync_with_stdio(false);
    //if(debug)
        freopen("/Users/ozzy/Documents/C-large.in.txt","r", stdin);
        freopen("/Users/ozzy/Documents/outt.txt","w", stdout);
    int t;
    cin >> t;
    for(int tt = 1; tt <= t; tt++){
        cout << "Case #" << tt << ": ";
        solve();
    }
    return 0;
}
