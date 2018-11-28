#pragma comment(linker, "/STACK:60000000")
#define _CRT_SECURE_NO_WARNINGS
/* Based on Sergey Rogulenko solution*/

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

string s;

void solve(){
    int N=0,R=0,O = 0, Y=0, G=0, B=0, V=0;
    int r,o,y,g,b,v;
    cin >> N >> R >> O >> Y >> G >> B >> V;
    char res[1001] = "";
    /*greedy approach*/
    if( R > 0 ){
        res[0] = 'R';
        R--; N--;
    } else if ( Y > 0 ){
        res[0] = 'Y';
        Y--; N--;
    } else if ( B > 0 ){
        res[0] = 'B';
        B--; N--;
    } else {
        cout << "IMPOSSIBLE" << endl;
        return;
    }
    int i = 0;
    while( true ){
        if( N == 0 && res[i] != res[0] ){
            break;
        }
        if( res[i] == 'R' ){
            if( G > 0 ){
                if( R == 0 && N > 1 ){
                    cout << "IMPOSSIBLE" << endl;
                    return;
                } else if ( R == 0 && N == 1){
                    res[++i] = 'G';
                    cout << res << endl;
                    return;
                }
                res[++i] = 'G';
                res[++i] = 'R';
                G--; R--; N--; N--;
            } else if ( Y > B - (res[0]=='Y') ){
                res[++i] = 'Y';
                Y--; N--;
            } else if ( B > 0 ){
                res[++i] = 'B';
                B--; N--;
            } else if ( N != 0 || res[0] == 'R' ){
                cout << "IMPOSSIBLE" << endl;
                return;
            } else {
                break;
            }
        } else if ( res[i] == 'Y' ){
            if( V > 0 ){
                if( Y == 0 && N > 1){
                    cout << "IMPOSSIBLE" << endl;
                    return;
                } else if ( Y == 0 && N == 1){
                    res[++i] = 'V';
                    cout << res << endl;
                    return;
                }
                res[++i] = 'V';
                res[++i] = 'Y';
                V--; Y--; N--; N--;
            } else if ( B > R - (res[0]=='B') ){
                res[++i] = 'B';
                B--; N--;
            } else if ( R > 0 ){
                res[++i] = 'R';
                R--; N--;
            } else if ( N != 0 || res[0] == 'R' ){
                cout << "IMPOSSIBLE" << endl;
                return;
            } else {
                break;
            }
        } else if ( res[i] == 'B' ){
            if( O > 0 ){
                if( B == 0 && N > 1){
                    cout << "IMPOSSIBLE" << endl;
                    return;
                } else if ( B == 0 && N == 1){
                    res[++i] = 'O';
                    cout << res << endl;
                    return;
                }
                res[++i] = 'O';
                res[++i] = 'B';
                O--; B--; N--; N--;
            } else if ( R > Y - (res[0]=='R') ){
                res[++i] = 'R';
                R--; N--;
            } else if ( Y > 0 ){
                res[++i] = 'Y';
                Y--; N--;
            } else if ( N != 0 || res[0] == 'R' ){
                cout << "IMPOSSIBLE" << endl;
                return;
            } else {
                break;
            }
        }
       //cout << R << " " << B << " " << Y <<  endl;
    }
    /*do stuff*/
    cout << res << endl;
}

int main(){
    int t;
    cin >> t;
    floop(i,t){
        printf( "Case #%d: " , i + 1 );
        solve();
    }
}
