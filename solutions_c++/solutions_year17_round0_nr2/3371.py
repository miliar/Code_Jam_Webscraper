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
LL N;
LL ans;
int digit[100];
int len;

void getDigit(){
    len = 0;
    LL tmp = N;
    while( tmp > 0 ){
        digit[len++] = tmp % 10;
        tmp /= 10;
    }
}
void solve(){
    if( N < 10 ){
        ans = N;
        return;
    }
    getDigit();
    for(int i=len-1; i>0; i--){
        if( digit[i] <= digit[i-1] ) continue;
        int p = i;
        while( p < len ){
            if( digit[p] < digit[i] ) break;
            p++;
        }
        p--;
        ans = 0;
        for(int i=len-1; i>p; i--) ans = ans*10+digit[i];
        ans = ans*10 + digit[p]-1;
        for(int i=p-1; i>=0; i--) ans = ans*10+9;
        return;
    }
    ans = N;
    return;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large_out.txt","w",stdout);
    ios::sync_with_stdio(false);

    cin >> T;
    for(int i=1; i<=T; i++){
        cin >> N;
        solve();
        cout << "Case #" << i << ": " << ans << endl;
    }

    return 0;
}
