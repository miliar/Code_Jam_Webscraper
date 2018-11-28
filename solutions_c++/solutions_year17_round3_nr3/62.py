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

int a[MX];

int read(){
    int ans;
    cin >> ans;
    char c;
    cin >> c;
    for(int i = 0; i < 4; i++){
        cin >> c;
        ans *= 10;
        ans += c - '0';
    }
    return ans;
}

double solve(){
    int n, k;
    cin >> n >> k;
    int total = read();
    //cout << total << endl;
    for(int i = 0; i < n; i++){
        //cout << read() << endl;
        a[i] = read();
    }
    while(total--){
        int p = 0;
        for(int i =0 ; i < n; i++){
            if(a[i] < a[p]) p = i;
        }
        a[p]++;
    }

    double ans = 1;
    for(int i = 0; i < n; i++){
            //cerr << a[i] << endl;
        ans *= a[i] / 10000.0;
    }
    return ans;
}

int main()
{
    //freopen("/Users/ozzy/Documents/in.txt","r", stdin);
    freopen("/Users/ozzy/Documents/C-small-1-attempt0.in.txt","r", stdin);
    freopen("/Users/ozzy/Documents/out.in.txt","w", stdout);

    ios_base::sync_with_stdio(false);
    int t;
    cin >> t;
    for(int tt = 1; tt <= t; tt++){
        printf("Case #%d: %.10f\n", tt, solve());
    }
    return 0;
}
