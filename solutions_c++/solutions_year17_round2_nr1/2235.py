#pragma comment(linker, "/STACK:60000000")
#define _CRT_SECURE_NO_WARNINGS
/* Based on Sergey Rogulenko solution */

#include <bitset>
#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <sstream>
#include <iomanip>
#include <complex>
#include <queue>
#include <functional>
using namespace std;

#define floop(i, n) for(int i = 0; i < (int)(n); i++)
#define bloop(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define last(a) int(a.size() - 1)
#define all(a) a.begin(), a.end()
#define seta(a,x) memset (a, x, sizeof (a))
#define I (int)
#define next NEXT64
#define prev PREV64
#define y1 Y164

typedef long long int64;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const int64 inf64 = ((int64)1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;


int64 D, N;

void solve(){
    int64 K[1000];
    int64 S[1000];
    ldb t, tmax = 0;
    cin >> D >> N;
    floop( i , N ){
        cin >> K[i] >> S[i];
        t = (D-K[i])/( (ldb) 1.0*S[i]);
        if( t > tmax ){
            tmax = t;
        }
    }
    cout << setprecision(16) << D/tmax << endl;
}

int main(){
    int t;
    cin >> t;
    floop(i,t){
        printf( "Case #%d: " , i + 1 );
        solve();
    }
}
