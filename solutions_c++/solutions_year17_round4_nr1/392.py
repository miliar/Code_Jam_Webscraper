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

bool emp(vector<int> A){
    rep(i, 1, A.size()){
        if(A[i] > 0) return false;
    }
    return true;
}

int main() {
    cin.tie(0);
    ios::sync_with_stdio(0);
    // source code
    
    int T;
    cin >> T;
    rep(t, T){
        
        int N, P;
        cin >> N >> P;
        vector<int> G(N);
        rep(i, N) cin >> G[i];
        vector<int> A(P);
        rep(i, N) A[G[i] % P]++;
        
        int ans = A[0];
        
        if(P == 2){
            ans += (A[1] + 1) / 2;
        }
        else if(P == 3){
            int m = min(A[1], A[2]);
            ans += m;
            A[1] -= m, A[2] -= m;
            ans += (A[1] + 2) / 3 + (A[2] + 2) / 3;
        }
        else{
            ans += A[2] / 2;
            A[2] %= 2;
            int m = min(A[1], A[3]);
            ans += m;
            A[1] -= m, A[3] -= m;
            ans += A[1] / 4;
            ans += A[3] / 4;
            A[1] %= 4;
            A[3] %= 4;
            int p = 0;
            if(A[2] > 0){
                p = 2;
                ans++;
            }
            rep(i, max(A[1], A[3])){
                if(p == 0) ans++;
                (p += 1) %= 4;
            }
        }
        
        
        
        
        cout << "Case #" << t + 1 << ": ";
        
        output(ans);
        
    }

    
    return 0;
}
