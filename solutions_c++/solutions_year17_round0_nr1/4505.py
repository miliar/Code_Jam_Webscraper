#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <numeric>
#include <functional>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <sstream>
#include <string>
#define _repargs(_1,_2,_3,name,...) name
#define _rep(i,n) repi(i,0,n)
#define repi(i,a,b) for(int i=(int)(a);i<(int)(b);++i)
#define rep(...) _repargs(__VA_ARGS__,repi,_rep,)(__VA_ARGS__)
#define all(x) (x).begin(),(x).end()
#define mod 1000000007
#define inf 2000000007
#define mp make_pair
#define pb push_back
typedef long long ll;
using namespace std;
template <typename T>
inline void output(T a, int p = 0) {
    if(p) cout << fixed << setprecision(p)  << a << "\n";
    else cout << a << "\n";
}
// end of template

int main() {
    cin.tie(0);
    ios::sync_with_stdio(0);
    // source code
    
    int T;
    cin >> T;
    rep(t, T){
        string s;
        int k;
        cin >> s >> k;
        int cnt = 0;
        rep(i, s.size() - k + 1){
            if(s[i] == '-'){
                rep(j, i, i + k){
                    if(s[j] == '-') s[j] = '+';
                    else s[j] = '-';
                }
                cnt++;
            }
        }
        bool ok = true;
        rep(i, s.size()){
            if(s[i] == '-') ok = false;
        }
        cout << "Case #" << t + 1 << ": ";
        if(!ok){
            output("IMPOSSIBLE");
        }
        else{
            output(cnt);
        }
        
    }
    
    return 0;
}
