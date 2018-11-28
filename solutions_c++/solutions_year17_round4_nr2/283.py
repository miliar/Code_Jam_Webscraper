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

const int N = 1010;
int T , n , c , m , people[N] , ticket[N];

void solve(){
    memset(people , 0 , sizeof(people));
    memset(ticket , 0 , sizeof(ticket));
    cin >> n >> c >> m;
    int ansa = 0 , ansb = 0;
    rep(i,0,m){
        int P , B;
        cin >> P >> B;
        people[B] ++;
        ticket[P] ++;
    }
    ansa = *max_element(people + 1 , people + c + 1);
    int sum = 0;
    rep(i,1,n+1) {
        sum += ticket[i];
        ansa = max(ansa , (sum + i - 1) / i);
    }
    rep(i,1,n+1) if(ticket[i] > ansa) ansb += ticket[i] - ansa;
    cout << ansa << " " << ansb << endl;
}

int main(){
    cin >> T;
    rep(i,1,T+1) {
        cout << "Case #" << i << ": ";
        solve();
        cerr << "Case #" << i << ": solved" << endl;
    }
    return 0;
}
