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

int dig[20],len;

bool check(ll x) {
    len = 0;
    while(x) dig[len++] = x%10 , x/=10;
    rep(i,0,len-1) if(dig[i]<dig[i+1]) return false;
    return true;
}

int main(){
    int T;cin >> T;
    rep(i,0,T){
        ll n;cin >> n;
        ll res = 0;
        if(check(n)) res = n;
        for(ll s=1;s<=n;s*=10){
            if(check(n / s * s - 1)) res = max(res , n / s * s - 1);
        }
        cout << "Case #" << i+1 <<": " << res << endl;
    }
    return 0;
}
