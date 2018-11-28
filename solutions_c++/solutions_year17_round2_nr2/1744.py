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

int T, N;
char A ='R', B='Y', C='B', AB='O', BC='G', AC='V';
int cntA, cntB, cntC, cntAB, cntBC, cntAC;
string ans;

void solve(){
    ans = "";
    A ='R', B='Y', C='B', AB='O', BC='G', AC='V';
    if( cntB > cntC ){ swap(cntB, cntC); swap(B, C); }
    if( cntA > cntB ){ swap(cntA, cntB); swap(A, B); }
    if( cntB > cntC ){ swap(cntB, cntC); swap(B, C); }
    if( cntA + cntB < cntC ){
        ans = "IMPOSSIBLE";
        return;
    }
    while( cntA < cntB ){
        if( cntC > 0 ) { ans = ans + C; cntC--; }
        if( cntB > 0 ) { ans = ans + B; cntB--; }
    }
    while( cntC > cntA ){
        if( cntC > 0 ) { ans = ans + C; cntC--; }
        if( cntB > 0 ) { ans = ans + B; cntB--; }
        if( cntC > 0 ) { ans = ans + C; cntC--; }
        if( cntA > 0 ) { ans = ans + A; cntA--; }
    }
    while( cntA ){
        if( cntC > 0 ) { ans = ans + C; cntC--; }
        if( cntB > 0 ) { ans = ans + B; cntB--; }
        if( cntA > 0 ) { ans = ans + A; cntA--; }
    }
}
int main()
{
    freopen("B-small-attempt2.in","r",stdin);
    freopen("B-small-attempt2_out.txt","w",stdout);
    ios::sync_with_stdio(false);

    cin >> T;
    for(int i=1; i<=T; i++){
        cin >> N;
        cin >> cntA >> cntAB >> cntB >> cntBC >> cntC >> cntAC;
        solve();
        cout << "Case #" << i << ": " << ans << endl;
    }

    return 0;
}
