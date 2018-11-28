#include <bits/stdc++.h>
using namespace std;
template <class T> int size(const T &x) { return x.size(); }
#define rep(i,a,b) for (__typeof(a) i=(a); i<(b); ++i)
#define iter(it,c) for (__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;
const int INF = ~(1<<31); // 2147483647

const double EPS = 1e-9;
const double pi = acos(-1);
typedef unsigned long long ull;
typedef vector<vi> vvi;
typedef vector<vii> vvii;
template <class T> T smod(T a, T b) { return (a % b + b) % b; }

int main(){
    int T;
    cin >> T;
    rep(t, 1, T+1){
        int n,k;
        cin >> n >> k;
        priority_queue<int> p;
        p.push(n);
        rep(i,0,k-1){
            int r = p.top(); p.pop();
            p.push(r/2);
            p.push((r-1)/2);
        }
        int r = p.top();
        int hi = r/2;
        int lo = (r-1)/2;
        cout << "Case #" << t << ": " << hi << " " << lo << endl;
    }
    return 0;
}
