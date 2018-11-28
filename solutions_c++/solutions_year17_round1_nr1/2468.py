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

#define floop(i,n) for( int i = 0 ; (i) < (n) ; i++ )
typedef long long int64;
typedef pair<int,int> pii;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const int64 inf64 = ((int64)1 << 62) - 1;
const long double pi = 3.1415926535897932384626433832795;

string s;
int R, C;

bool find_next( char grid[][26] , int r , int c ){
    for( int i = r + 1 ; i < R ; i++ ){
        if( grid[i][c] != '?' ){
            char ch = grid[i][c];
            for( i ; i >= r ; i-- ){
                grid[i][c] = ch;
            }
            cout << "row: " << ch << endl;
            return true;
        }
    }
    for( int i = c + 1 ; i < C; i++ ){
        if( grid[r][i] != '?'){
            char ch = grid[r][i];
            for( i ; i >= c ; i-- ){
                grid[r][i] = ch;
            }
            cout << "col";
            return true;
        }
    }
    return false;
}

void solve(){
    char grid[26][26] = {""};
    cin >> R >> C;
    floop(i,R){
        cin >> grid[i];
    }
    bool done = false;
    //row first
    for( int i = 0 ; i < R ; i++ ){
        char ch = '?';
        for( int j = 0 ; j < C ; j++ ){
            if( grid[i][j] != '?' ){
                ch = grid[i][j];
                break;
            }
        }
        for ( int j = 0; j < C ; j++ ){
            if( grid[i][j] != '?' ){
                ch = grid[i][j];
            }
            grid[i][j] = ch;
        }
    }
    for( int j = 0 ; j < C ; j++ ){
        char ch = '?';
        for( int i = 0 ; i < R ; i++ ){
            if( grid[i][j] != '?' ){
                ch = grid[i][j];
                break;
            }
        }
        for ( int i = 0; i < R ; i++ ){
            if( grid[i][j] != '?' ){
                ch = grid[i][j];
            }
            grid[i][j] = ch;
        }
    }
    floop(i,R){
        cout << grid[i] << endl;
    }
}

int main(){
    int t;
    cin >> t;
    floop(i,t){
        printf( "Case #%d:\n" , i + 1 );
        solve();
    }
}
