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

int main(){
    int T;
    scanf("%d",&T);
    rep(i,0,T){
        int D , n;
        scanf("%d%d",&D,&n);
        long double ans = 1e50;
        int K , S;
        rep(i,0,n){
            scanf("%d%d",&K,&S);
            long double t = (long double)(D - K) / S;
            ans = min(ans , D / t);
        }
        printf("Case #%d: %.16lf\n",i + 1 , (double)ans);
    }
    return 0;
}
