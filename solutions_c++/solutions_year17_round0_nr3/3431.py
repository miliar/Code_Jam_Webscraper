#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define MOD 1000000007
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
ll n, k;
pair<ll, ll> solve() {
        priority_queue<pair<ll, ll> > q;
        q.push(mp(n, 1));
        while(true) {
                pair<ll, ll> p = q.top();
                q.pop();
                if(p.f % 2) {
                        q.push(mp(p.f / 2, p.s << 1));
                } else {
                        q.push(mp(p.f / 2, p.s));
                        q.push(mp(p.f / 2 - 1, p.s));
                }
                k -= p.s;
                if(k <= 0) {
                        if(p.f % 2)
                                return mp(p.f / 2, p.f / 2);
                        else    return mp(p.f / 2 - 1, p.f / 2);
                }
        }
}
int main()
{
        freopen("C-small-2-attempt0.in", "r", stdin);
        freopen("out.txt", "w", stdout);
        int t, c = 0;
        scanf("%d", &t);
        while(t--) {
                c++;
                cin >> n >> k;
                cout << "Case #" << c << ": ";
                pair<ll, ll> ans = solve();
                cout << ans.s << " " << ans.f << "\n";
        }
        return 0;
}
