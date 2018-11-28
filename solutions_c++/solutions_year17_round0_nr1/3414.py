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
string s;
int side[2000];
int K;
int ans;

void solve(){
    int len = s.size();
    for(int i=0; i<len; i++){
        side[i] = ( s[i] == '+' ? 1 : 0 );
    }
    ans = 0;
    for(int i=0; i<=len-K; i++){
        if( side[i] == 0 ){
            ans++;
            for(int j=0; j<K; j++) side[i+j] = 1-side[i+j];
        }
    }
    for(int i=len-K+1; i<len; i++){
        if( side[i] == 0 ) ans = -1;
    }
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large_out.txt","w",stdout);
    ios::sync_with_stdio(false);

    cin >> T;
    for(int i=1; i<=T; i++){
        cin >> s >> K;
        ans = 0;
        solve();
        if( ans != -1 ) cout << "case #" << i << ": " << ans << endl;
        else cout << "case #" << i << ": IMPOSSIBLE" << endl;
    }

    return 0;
}
