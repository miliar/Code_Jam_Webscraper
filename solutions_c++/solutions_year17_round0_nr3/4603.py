#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

const int maxn = 1e5 + 100, inf = 1e9 + 100, mod = 1e9 + 7;

int test;

map<ll, ll> q;

int main(){
    #ifdef ONPC
    ifstream cin("a.in");
    ofstream cout("a.out");
    #else
    //ifstream cin("a.in");
    //ofstream cout("a.out");
    #endif // ONPC
    ios::sync_with_stdio(0);
    cin >> test;
    for (int iter = 1; iter <= test; iter++){
        ll n, k;
        cin >> n >> k;
        q.clear();
        q[-n] = 1;
        while (k > 1){
            ll pos = q.begin()->first, cnt = q[pos];
            pos = -pos;
            ll rem = min(cnt, k - 1);
            q[-(pos - 1) / 2] += rem;
            q[-(pos / 2)] += rem;
            q[-pos] -= rem;
            if (q[-pos] == 0)
                q.erase(-pos);
            k -= rem;
        }
        ll pos = q.begin()->first;
        pos = -pos;
        cout << "Case #" << iter << ": " << pos / 2 << ' ' << (pos - 1) / 2 << '\n';
    }
}
