#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;

#define OK puts("OK")
#define EL printf("\n")
#define sz(A) (int) A.size()
#define end(A) (int) A.size()-1
#define FOR(i,l,r) for (auto i=l;i<=r;i++)
#define FOD(i,l,r) for (auto i=l;i>=r;i--)

int T;
map<ll,ll> m;
queue<ll> st;
ll n, k;

void solve(int test) {
    cin >> n >> k;
    m.clear();
    while (!st.empty()) st.pop();
    st.push(n); m[n] = 1ll;
    while (!st.empty()) {
        ll p = st.front(); st.pop();
//    cout << p << " " << m[p] << endl;
        if (k <= m[p]) {
            printf("Case #%d: ", test);
            cout << p/2 << " " << (p-1)/2 << endl;
            return;
        }
        k -= m[p];
        if (m[p/2] == 0) st.push(p/2); m[p/2] += m[p];
        if (m[(p-1)/2] == 0) st.push((p-1)/2); m[(p-1)/2] += m[p];
    }
}

int main()
{
//    freopen("inp.txt", "r", stdin);
    //freopen("C-large.in", "r", stdin);
    //freopen("output-large.txt", "w", stdout);

    cin >> T;
    FOR(test, 1, T) solve(test);

    return 0;
}







