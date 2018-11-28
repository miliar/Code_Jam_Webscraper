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
    string s;
    cin >> s;
    int pos = s.size();
    for(int i = 0; i < s.size() - 1; i++){
        if(s[i] > s[i + 1]){
            pos = i; break;
        }
    }
    if(pos == s.size()) {cout << s << endl; return;}
    while(pos > 0 && s[pos] == s[pos - 1]) pos--;
    s[pos]--;
    for(int i = pos + 1; i < s.size(); i++){
        s[i] = '9';
    }
    while(s[0] == '0') s = s.substr(1);
    cout << s << endl;
}

int main()
{
    //ios_base::sync_with_stdio(false);
    //if(debug)
        freopen("/Users/ozzy/Documents/B-large.in.txt","r", stdin);
        freopen("/Users/ozzy/Documents/outt.txt","w", stdout);
    int t;
    cin >> t;
    for(int tt = 1; tt <= t; tt++){
        cout << "Case #" << tt << ": ";
        solve();
    }
    return 0;
}
