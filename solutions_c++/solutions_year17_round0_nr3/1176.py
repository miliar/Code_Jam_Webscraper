#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef double dd;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;

#define FOR(i,a,b) for (int (i) = (a); (i) < (b); (i)++)
#define DOW(i,b,a) for (int i = (b); i >= (a); i--)
#define pb(a) push_back(a)
#define ALL(a) (a).begin(),(a).end()
#define fi first
#define se second

template<typename T>
void print_array(T* arr, int num) {
   FOR(i, 0, num) cout << arr[i] << ' ';
   cout << endl;
}

template<typename T> 
void print_vector(vector<T> vec) {
   FOR(i,0,vec.size()) cout << vec[i] << ' ';
   cout << endl;
}

int t;
ll n,k;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0);
    freopen("test.txt", "r", stdin);
    freopen("C3.out", "w", stdout);
    cin >> t;
    FOR(p,1,t+1) {
        cin >> n >> k;
        map<ll,ll> ma;
        ma[n] = 1;
        ll ls, rs;
        while (k > 0) {
            pair<ll,ll> cur = *ma.rbegin();
            ma.erase(cur.fi);
            k -= cur.se;
            rs = (cur.fi - 1) / 2, ls = (cur.fi - 1) / 2 + (cur.fi - 1) % 2;
            ma[ls] += cur.se;
            ma[rs] += cur.se;
        }
        printf("Case #%d: %lld %lld\n", p,ls,rs);
    }
}