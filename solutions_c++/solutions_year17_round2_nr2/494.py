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

int ma(int R, int B, int Y){
    return max(R, max(B, Y));
}

int main() {
    cin.tie(0);
    ios::sync_with_stdio(0);
    // source code
    
    int T;
    cin >> T;
    rep(t, T){
        
        int N, R, O, Y, G, B, V;
        cin >> N >> R >> O >> Y >> G >> B >> V;
        string ans = "";
        
        if(R + Y >= B && R + B >= Y && B + Y >= R){
            int m = ma(R, Y, B);
            if(R == m){
                int by = B + Y - R;
                rep(i, B - by) ans += "RB";
                rep(i, Y - by) ans += "RY";
                rep(i, by) ans += "RBY";
            }
            else if(B == m){
                int ry = R + Y - B;
                rep(i, R - ry) ans += "BR";
                rep(i, Y - ry) ans += "BY";
                rep(i, ry) ans += "BRY";
            }
            else{
                int rb = R + B - Y;
                rep(i, R - rb) ans += "YR";
                rep(i, B - rb) ans += "YB";
                rep(i, rb) ans += "YRB";
            }
            
            
        }
        else{
            ans = "IMPOSSIBLE";
        }
        
        
        cout << "Case #" << t + 1 << ": ";
        
        output(ans);
        
    }
    
    return 0;
}
