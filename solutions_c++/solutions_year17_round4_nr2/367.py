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

template <typename T> inline void voutput(T &v){
    rep(i, v.size()){
        if (i) cout << " " << v[i];
        else cout << v[i];
    }
    cout << endl;
}

int main() {
    cin.tie(0);
    ios::sync_with_stdio(0);
    // source code
    
    int T;
    cin >> T;
    rep(t, T){
        
        int N, C, M;
        cin >> N >> C >> M;
        vector<pair<int, int>> A(M);
        rep(i, M) cin >> A[i].first >> A[i].second, A[i].first--, A[i].second--;
        vector<int> count(C, 0);
        int ma = 0;
        rep(i, M) {
            count[A[i].second]++;
            ma = max(ma, count[A[i].second]);
        }
        
//        voutput(count);
        
        vector<int> height(N, 0);
        rep(i, M){
            height[A[i].first]++;
        }
        
        int h = 0;
        int num = 0;
        rep(i, N){
            num += height[i];
            h = max(h, (num + i) / (i + 1));
        }
        
        
        int y = max(ma, h);
        int z = 0;
        
        rep(i, N){
            if(y < height[i]){
                z += height[i] - y;
            }
        }
        
        
        cout << "Case #" << t + 1 << ": ";
        
        cout << y << " " << z << endl;
        
    }

    
    return 0;
}
