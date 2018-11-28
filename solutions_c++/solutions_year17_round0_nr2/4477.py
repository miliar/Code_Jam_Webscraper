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

ll ten[19];

int main() {
    cin.tie(0);
    ios::sync_with_stdio(0);
    // source code
    
    ten[0] = 1;
    rep(i, 1, 19){
        ten[i] = ten[i - 1] * 10;
    }
    
    int T;
    cin >> T;
    rep(t, T){
        ll N;
        cin >> N;
        int len = 0;
//        while(1){
//            if(ten[len] > N){
//                break;
//            }
//            len++;
//        }
        

        
        vector<int> A(19);
        rep(i, 19){
            A[i] = (N / ten[i]) % 10;
        }
//        voutput(A);
        
        rep(i, 18){
            if(A[i + 1] > A[i]){
                A[i + 1]--;
                rep(j, i + 1){
                    A[j] = 9;
                }
            }
        }
//        voutput(A);
        ll ans = 0;
        rep(i, 19){
            ans += A[i] * ten[i];

        }
        cout << "Case #" << t + 1 << ": ";
        output(ans);
    }
    
    return 0;
}
