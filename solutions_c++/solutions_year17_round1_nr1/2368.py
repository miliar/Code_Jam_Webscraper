#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <string.h>
#include <vector>
#include <queue>
#include <list>
#include <set>
#include <map>
#include <iomanip>

#define LL long long
#define LD long double

using namespace std;

const int MAXN = 1001000;

int T;
int R, C;
string s;
char x[100][100];

void solve(){
    int cnt = 0;
    char tmp;
    for(int i=0; i<R; i++){
        cnt = 0;
        for(int j=0; j<C; j++){
            if( x[i][j] != '?' ){
                for(int k=0; k<j; k++) x[i][k] = x[i][j];
                cnt = 1;
                break;
            }
        }
        if( cnt == 0 ) continue;
        for(int j=0; j<C; j++){
            if( x[i][j] != '?' ) tmp = x[i][j];
            else x[i][j] = tmp;
        }
    }
    for(int j=0; j<C; j++){
        cnt = 0;
        for(int i=0; i<R; i++){
            if( x[i][j] != '?' ){
                for(int k=0; k<i; k++) x[k][j] = x[i][j];
                cnt = 1;
                break;
            }
        }
        if( cnt == 0 ) continue;
        for(int i=0; i<R; i++){
            if( x[i][j] != '?' ) tmp = x[i][j];
            else x[i][j] = tmp;
        }
    }
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large_out.txt","w",stdout);
    ios::sync_with_stdio(false);

    cin >> T;
    for(int i=1; i<=T; i++){
        cin >> R >> C;
        for(int j=0; j<R; j++){
            cin >>s;
            for(int k=0; k<C; k++) x[j][k] = s[k];
        }
        solve();
        cout << "Case #" << i << ": " << endl;
        for(int j=0; j<R; j++){
            for(int k=0; k<C; k++) cout << x[j][k];
            cout << endl;
        }
    }

    return 0;
}
