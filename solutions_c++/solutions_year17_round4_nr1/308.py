//#include {{{
#include <iostream>
#include <cassert>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <ctime>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <string>
#include <bitset>
#include <vector>
#include <complex>
#include <algorithm>
using namespace std;
// }}}
// #define {{{
typedef long long ll;
typedef double db;
typedef pair<int,int> pii;
typedef vector<int> vi;
#define de(x) cout << #x << "=" << x << endl
#define rep(i,a,b) for(int i=a;i<(b);++i)
#define per(i,a,b) for(int i=(b)-1;i>=(a);--i)
#define all(x) (x).begin(),(x).end()
#define sz(x) (int)(x).size()
#define mp make_pair
#define pb push_back
#define fi first
#define se second
// }}}

const int N = 110;
int T , n , P , a[110] , f[N][N][N] , cnt[4];

void Update(int &x,int d){
    x = max(x , d);
}
int solve(){
    cin >> n >> P;
    memset(cnt , 0 , sizeof(cnt));
    rep(i,0,n) {
        cin >> a[i];
        a[i] %= P;
        cnt[a[i]]++;
    }
    memset(f , 0 , sizeof(f));
    rep(i,0,cnt[1] + 1) rep(j,0,cnt[2] + 1) rep(k,0,cnt[3] + 1){
        int plus = (i * 1 + j * 2 + k * 3) % P == 0;
        if(i != cnt[1]) Update(f[i+1][j][k] , f[i][j][k] + plus);
        if(j != cnt[2]) Update(f[i][j+1][k] , f[i][j][k] + plus);
        if(k != cnt[3]) Update(f[i][j][k+1] , f[i][j][k] + plus);

    }
    return cnt[0] + f[cnt[1]][cnt[2]][cnt[3]];
}


int main(){
    cin >> T;
    rep(i,1,T+1) {
        cout << "Case #" << i << ": " << solve() << endl;
        cerr << "Case #" << i << ": solved" << endl;
    }
    return 0;
}
