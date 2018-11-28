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

int T;
ll n , K;

int main(){
    cin >> T;
    rep(i,0,T){
        cout << "Case #" << i + 1 << ": ";
        cin >> n >> K;
        map<ll,ll> S;S.insert(mp(n,1));
        while(K){
            auto e = *S.rbegin();
            if(K <= e.se){
                cout << e.fi / 2 << " " << (e.fi - 1) / 2 << endl;
                break;
            } else{
                K -= e.se;
                S.erase(e.fi);
                S[e.fi / 2] += e.se;
                S[(e.fi - 1) / 2] += e.se;
            }
        }
    }
    return 0;
}
