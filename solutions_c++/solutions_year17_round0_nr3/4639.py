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
        ll N, K;
        cin >> N >> K;
        vector<int> A(N + 1);
        A[N] = 1;
        ll cur = N;
        rep(i, K - 1){
            while(1){
                if(A[cur] == 0) cur--;
                else break;
            }
            if(cur % 2 == 1){
                A[cur]--;
                A[(cur - 1) / 2] += 2;
            }
            else{
                A[cur]--;
                A[cur / 2]++;
                A[cur / 2 - 1]++;
            }
//            cout << cur << endl;
//            voutput(A);
        }
        
        int num = 0;
        rep(i, N + 1){
            if(A[i] > 0) num = i;
        }
        
        
        cout << "Case #" << t + 1 << ": ";
        
        if(num % 2 == 0){
            cout << num / 2 << " " << num / 2 - 1;
        }
        else{
            cout << (num - 1) / 2 << " " << (num - 1) / 2;
        }
        cout << endl;
        
    }
    
    return 0;
}
